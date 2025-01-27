import sys
import os
import re

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(__file__))
import json
import pathlib

from PySide6.QtWidgets import QMainWindow, QStyle, QFileDialog
from PySide6.QtCore import Qt, Signal, QThread
from PySide6.QtGui import QIcon, QPixmap, QShortcut

from nomad_camels.gui.mainWindow_v2 import Ui_MainWindow
from importlib import resources
from nomad_camels import graphics

from nomad_camels.frontpanels.helper_panels.button_move_scroll_area import (
    Drop_Scroll_Area,
)
from nomad_camels.utility import (
    load_save_functions,
    variables_handling,
    number_formatting,
    theme_changing,
    update_camels,
    logging_settings,
    qthreads,
)
from nomad_camels.ui_widgets import options_run_button, warn_popup
from nomad_camels.extensions import extension_contexts

from collections import OrderedDict
import importlib


camels_github = "https://github.com/FAU-LAP/NOMAD-CAMELS"
camels_github_pages = "https://fau-lap.github.io/NOMAD-CAMELS/"


class MainWindow(Ui_MainWindow, QMainWindow):
    """Main Window for the program. Connects to all the other classes."""

    protocol_stepper_signal = Signal(int)
    run_done_file_signal = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        sys.stdout = self.textEdit_console_output.text_writer
        sys.stderr = self.textEdit_console_output.error_writer

        self.sample_widget.layout().setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.user_widget.layout().setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.session_upload_widget.layout().setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.button_area_meas = Drop_Scroll_Area(self, 120, 120)
        self.button_area_manual = Drop_Scroll_Area(self, 120, 120)
        self.meas_widget.layout().addWidget(self.button_area_meas, 2, 0, 1, 4)
        self.manual_widget.layout().addWidget(self.button_area_manual, 2, 0, 1, 3)

        self.setWindowTitle(
            "NOMAD CAMELS - Configurable Application for Measurements, Experiments and Laboratory-Systems"
        )
        self.setWindowIcon(QIcon(str(resources.files(graphics) / "camels_icon.png")))

        image = QPixmap()
        image.load(str(resources.files(graphics) / "CAMELS_horizontal.png"))
        self.label_logo.setPixmap(image)

        arrow = self.style().standardIcon(QStyle.SP_ArrowUp)
        self.label_arrow.setPixmap(arrow.pixmap(130, 130))

        icon = self.style().standardIcon(QStyle.SP_MediaPause)
        self.pushButton_pause.setIcon(icon)
        icon = self.style().standardIcon(QStyle.SP_MediaPlay)
        self.pushButton_resume.setIcon(icon)
        icon = self.style().standardIcon(QStyle.SP_MediaStop)
        self.pushButton_stop.setIcon(icon)

        self.setStyleSheet("QSplitter::handle{background: gray;}")
        self.protocol_stepper_signal.connect(self.progressBar_protocols.setValue)

        # saving / loading
        self.__save_dict__ = {}
        if os.name == "nt":
            name = os.environ["COMPUTERNAME"]
        else:
            name = os.uname()[1]
        self._current_preset = [name]
        self.active_instruments = {}
        variables_handling.devices = self.active_instruments
        self.protocols_dict = OrderedDict()
        variables_handling.protocols = self.protocols_dict
        self.manual_controls = OrderedDict()
        self.preset_save_dict = {
            "_current_preset": self._current_preset,
            "active_instruments": self.active_instruments,
            "protocols_dict": self.protocols_dict,
            "manual_controls": self.manual_controls,
        }
        self.preferences = {}
        self.load_preferences()
        if self.preferences["auto_check_updates"]:
            update_camels.auto_update(self)
        self.load_state()

        self.open_windows = []
        self.current_protocol_device_list = []

        self.button_area_meas.order_changed.connect(self.protocol_order_changed)

        self.active_controls = {}
        self.open_plots = []

        # user and sample data
        self.sampledata = {}
        self.userdata = {}
        self.active_user = "default_user"
        self.active_sample = "default_sample"

        self.nomad_user = None
        self.nomad_sample = None

        self.comboBox_upload_type.addItems(
            ["auto upload", "ask after run", "don't upload"]
        )
        self.comboBox_upload_type.setCurrentText("don't upload")
        self.comboBox_upload_type.currentTextChanged.connect(self.show_nomad_upload)

        self.checkBox_use_nomad_sample.clicked.connect(self.show_nomad_sample)

        self.pushButton_editUserInfo.clicked.connect(self.edit_user_info)
        self.load_user_data()
        self.pushButton_editSampleInfo.clicked.connect(self.edit_sample_info)
        self.load_sample_data()
        variables_handling.CAMELS_path = os.path.dirname(__file__)

        self.comboBox_user_type.addItems(["local user", "NOMAD user"])
        self.comboBox_user_type.currentTextChanged.connect(self.change_user_type)
        self.change_user_type()

        self.pushButton_login_nomad.clicked.connect(self.login_logout_nomad)
        self.pushButton_nomad_sample.clicked.connect(self.select_nomad_sample)

        # actions
        self.actionSettings.triggered.connect(self.change_preferences)
        self.actionSave_Preset_As.triggered.connect(self.save_preset_as)
        self.actionSave_Preset.triggered.connect(self.save_state)
        self.actionNew_Preset.triggered.connect(self.new_preset)
        self.actionLoad_Backup_Preset.triggered.connect(self.load_backup_preset)
        self.action_driver_builder.triggered.connect(self.launch_device_builder)
        self.actionEPICS_driver_builder.triggered.connect(self.launch_epics_builder)
        self.actionExport_from_databroker.triggered.connect(self.launch_data_exporter)
        self.actionReport_Bug.triggered.connect(
            lambda x: os.startfile(f"{camels_github}/issues")
        )
        self.actionDocumentation.triggered.connect(
            lambda x: os.startfile(camels_github_pages)
        )
        self.actionUpdate_CAMELS.triggered.connect(
            lambda x: update_camels.question_message_box(self)
        )
        self.actionExport_CAMELS_hdf5_to_csv_json.triggered.connect(
            self.launch_hdf5_exporter
        )
        self.actionQuit.triggered.connect(self.close)

        # buttons
        self.pushButton_add_manual.clicked.connect(self.add_manual_control)

        self.pushButton_manage_instr.clicked.connect(self.manage_instruments)
        self.pushButton_add_meas.clicked.connect(self.add_measurement_protocol)
        self.pushButton_import_protocol.clicked.connect(
            self.import_measurement_protocol
        )

        self.pushButton_stop.clicked.connect(self.stop_protocol)
        self.pushButton_pause.clicked.connect(self.pause_protocol)
        self.pushButton_resume.clicked.connect(self.resume_protocol)

        self.pushButton_clear_log.clicked.connect(self.textEdit_console_output.clear)
        self.pushButton_close_plots.clicked.connect(self.close_plots)

        QShortcut("Ctrl+s", self).activated.connect(self.save_state)

        # self.show()
        self.adjustSize()

        self.run_engine = None
        self.databroker_catalog = None
        self.still_running = False
        self.re_subs = []
        self.protocol_module = None
        self.protocol_savepath = ""
        self.running_protocol = None

        # Extension Contexts
        self.extension_user = {}
        self.extension_sample = {}
        self.eln_context = extension_contexts.ELN_Context(self)
        self.extension_contexts = {"ELN_Context": self.eln_context}
        self.extensions = []
        self.load_extensions()
        self.actionManage_Extensions.triggered.connect(self.manage_extensions)

        self.importer_thread = qthreads.Additional_Imports_Thread(self)
        self.importer_thread.start(priority=QThread.LowPriority)

    def check_password_protection(self):
        if (
            "password_protection" in self.preferences
            and self.preferences["password_protection"]
        ):
            from nomad_camels.utility.password_widgets import Password_Dialog

            dialog = Password_Dialog(
                self, compare_hash=self.preferences["password_hash"]
            )
            if not dialog.exec():
                return False
        return True

    def manage_extensions(self):
        if not self.check_password_protection():
            return
        self.setCursor(Qt.WaitCursor)
        from nomad_camels.extensions.extension_management import Extension_Manager
        from nomad_camels.utility.update_camels import restart_camels

        dialog = Extension_Manager(self.preferences, self)
        if dialog.exec():
            # self.load_extensions()
            load_save_functions.save_preferences(self.preferences)
            warn_popup.WarnPopup(
                self,
                "Extensions will be loaded after restart.",
                "Restart required",
                info_icon=True,
            )
            restart_camels(self, True)
        self.setCursor(Qt.ArrowCursor)

    def load_extensions(self):
        if not "extensions" in self.preferences:
            from nomad_camels.utility.load_save_functions import standard_pref

            self.preferences["extensions"] = standard_pref["extensions"]
        if not "extension_path" in self.preferences:
            from nomad_camels.utility.load_save_functions import standard_pref

            self.preferences["extension_path"] = standard_pref["extension_path"]
        sys.path.append(self.preferences["extension_path"])
        for f in pathlib.Path(self.preferences["extension_path"]).rglob("*"):
            for extension in self.preferences["extensions"]:
                if not f.name == extension:
                    continue
                sys.path.append(str(f.parent))
                try:
                    extension_module = importlib.import_module(extension)
                except (ModuleNotFoundError, AttributeError) as e:
                    print(f"Could not load extension {extension}.\n{e}")
                    continue
                config = getattr(extension_module, "EXTENSION_CONFIG")
                name = config["name"]
                contexts = {}
                for context in config["required_contexts"]:
                    contexts[context] = self.extension_contexts[context]
                self.extensions.append(getattr(extension_module, name)(**contexts))

    def bluesky_setup(self):
        # IMPORT bluesky only if it is needed
        from bluesky import RunEngine
        from bluesky.callbacks.best_effort import BestEffortCallback
        import databroker

        self.run_engine = RunEngine()
        bec = BestEffortCallback()
        self.run_engine.subscribe(bec)
        self.change_catalog_name()
        try:
            self.databroker_catalog = databroker.catalog[
                self.preferences["databroker_catalog_name"]
            ]
        except KeyError:
            print("Could not find databroker catalog, using temporary")
            self.databroker_catalog = databroker.temp().v2
        self.run_engine.subscribe(self.databroker_catalog.v1.insert)
        self.run_engine.subscribe(self.protocol_finished, "stop")
        self.still_running = False
        self.re_subs = []
        self.protocol_module = None
        self.protocol_savepath = ""
        self.running_protocol = None

    def with_or_without_instruments(self):
        """ """
        available = False
        if self.active_instruments:
            available = True
        self.main_splitter.setHidden(not available)
        self.pushButton_resume.setHidden(not available)
        self.pushButton_pause.setHidden(not available)
        self.pushButton_stop.setHidden(not available)
        self.progressBar_protocols.setHidden(not available)
        # self.textEdit_console_output.setHidden(not available)
        # self.pushButton_clear_log.setHidden(not available)
        self.pushButton_close_plots.setHidden(not available)
        self.label_arrow.setHidden(available)
        self.label_no_instruments.setHidden(available)

    def manage_instruments(self):
        """ """
        self.setCursor(Qt.WaitCursor)
        # IMPORT ManageInstruments only if it is needed
        from nomad_camels.frontpanels.manage_instruments import ManageInstruments

        dialog = ManageInstruments(
            active_instruments=self.active_instruments, parent=self
        )
        self.setCursor(Qt.ArrowCursor)
        if dialog.exec():
            self.active_instruments.clear()
            self.active_instruments.update(dialog.active_instruments)
        self.with_or_without_instruments()

    def add_to_open_windows(self, window):
        """

        Parameters
        ----------
        window :


        Returns
        -------

        """
        self.open_windows.append(window)
        window.closing.connect(lambda x=window: self.open_windows.remove(x))

    def add_to_plots(self, plot):
        """

        Parameters
        ----------
        plot :


        Returns
        -------

        """
        self.open_plots.append(plot)
        plot.closing.connect(lambda x=plot: self.open_plots.remove(x))
        self.add_to_open_windows(plot)

    def close_plots(self):
        """ """
        for plot in list(self.open_plots):
            plot.close()

    # --------------------------------------------------
    # Overwriting parent-methods
    # --------------------------------------------------
    def close(self) -> bool:
        """Calling the save_state method when closing the window."""
        ret = super().close()
        # if self.preferences['autosave']:
        #     self.save_state()
        return ret

    def closeEvent(self, a0):
        """Calling the save_state method when closing the window.

        Parameters
        ----------
        a0 :


        Returns
        -------

        """
        for window in list(self.open_windows):
            window.close()
        if self.open_windows:
            a0.ignore()
            return
        super().closeEvent(a0)
        if self.preferences["autosave"]:
            self.save_state()

    # --------------------------------------------------
    # user / sample methods
    # --------------------------------------------------
    def login_logout_nomad(self):
        """Handles logging in / out of NOMAD when the respective button is pushed"""
        # IMPORT nomad_communication only if it is needed
        from nomad_camels.nomad_integration import nomad_communication

        if nomad_communication.token:
            nomad_communication.logout_of_nomad()
            self.pushButton_login_nomad.setText("NOMAD login")
            self.label_nomad_user.setText("not logged in")
            self.pushButton_nomad_sample.setText("select NOMAD sample")
            self.nomad_user = None
            self.nomad_sample = None
        else:
            self.login_nomad()
        self.show_nomad_sample()
        self.show_nomad_upload()

    def login_nomad(self):
        """Handles the login to NOMAD. If the login is successful, the UI is
        adapted to show all the NOMAD-related buttons."""
        # IMPORT nomad_communication only if it is needed
        from nomad_camels.nomad_integration import nomad_communication

        nomad_communication.ensure_login(self)
        if not nomad_communication.token:
            return
        self.pushButton_login_nomad.setText("NOMAD logout")
        user_data = nomad_communication.get_user_information(self)
        for key in ["created", "is_admin", "is_oasis_admin"]:
            if key in user_data:
                user_data.pop(key)
        self.label_nomad_user.setText(user_data["name"])
        self.nomad_user = user_data

    def show_nomad_upload(self):
        """Shows / hides the settings for directly uploading data to NOMAD."""
        nomad = self.nomad_user is not None
        self.nomad_upload_widget.setHidden(not nomad)
        auto_upload = self.comboBox_upload_type.currentText() == "auto upload"
        self.comboBox_upload_choice.setHidden(not nomad or not auto_upload)
        if nomad:
            # IMPORT nomad_communication only if it is needed
            from nomad_camels.nomad_integration import nomad_communication

            uploads = nomad_communication.get_user_upload_names(self)
            self.comboBox_upload_choice.clear()
            self.comboBox_upload_choice.addItems(uploads)

    def change_user_type(self):
        """Shows / hides the ui-elements depending on the type of user,
        e.g. the NOMAD login button is only shown if NOMAD user is selected."""
        user_type = self.comboBox_user_type.currentText()
        if user_type not in ["local user", "NOMAD user"]:
            return
        nomad = user_type == "NOMAD user"
        self.user_widget_nomad.setHidden(not nomad)
        self.user_widget_default.setHidden(nomad)
        if not nomad:
            self.nomad_user = None
        else:
            self.login_nomad()
        self.show_nomad_sample()
        self.show_nomad_upload()

    def edit_user_info(self):
        """Calls dialog for user-information when
        pushButton_editUserInfo is clicked.

        The opened AddRemoveDialoge contains columns for Name, E-Mail,
        Affiliation, Address, ORCID and Phone of the user.
        If the dialog is canceled, nothing is changed, otherwise the new
        data will be written into self.userdata.

        Parameters
        ----------

        Returns
        -------

        """
        # IMPORT pandas and add_remove_table only if it is needed
        import pandas as pd
        from nomad_camels.ui_widgets import add_remove_table

        self.active_user = self.comboBox_user.currentText()
        headers = [
            "name",
            "email",
            "affiliation",
            "address",
            "orcid",
            "telephone_number",
        ]
        tableData = pd.DataFrame.from_dict(self.userdata, "index")
        dialog = add_remove_table.AddRemoveDialoge(
            headerLabels=headers,
            parent=self,
            title="User-Information",
            askdelete=True,
            tableData=tableData,
        )
        if dialog.exec():
            # changing the returned dict to dataframe and back to have a
            # dictionary that is formatted as {name: {'Name': name,...}, ...}
            dat = dialog.get_data()
            if re.search(r"[^\w\s]", str(dat["name"][0])):
                    raise ValueError(
                        "Name contains special characters.\nPlease use only letters, numbers and whitespace."
                    )
            # remove trailing whitespace from name
            dat["name"][0] = dat["name"][0].strip()
            dat["Name2"] = dat["name"]
            data = pd.DataFrame(dat)
            data.set_index("Name2", inplace=True)
            self.userdata = data.to_dict("index")
        self.comboBox_user.clear()
        self.comboBox_user.addItems(self.userdata.keys())
        if self.active_user in self.userdata:
            self.comboBox_user.setCurrentText(self.active_user)

    def save_user_data(self):
        """Calling the save_dictionary function with the savefile as
        %localappdata%/userdata.json and self.userdata as dictionary.

        Parameters
        ----------

        Returns
        -------

        """
        self.active_user = self.comboBox_user.currentText()
        userdic = {"active_user": self.active_user}
        userdic.update(self.userdata)
        load_save_functions.save_dictionary(
            os.path.join(load_save_functions.appdata_path, "userdata.json"), userdic
        )

    def load_user_data(self):
        """Loading the dictionary from %localappdata%/userdata.json,
        selecting the active user and saving the rest into self.userdata.

        Parameters
        ----------

        Returns
        -------

        """
        userdat = {}
        userfile = os.path.join(load_save_functions.appdata_path, "userdata.json")
        if os.path.isfile(userfile):
            with open(userfile, "r", encoding="utf-8") as f:
                string_dict = json.load(f)
            load_save_functions.load_save_dict(
                string_dict, userdat, update_missing_key=True
            )
        if "active_user" in userdat:
            self.active_user = userdat["active_user"]
            userdat.pop("active_user")
        self.userdata = userdat
        self.comboBox_user.addItems(userdat.keys())
        if not self.active_user == "default_user":
            self.comboBox_user.setCurrentText(self.active_user)

    def edit_sample_info(self):
        """Calls dialog for user-information when
        pushButton_editSampleInfo is clicked.

        The opened AddRemoveDialoge contains columns for Name,
        Identifier, and Preparation-Info.
        If the dialog is canceled, nothing is changed, otherwise the new
        data will be written into self.userdata.

        Parameters
        ----------

        Returns
        -------

        """
        # IMPORT pandas and add_remove_table only if it is needed
        import pandas as pd
        from nomad_camels.ui_widgets import add_remove_table

        self.active_sample = self.comboBox_sample.currentText()
        headers = ["name", "sample_id", "description"]
        tableData = pd.DataFrame.from_dict(self.sampledata, "index")
        dialog = add_remove_table.AddRemoveDialoge(
            headerLabels=headers,
            parent=self,
            title="Sample-Information",
            askdelete=True,
            tableData=tableData,
        )
        if dialog.exec():
            # changing the returned dict to dataframe and back to have a
            # dictionary that is formatted as {name: {'Name': name,...}, ...}
            dat = dialog.get_data()
            if re.search(r"[^\w\s]", str(dat["name"][0])):
                raise ValueError(
                    "Sample name contains special characters.\nPlease use only letters, numbers and whitespace."
                )
            dat["name"][0] = dat["name"][0].strip()
            dat["Name2"] = dat["name"]
            data = pd.DataFrame(dat)
            data.set_index("Name2", inplace=True)
            self.sampledata = data.to_dict("index")
        self.comboBox_sample.clear()
        self.comboBox_sample.addItems(self.sampledata.keys())
        if self.active_sample in self.sampledata.keys():
            self.comboBox_sample.setCurrentText(self.active_sample)

    def save_sample_data(self):
        """Calling the save_dictionary function with the savefile as
        %localappdata%/sampledata.json and self.sampledata as dictionary.

        Parameters
        ----------

        Returns
        -------

        """
        self.active_sample = self.comboBox_sample.currentText()
        sampledic = {"active_sample": self.active_sample}
        sampledic.update(self.sampledata)
        load_save_functions.save_dictionary(
            os.path.join(load_save_functions.appdata_path, "sampledata.json"), sampledic
        )

    def load_sample_data(self):
        """Loading the dictionary from %localappdata%/sampledata.json,
        selecting the active sample and saving the rest into self.sampledata.

        Parameters
        ----------

        Returns
        -------

        """
        sampledat = {}
        samplefile = os.path.join(load_save_functions.appdata_path, "sampledata.json")
        if os.path.isfile(samplefile):
            with open(samplefile, "r", encoding="utf-8") as f:
                string_dict = json.load(f)
            load_save_functions.load_save_dict(
                string_dict, sampledat, update_missing_key=True
            )
        if "active_sample" in sampledat:
            self.active_sample = sampledat["active_sample"]
            sampledat.pop("active_sample")
        self.sampledata = sampledat
        self.comboBox_sample.addItems(sampledat.keys())
        if not self.active_sample == "default_sample":
            self.comboBox_sample.setCurrentText(self.active_sample)

    def select_nomad_sample(self):
        # IMPORT sample_selection only if it is needed
        from nomad_camels.nomad_integration import sample_selection

        dialog = sample_selection.Sample_Selector(self)
        if dialog.exec():
            self.nomad_sample = dialog.sample_data
            if "name" in self.nomad_sample:
                name = self.nomad_sample["name"]
            else:
                name = self.nomad_sample["Name"]
            self.pushButton_nomad_sample.setText(f'change sample "{name}"')
        self.show_nomad_sample()

    def show_nomad_sample(self):
        nomad = self.nomad_user is not None
        self.sample_widget_nomad.setHidden(not nomad)
        active_sample = self.nomad_sample is not None
        use_nomad = self.checkBox_use_nomad_sample.isChecked()
        use_nomad_sample = active_sample and use_nomad and nomad
        self.sample_widget_default.setHidden(use_nomad_sample)
        self.pushButton_nomad_sample.setEnabled(use_nomad)

    # --------------------------------------------------
    # save / load methods
    # --------------------------------------------------

    def load_preferences(self):
        """Loads the preferences.

        Those may contain:
        - autosave: turn on / off autosave on closing the program.
        - dark_mode: turning dark-mode on / off.
        - number_format: the number format for display, can be either "mixed", "plain" or "scientific".
        - mixed_from: the exponent from where to switch to scientific format, if number_format is "mixed".
        - n_decimals: the number of displayed decimals of a number.
        - py_files_path: the path, where python files (e.g. protocols) are created.
        - meas_files_path: the path, where measurement data is stored.
        - device_driver_path: the path, where NOMAD CAMELS can find the installed devices.
        - databroker_catalog_name: the name of the databroker catalog

        Parameters
        ----------

        Returns
        -------

        """
        self.preferences = load_save_functions.get_preferences()
        self.update_preference_settings()

    def update_preference_settings(self):
        number_formatting.preferences = self.preferences
        variables_handling.preferences = self.preferences
        variables_handling.device_driver_path = self.preferences["device_driver_path"]
        variables_handling.meas_files_path = self.preferences["meas_files_path"]
        if "graphic_theme" in self.preferences:
            self.change_theme()
        self.change_catalog_name()
        logging_settings.update_log_settings()

    def change_theme(self):
        """ """
        theme = self.preferences["graphic_theme"]
        if "material_theme" in self.preferences:
            material_theme = self.preferences["material_theme"]
        else:
            material_theme = None
        dark = self.preferences["dark_mode"]
        theme_changing.change_theme(
            theme, material_theme=material_theme, dark_mode=dark
        )
        self.toggle_dark_mode()

    def toggle_dark_mode(self):
        """Turning dark mode on / off, called whenever the settings are
        changed. Using qdarkstyle to provide the stylesheets.

        Parameters
        ----------

        Returns
        -------

        """
        dark = self.preferences["dark_mode"]
        variables_handling.dark_mode = dark

    def change_catalog_name(self):
        """ """
        if not hasattr(self, "databroker_catalog") or not self.databroker_catalog:
            return
        # IMPORT databroker only if it is needed
        import databroker

        if "meas_files_path" in self.preferences:
            catalog_name = "CATALOG_NAME"
            if "databroker_catalog_name" in self.preferences:
                catalog_name = self.preferences["databroker_catalog_name"]
            # IMPORT make_catalog only if it is needed
            from nomad_camels.bluesky_handling import make_catalog

            make_catalog.make_yml(
                self.preferences["meas_files_path"], catalog_name, ask_restart=True
            )
            databroker.catalog.force_reload()
            try:
                self.databroker_catalog = databroker.catalog[catalog_name]
            except KeyError:
                # IMPORT warnings only if it is needed
                import warnings

                warnings.warn(
                    "Could not find databroker catalog, using temporary catalog. If data is not transferred, it might get lost."
                )
                self.databroker_catalog = databroker.temp()

    def change_preferences(self):
        """Called when any preferences are changed. Makes the dictionary
         of preferences and calls save_preferences from the
         load_save_functions module.

        Parameters
        ----------

        Returns
        -------

        """
        # IMPORT Settings_Window only if it is needed
        from nomad_camels.frontpanels.settings_window import Settings_Window

        settings_dialog = Settings_Window(parent=self, settings=self.preferences)
        if settings_dialog.exec():
            self.preferences.update(settings_dialog.get_settings())
            load_save_functions.save_preferences(self.preferences)
        self.update_preference_settings()

    def save_state(self, fromload=False, do_backup=True):
        """Saves the current states of both presets.

        Parameters
        ----------
        fromload :
             (Default value = False)

        do_backup :
            (Default value = True)

        Returns
        -------

        """
        if (
            "password_protection" in self.preferences
            and self.preferences["password_protection"]
        ):
            from PySide6.QtWidgets import QMessageBox

            msg_box = QMessageBox()
            msg_box.setText(
                "This version of NOMAD CAMELS is password protected.\nDo you want to save changes?"
            )
            msg_box.setWindowTitle("Save changes?")
            msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            if msg_box.exec() == QMessageBox.Cancel:
                return
            from nomad_camels.utility.password_widgets import Password_Dialog

            dialog = Password_Dialog(
                self, compare_hash=self.preferences["password_hash"]
            )
            if not dialog.exec():
                return
        self.make_save_dict()
        load_save_functions.autosave_preset(
            self._current_preset[0], self.__save_dict__, do_backup
        )
        if fromload:
            return
        self.save_user_data()
        self.save_sample_data()
        print("current state saved!")

    def new_preset(self):
        """Create a new, empty device-preset via a QFileDialog."""
        file = QFileDialog.getSaveFileName(
            self, "Save Preset", load_save_functions.preset_path, "*.preset"
        )[0]
        if not len(file):
            return
        preset_name = file.split("/")[-1][:-7]
        load_save_functions.save_preset(
            file,
            {
                "_current_preset": [preset_name],
                "active_instruments": {},
                "protocols_dict": OrderedDict(),
            },
        )
        self._current_preset[0] = preset_name

    def save_preset_as(self):
        """Opens a QFileDialog to save the device preset.
        A backup / autosave of the preset is made automatically.

        Parameters
        ----------

        Returns
        -------

        """
        file = QFileDialog.getSaveFileName(
            self, "Save Preset", load_save_functions.preset_path, "*.preset"
        )[0]
        if not len(file):
            return
        preset_name = file.split("/")[-1][:-7]
        self._current_preset[0] = preset_name
        self.make_save_dict()
        load_save_functions.save_preset(file, self.__save_dict__)

    def load_backup_preset(self):
        """Opens a QFileDialog in the Backup-folder of the presets.
        If a backup is selected, the current preset is put into backup.

        Parameters
        ----------

        Returns
        -------

        """
        file = QFileDialog.getOpenFileName(
            self, "Open Preset", load_save_functions.preset_path, "*.preset"
        )[0]
        if not file:
            return
        # preset_name = file.split('_')[-1][:-7]
        # preset = f'Backup/{file.split("/")[-2]}/{file.split("/")[-1][:-7]}'
        self.save_state()
        # self._current_preset[0] = preset_name
        self.load_preset(file)

    def load_state(self):
        """Loads the most recent presets."""
        preset = load_save_functions.get_most_recent_presets()
        if preset is not None:
            self.load_preset(preset)
        else:
            self.save_state(True)

    def change_preset(self, preset):
        """saves the old device preset,
        then changes to / loads the new preset.

        Parameters
        ----------
        preset :


        Returns
        -------

        """
        self.save_state()
        self._current_preset[0] = preset
        self.load_preset(preset)

    def load_preset(self, preset):
        """Called when loading a preset (e.g. when loading the last state).
        Opens the given preset.

        Parameters
        ----------
        preset :


        Returns
        -------

        """
        try:
            with open(
                os.path.join(load_save_functions.preset_path, f"{preset}.preset"),
                "r",
                encoding="utf-8",
            ) as f:
                preset_dict = json.load(f)
        except:
            with open(preset, "r", encoding="utf-8") as f:
                preset_dict = json.load(f)
        try:
            load_save_functions.load_save_dict(preset_dict, self.preset_save_dict)
        except Exception as e:
            text = f"Could not load preset {preset}.\nAn empty preset will be loaded instead.\nTo handle this error, you may want to install a missing driver or remove some settings from the preset.\n\nError Message:\n{e}"
            warn_popup.WarnPopup(self, text, "Load Error")
            load_save_functions.load_save_dict(
                {}, self.preset_save_dict, remove_extra_key=True
            )
            self._current_preset[0] = "empty_preset"
        self.update_channels()
        variables_handling.preset = self._current_preset[0]
        self.with_or_without_instruments()
        self.populate_meas_buttons()
        self.populate_manuals_buttons()
        self.adjustSize()

    def make_save_dict(self):
        """ """
        self.preset_save_dict = {
            "_current_preset": self._current_preset,
            "active_instruments": self.active_instruments,
            "protocols_dict": self.protocols_dict,
            "manual_controls": self.manual_controls,
        }
        for key in self.preset_save_dict:
            add_string = load_save_functions.get_save_str(self.preset_save_dict[key])
            if add_string is not None:
                self.__save_dict__.update(
                    {key: load_save_functions.get_save_str(self.preset_save_dict[key])}
                )

    def update_channels(self):
        """Called when the active devices change.
        The channels in variables_handling are updated with the ones
        provided by the active devices.

        Parameters
        ----------

        Returns
        -------

        """
        variables_handling.channels.clear()
        for key, dev in self.active_instruments.items():
            # for channel in dev.get_channels():
            variables_handling.channels.update(dev.get_channels())
            variables_handling.config_channels.update(dev.config_channels)

    # --------------------------------------------------
    # manual controls
    # --------------------------------------------------

    def manual_control_order_changed(self, order):
        """

        Parameters
        ----------
        order :


        Returns
        -------

        """
        self.manual_controls = OrderedDict(
            sorted(self.manual_controls.items(), key=lambda x: order.index(x[0]))
        )

    def add_manual_control(self):
        """ """
        # IMPORT New_Manual_Control_Dialog only if needed
        from nomad_camels.manual_controls.get_manual_controls import (
            New_Manual_Control_Dialog,
        )

        dialog = New_Manual_Control_Dialog(self)
        if dialog.exec():
            control_cls, options_cls = dialog.selected_control
            options = options_cls()
            if options.exec():
                self.add_manual_control_to_data(options.control_data)

    def add_manual_control_to_data(self, control_data):
        """

        Parameters
        ----------
        control_data :


        Returns
        -------

        """
        self.manual_controls[control_data["name"]] = control_data
        self.add_button_to_manuals(control_data["name"])
        self.button_area_manual.setHidden(False)

    def remove_manual_control(self, control_name):
        """

        Parameters
        ----------
        control_name :


        Returns
        -------

        """
        self.manual_controls.pop(control_name)
        self.button_area_manual.remove_button(control_name)
        if not self.manual_controls:
            self.button_area_manual.setHidden(True)

    def update_man_cont_data(self, control_data, old_name):
        """

        Parameters
        ----------
        control_data :

        old_name :


        Returns
        -------

        """
        self.manual_controls.pop(old_name)
        self.manual_controls[control_data["name"]] = control_data
        button = self.button_area_manual.rename_button(old_name, control_data["name"])
        self.add_functions_to_manual_button(button, control_data["name"])

    def open_manual_control_config(self, control_name):
        """

        Parameters
        ----------
        control_name :


        Returns
        -------

        """
        # IMPORT get_control_by_type_name only if needed
        from nomad_camels.manual_controls.get_manual_controls import (
            get_control_by_type_name,
        )

        control_data = self.manual_controls[control_name]
        config_cls = get_control_by_type_name(control_data["control_type"])[1]
        dialog = config_cls(parent=self, control_data=control_data)
        if dialog.exec():
            self.update_man_cont_data(dialog.control_data, control_name)

    def add_button_to_manuals(self, name):
        """

        Parameters
        ----------
        name :


        Returns
        -------

        """
        button = options_run_button.Options_Run_Button(
            name, small_text="Start", protocol_options=False
        )
        self.button_area_manual.add_button(button, name)
        self.add_functions_to_manual_button(button, name)

    def add_functions_to_manual_button(self, button, name):
        """

        Parameters
        ----------
        button :

        name :


        Returns
        -------

        """
        button.config_function = (
            lambda state=None, x=name: self.open_manual_control_config(x)
        )
        button.run_function = lambda state=None, x=name: self.start_manual_control(x)
        button.del_function = lambda x=name: self.remove_manual_control(x)
        button.update_functions()

    def populate_manuals_buttons(self):
        """ """
        self.button_area_manual.clear_area()
        if not self.manual_controls:
            self.button_area_manual.setHidden(True)
        else:
            self.button_area_manual.setHidden(False)
        for control in self.manual_controls:
            self.add_button_to_manuals(control)

    def start_manual_control(self, name):
        """

        Parameters
        ----------
        name :


        Returns
        -------

        """
        # IMPORT get_control_by_type_name only if needed
        from nomad_camels.manual_controls.get_manual_controls import (
            get_control_by_type_name,
        )

        control_data = self.manual_controls[name]
        control_type = control_data["control_type"]
        control_cls = get_control_by_type_name(control_type)[0]
        control = control_cls(control_data=control_data)
        self.open_windows.append(control)
        control.closing.connect(
            lambda x=control, y=name: self.close_manual_control(x, y)
        )
        self.button_area_manual.disable_single_run(name)

    def close_manual_control(self, control, name):
        """

        Parameters
        ----------
        control :

        name :


        Returns
        -------

        """
        self.open_windows.remove(control)
        self.button_area_manual.enable_single_run(name)

    # --------------------------------------------------
    # protocols
    # --------------------------------------------------
    def protocol_order_changed(self, order):
        """

        Parameters
        ----------
        order :


        Returns
        -------

        """
        self.protocols_dict = OrderedDict(
            sorted(self.protocols_dict.items(), key=lambda x: order.index(x[0]))
        )

    def add_measurement_protocol(self):
        """ """
        # IMPORT Protocol_Config only if needed
        from nomad_camels.frontpanels.protocol_config import Protocol_Config

        dialog = Protocol_Config()
        dialog.show()
        dialog.accepted.connect(self.add_prot_to_data)
        self.add_to_open_windows(dialog)

    def import_measurement_protocol(self):
        # IMPORT Protocol_Config and Path_Button_Dialog only if needed
        from nomad_camels.frontpanels.protocol_config import Protocol_Config
        from nomad_camels.ui_widgets.path_button_edit import Path_Button_Dialog

        dialog = Path_Button_Dialog(
            self,
            default_dir=self.preferences["py_files_path"],
            file_extension="*.cprot",
            title="Choose Protocol - NOMAD CAMELS",
            text="select the protocol you want to import",
        )
        if not dialog.exec():
            return
        prot_path = dialog.path
        prot = load_save_functions.load_protocol(prot_path)
        dialog = Protocol_Config(prot)
        dialog.show()
        dialog.accepted.connect(self.add_prot_to_data)
        self.add_to_open_windows(dialog)

    def add_prot_to_data(self, protocol):
        """

        Parameters
        ----------
        protocol :


        Returns
        -------

        """
        self.protocols_dict[protocol.name] = protocol
        self.add_button_to_meas(protocol.name)
        self.button_area_meas.setHidden(False)

    def remove_protocol(self, prot_name):
        """

        Parameters
        ----------
        prot_name :


        Returns
        -------

        """
        self.protocols_dict.pop(prot_name)
        self.button_area_meas.remove_button(prot_name)
        if not self.protocols_dict:
            self.button_area_meas.setHidden(True)

    def update_prot_data(self, protocol, old_name):
        """

        Parameters
        ----------
        protocol :

        old_name :


        Returns
        -------

        """
        self.protocols_dict.pop(old_name)
        self.protocols_dict[protocol.name] = protocol
        button = self.button_area_meas.rename_button(old_name, protocol.name)
        self.add_functions_to_meas_button(button, protocol.name)

    def open_protocol_config(self, prot_name):
        """

        Parameters
        ----------
        prot_name :


        Returns
        -------

        """
        # IMPORT Protocol_Config only if needed
        if not self.check_password_protection():
            return
        from nomad_camels.frontpanels.protocol_config import Protocol_Config

        dialog = Protocol_Config(self.protocols_dict[prot_name])
        dialog.show()
        dialog.accepted.connect(lambda x, y=prot_name: self.update_prot_data(x, y))
        self.add_to_open_windows(dialog)

    def add_button_to_meas(self, name):
        """

        Parameters
        ----------
        name :


        Returns
        -------

        """
        button = options_run_button.Options_Run_Button(name)
        self.button_area_meas.add_button(button, name)
        self.add_functions_to_meas_button(button, name)

    def add_functions_to_meas_button(self, button, name):
        """

        Parameters
        ----------
        button :

        name :


        Returns
        -------

        """
        button.config_function = lambda state=None, x=name: self.open_protocol_config(x)
        button.run_function = lambda state=None, x=name: self.run_protocol(x)
        button.build_function = lambda x=name: self.build_protocol(x)
        button.external_function = lambda x=name: self.open_protocol(x)
        button.data_path_function = lambda x=name: self.open_data_path(x)
        button.del_function = lambda x=name: self.remove_protocol(x)
        button.update_functions()

    def open_data_path(self, protocol_name):
        user = self.get_user_name_data()[0]
        sample = self.get_sample_name_data()[0]
        protocol = self.protocols_dict[protocol_name]
        savepath = f'{self.preferences["meas_files_path"]}/{user}/{sample}/{protocol.filename or "data"}.h5'
        savepath = os.path.normpath(savepath)
        while not os.path.exists(savepath):
            savepath = os.path.dirname(savepath)
        import platform, subprocess

        if platform.system() == "Windows":
            # /select, specifies that the file should be highlighted
            subprocess.Popen(f'explorer /select,"{savepath}"')
        elif platform.system() == "Darwin":
            # -R, specifies that the file should be revealed in finder
            subprocess.Popen(["open", "-R", savepath])
        else:
            # Linux doesn't support highlighting a specific file in the file explorer
            subprocess.Popen(["xdg-open", os.path.dirname(savepath)])

    def populate_meas_buttons(self):
        """ """
        self.button_area_meas.clear_area()
        if not self.protocols_dict:
            self.button_area_meas.setHidden(True)
        else:
            self.button_area_meas.setHidden(False)
        for prot in self.protocols_dict:
            self.add_button_to_meas(prot)

    def run_protocol(self, protocol_name):
        """
        This function runs the given protocol `protocol_name`.
        First the protocol is built, then imported. The used instruments are
        instantiated with `device_handling.instantiate_devices` and functions
        from the protocol like creating plots are called.

        If everything runs correctly and a nomad upload should be done, after
        `protocol_finished` is called, this function will wait for it and then
        handle the upload.
        """
        self.setCursor(Qt.WaitCursor)
        # IMPORT importlib, bluesky, ophyd and time only if needed
        import importlib

        if not self.run_engine:
            self.bluesky_setup()
        self.still_running = True
        # IMPORT device_handling only if needed
        from nomad_camels.utility import device_handling

        if "autosave_run" in self.preferences and self.preferences["autosave_run"]:
            self.save_state(do_backup=self.preferences["backup_before_run"])
        self.button_area_meas.disable_run_buttons()
        try:
            self.build_protocol(protocol_name, ask_file=False)
            protocol = self.protocols_dict[protocol_name]
            path = f"{self.preferences['py_files_path']}/{protocol.name}.py"
            name = os.path.basename(path)[:-3]
            spec = importlib.util.spec_from_file_location(name, path)
            self.protocol_module = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = self.protocol_module
            spec.loader.exec_module(self.protocol_module)
            self.protocol_module.protocol_step_information[
                "protocol_stepper_signal"
            ] = self.protocol_stepper_signal
            plots, subs, _ = self.protocol_module.create_plots(self.run_engine)
            for plot in plots:
                self.add_to_plots(plot)
            device_list = protocol.get_used_devices()
            self.current_protocol_device_list = list(device_list)
            self.re_subs += subs
            self.instantiate_devices_thread = device_handling.InstantiateDevicesThread(
                device_list, skip_config=protocol.skip_config
            )
            self.instantiate_devices_thread.finished.connect(self.run_protocol_part2)
            self.instantiate_devices_thread.exception_raised.connect(
                self.propagate_exception
            )
            self.instantiate_devices_thread.start()
        except Exception as e:
            self.protocol_finished()
            if isinstance(e, IndentationError):
                text = "The protocol did not compile correctly, please check whether there are for example any if-statements or loops that do not have children-steps."
                raise Exception(text).with_traceback(e.__traceback__)
            raise e

    def propagate_exception(self, exception):
        self.protocol_finished()
        raise exception

    def run_protocol_part2(self):
        try:
            devs = self.instantiate_devices_thread.devices
            dev_data = self.instantiate_devices_thread.device_config
            additionals = self.protocol_module.steps_add_main(self.run_engine, devs)
            self.add_subs_and_plots_from_dict(additionals)
        except Exception as e:
            self.protocol_finished()
            raise e
        import bluesky, ophyd, time

        self.pushButton_resume.setEnabled(False)
        self.pushButton_pause.setEnabled(True)
        self.pushButton_stop.setEnabled(True)
        protocol = self.running_protocol
        self.protocol_module.run_protocol_main(
            self.run_engine,
            catalog=self.databroker_catalog,
            devices=devs,
            md={
                "devices": dev_data,
                "description": protocol.description,
                "versions": {
                    "NOMAD CAMELS": "0.1",
                    "EPICS": "7.0.6.2",
                    "bluesky": bluesky.__version__,
                    "ophyd": ophyd.__version__,
                },
            },
        )
        self.pushButton_resume.setEnabled(False)
        self.pushButton_pause.setEnabled(False)
        self.pushButton_stop.setEnabled(False)
        self.protocol_stepper_signal.emit(100)
        nomad = self.nomad_user is not None
        self.run_done_file_signal.emit(self.protocol_savepath)
        if not nomad:
            return
        while self.still_running:
            time.sleep(0.1)
        if self.nomad_sample:
            if "name" in self.nomad_sample:
                name = f"/{self.nomad_sample['name']}"
            elif "Name" in self.nomad_sample:
                name = f"/{self.nomad_sample['Name']}"
            else:
                name = ""
        else:
            name = f"/{self.active_sample}"
        if self.comboBox_upload_type.currentText() == "auto upload":
            # IMPORT nomad_communication only if needed
            from nomad_camels.nomad_integration import nomad_communication

            upload = self.comboBox_upload_choice.currentText()
            nomad_communication.upload_file(
                self.protocol_savepath, upload, f"CAMELS_data{name}", parent=self
            )
        elif self.comboBox_upload_type.currentText() == "ask after run":
            # IMPORT file_uploading only if needed
            from nomad_camels.nomad_integration import file_uploading

            dialog = file_uploading.UploadDialog(
                self, self.protocol_savepath, f"CAMELS_data{name}"
            )

    def add_subs_and_plots_from_dict(self, dictionary):
        """

        Parameters
        ----------
        dictionary :


        Returns
        -------

        """
        for k, v in dictionary.items():
            if k == "subs":
                self.re_subs += v
            elif k == "plots":
                for plot in v:
                    self.add_to_plots(plot)
            elif isinstance(v, dict):
                self.add_subs_and_plots_from_dict(v)

    def pause_protocol(self):
        """ """
        if self.run_engine.state == "running":
            self.run_engine.request_pause()
            self.pushButton_resume.setEnabled(True)
            self.pushButton_pause.setEnabled(False)

    def stop_protocol(self):
        """ """
        if self.run_engine.state != "idle":
            self.run_engine.abort("Aborted by user")
        # self.protocol_finished()

    def resume_protocol(self):
        """ """
        if self.run_engine.state == "paused":
            self.pushButton_resume.setEnabled(False)
            self.pushButton_pause.setEnabled(True)
            self.run_engine.resume()

    def protocol_finished(self, *args):
        """

        Parameters
        ----------
        *args :


        Returns
        -------

        """
        # IMPORT databroker_export and device_handling only if needed
        from nomad_camels.utility import databroker_export, device_handling

        if (
            self.protocol_module
            and hasattr(self.protocol_module, "uids")
            and self.protocol_module.uids
        ):
            runs = self.databroker_catalog[tuple(self.protocol_module.uids)]
            databroker_export.broker_to_NX(
                runs,
                self.protocol_savepath,
                self.protocol_module.plots,
                session_name=self.running_protocol.session_name,
                export_to_csv=self.running_protocol.export_csv,
                export_to_json=self.running_protocol.export_json,
                new_file_each_run=self.preferences["new_file_each_run"],
            )
        for sub in self.re_subs:
            self.run_engine.unsubscribe(sub)
        device_handling.close_devices(self.current_protocol_device_list)
        self.current_protocol_device_list = []
        self.pushButton_stop.setEnabled(False)
        self.pushButton_pause.setEnabled(False)
        self.pushButton_resume.setEnabled(False)
        self.button_area_meas.enable_run_buttons()
        self.protocol_stepper_signal.emit(100)
        self.setCursor(Qt.ArrowCursor)
        if "number_databroker_files" in variables_handling.preferences:
            n_files = variables_handling.preferences["number_databroker_files"]
            if n_files > 0:
                name = self.preferences["databroker_catalog_name"]
                meas_dir = self.preferences["meas_files_path"]
                catalog_dir = f"{meas_dir}/databroker/{name}"
                if os.path.isdir(catalog_dir):
                    files = os.listdir(catalog_dir)
                    if len(files) > n_files:
                        files.sort(key=lambda x: os.path.getmtime(f"{catalog_dir}/{x}"))
                        for file in files[:-n_files]:
                            os.remove(f"{catalog_dir}/{file}")
        self.still_running = False

    def build_protocol(self, protocol_name, ask_file=True):
        """Calls the build_protocol from nomad_camels.bluesky_handling.protocol_builder
        for the selected protocol and provides it with a savepath and
        user- and sample-data.

        Parameters
        ----------
        protocol_name :

        ask_file :
             (Default value = True)

        Returns
        -------

        """
        self.progressBar_protocols.setValue(0)
        protocol = self.protocols_dict[protocol_name]
        protocol.session_name = self.lineEdit_session.text()
        if re.search(r"[^\w\s]", protocol.session_name):
                    raise ValueError(
                        "Session name contains special characters.\nPlease use only letters, numbers and whitespace."
                    )

        self.running_protocol = protocol
        if ask_file:
            path = QFileDialog.getSaveFileName(
                self, "Export Protocol", protocol_name, "*.py"
            )[0]
            if not path:
                return
        else:
            path = f"{self.preferences['py_files_path']}/{protocol_name}.py"
        user, userdata = self.get_user_name_data()
        sample, sampledata = self.get_sample_name_data()
        savepath = f'{self.preferences["meas_files_path"]}/{user}/{sample}/{protocol.filename or "data"}.h5'
        self.protocol_savepath = savepath
        # IMPORT protocol_builder only if needed
        from nomad_camels.bluesky_handling import protocol_builder

        protocol_builder.build_protocol(
            protocol, path, savepath, userdata=userdata, sampledata=sampledata
        )
        print("\n\nBuild successful!\n")
        self.progressBar_protocols.setValue(100 if ask_file else 1)

    def get_user_name_data(self):
        if self.nomad_user:
            userdata = self.nomad_user
            user = userdata["name"]
        elif self.extension_user:
            userdata = self.extension_user
        else:
            user = self.active_user or "default_user"
            userdata = (
                {"name": "default_user"}
                if user == "default_user"
                else self.userdata[user]
            )
        return user, userdata

    def get_sample_name_data(self):
        if self.nomad_sample and self.checkBox_use_nomad_sample.isChecked():
            sampledata = self.nomad_sample
            if "name" in sampledata:
                sample = sampledata["name"]
            elif "Name" in sampledata:
                sample = sampledata["Name"]
            else:
                sample = "NOMAD-Sample"
        elif self.extension_sample:
            sampledata = self.extension_sample
            sample = sampledata["name"]
        else:
            sample = self.comboBox_sample.currentText() or "default_sample"
            sampledata = (
                {"name": "default_sample"}
                if sample == "default_sample"
                else self.sampledata[sample]
            )
        return sample, sampledata

    def open_protocol(self, protocol_name):
        """

        Parameters
        ----------
        protocol_name :


        Returns
        -------

        """
        path = f"{self.preferences['py_files_path']}/{protocol_name}.py"
        if not os.path.isfile(path):
            self.build_protocol(protocol_name, False)
        os.startfile(path)

    # --------------------------------------------------
    # tools
    # --------------------------------------------------
    def launch_device_builder(self):
        """ """
        # IMPORT device_driver_builder only if needed
        from nomad_camels.tools import device_driver_builder

        device_builder = device_driver_builder.Driver_Builder(self)
        device_builder.show()

    def launch_epics_builder(self):
        # IMPORT EPICS_driver_builder only if needed
        from nomad_camels.tools import EPICS_driver_builder

        device_builder = EPICS_driver_builder.EPICS_Driver_Builder(self)
        device_builder.show()

    def launch_data_exporter(self):
        # IMPORT databroker_exporter only if needed
        from nomad_camels.tools import databroker_exporter

        exporter = databroker_exporter.Datbroker_Exporter(self)
        exporter.show()

    def launch_hdf5_exporter(self):
        from nomad_camels.utility import databroker_export

        exporter = databroker_export.ExportH5_dialog(self)
        exporter.exec()
