from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QLabel, QComboBox
from PyQt5.QtCore import Qt
from main_classes.loop_step import Loop_Step, Loop_Step_Config

from gui.read_channels import Ui_read_channels_config

from utility import variables_handling, fit_variable_renaming


class Read_Channels(Loop_Step):
    """This step represents the bluesky plan stub `trigger_and_read`.

    Attributes
    ----------
    read_all : bool
        whether to simply read all available channels
    channel_dict : dict
        the dictionary of all channels and whether to read them. It also
        provides "use set" for using the set-value without reading, but
        that is not supported. The shape should look like:
        {channel: {'read': True, 'use set': False}}
    """
    def __init__(self, name='', parent_step=None, step_info=None, **kwargs):
        super().__init__(name, parent_step, step_info, **kwargs)
        self.step_type = 'Read Channels'
        if step_info is None:
            step_info = {}
        self.read_all = step_info['read_all'] if 'read_all' in step_info else False
        self.split_trigger = step_info['split_trigger'] if 'split_trigger' in step_info else False
        # self.plot_data = step_info['plot_data'] if 'plot_data' in step_info else True
        # self.save_data = step_info['save_data'] if 'save_data' in step_info else True
        # self.use_set_val = step_info['use_set_val'] if 'use_set_val' in step_info else False
        # if 'channel_dict' in step_info:
        #     self.channel_dict = step_info['channel_dict']
        # else:
        #     self.channel_dict = {}
        if 'channel_list' in step_info:
            self.channel_list = step_info['channel_list']
        else:
            self.channel_list = []
        # for channel in variables_handling.channels:
        #     if channel not in self.channel_dict:
        #         self.channel_dict.update({channel: {'read': False,
        #                                         'use set': False}})
        self.update_used_devices()

    def update_used_devices(self):
        """All devices that should be read are added to the used_devices."""
        self.used_devices = []
        for channel in variables_handling.channels:
            if self.read_all or channel in self.channel_list:
                device = variables_handling.channels[channel].device
                if device not in self.used_devices:
                    self.used_devices.append(device)
        # for channel_name in self.channel_list:
        #     if (self.read_all or channel_info['read']) and channel_name in variables_handling.channels:
        #         device = variables_handling.channels[channel_name].device
        #         if device not in self.used_devices:
        #             self.used_devices.append(device)

    def get_channels_string(self, tabs):
        channel_string = f'{tabs}channels_{self.variable_name()} = ['
        if not self.read_all and not self.channel_list:
            raise Exception(f'Trying to read no channel in {self.full_name}!')
        if self.read_all:
            for channel in variables_handling.channels:
                channel_string += get_channel_string(channel)
        else:
            for channel in self.channel_list:
                channel_string += get_channel_string(channel)
        channel_string = channel_string[:-2] + ']\n'
        return channel_string

    def variable_name(self):
        return fit_variable_renaming.replace_name(self.name)

    def get_protocol_string(self, n_tabs=1):
        """In the protocol, at first a list `channels` is defined,
        including all the channels, that are selected to be read. Then
        bps.trigger_and_read is called on these channels."""
        tabs = '\t' * n_tabs
        protocol_string = super().get_protocol_string(n_tabs)
        if self.split_trigger:
            protocol_string += f'{tabs}yield from helper_functions.read_wo_trigger(channels_{self.variable_name()}, grp_{self.variable_name()}, stream=stream_name)\n'
        else:
            protocol_string += self.get_channels_string(tabs)
            protocol_string += f'{tabs}yield from bps.trigger_and_read(channels_{self.variable_name()}, name=stream_name)\n'
        return protocol_string

    def get_protocol_short_string(self, n_tabs=0):
        short_string = super().get_protocol_short_string(n_tabs)
        short_string = f'{short_string[:-1]} - {self.channel_list}\n'
        return short_string

def get_channel_string(channel):
    name = variables_handling.channels[channel].name
    if '.' in name:
        dev, chan = name.split('.')
        return f'devs["{dev}"].{chan}, '
    else:
        return f'devs["{name}"], '



class Read_Channels_Config(Loop_Step_Config):
    def __init__(self, loop_step:Read_Channels, parent=None):
        super().__init__(parent, loop_step)
        self.sub_widget = Read_Channels_Config_Sub(loop_step, self)
        self.layout().addWidget(self.sub_widget, 1, 0, 1, 5)

    def update_step_config(self):
        self.sub_widget.update_step_config()

class Read_Channels_Config_Sub(QWidget, Ui_read_channels_config):
    """Config for the Read_Channels it provides a table of channels with
    a checkbox, whether to read them. Also there is a checkbox whether
    to simply read all available channels."""
    def __init__(self, loop_step:Read_Channels, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.loop_step = loop_step
        self.checkBox_read_all.stateChanged.connect(self.read_type_changed)
        self.checkBox_split_trigger.clicked.connect(self.use_trigger)
        # self.comboBox_readType.addItems(['read all', 'read selected'])
        # self.comboBox_readType.currentTextChanged.connect(self.read_type_changed)
        self.load_data()
        self.read_type_changed()
        self.tableWidget_channels.setHorizontalHeaderLabels(['read',
                                                             'channel name',
                                                             'use set-value'])
        self.build_channels_table()
        self.lineEdit_search.textChanged.connect(self.build_channels_table)
        # self.checkBox_use_set.toggled.connect(self.checkbox_toggle)
        # self.checkBox_plot.toggled.connect(self.checkbox_toggle)
        # self.checkBox_save.toggled.connect(self.checkbox_toggle)
        self.tableWidget_channels.clicked.connect(self.table_check_changed)

    def use_trigger(self):
        self.loop_step.split_trigger = self.checkBox_split_trigger.isChecked()

    def checkbox_toggle(self):
        """When a checkbox is (un-)checked, the new value is stored
        inside the loop_step."""
        self.loop_step.use_set_val = self.checkBox_use_set.isChecked()
        self.loop_step.save_data = self.checkBox_save.isChecked()
        self.loop_step.plot_data = self.checkBox_plot.isChecked()

    def read_type_changed(self):
        """If the read-all checkbox is checked, disables the table, if
        not, enables it."""
        read_all = self.checkBox_read_all.isChecked()
        if read_all:
            self.tableWidget_channels.setEnabled(False)
            # self.checkBox_use_set.setEnabled(True)
        else:
            self.tableWidget_channels.setEnabled(True)
            # self.checkBox_use_set.setEnabled(False)
        self.loop_step.read_all = read_all
        self.loop_step.update_used_devices()

    def load_data(self):
        """Putting the data from the loop_step into the widgets."""
        self.checkBox_read_all.setChecked(self.loop_step.read_all)
        self.checkBox_split_trigger.setChecked(self.loop_step.split_trigger)
        # self.checkBox_save.setChecked(self.loop_step.save_data)
        # self.checkBox_plot.setChecked(self.loop_step.plot_data)
        # self.checkBox_use_set.setChecked(self.loop_step.use_set_val)
        self.build_channels_table()

    def update_step_config(self):
        self.lineEdit_search.clear()
        self.build_channels_table()
        self.loop_step.channel_list = []
        for i in range(self.tableWidget_channels.rowCount()):
            if self.tableWidget_channels.item(i, 0).checkState() > 0:
                name = self.tableWidget_channels.item(i, 1).text()
                self.loop_step.channel_list.append(name)

    def table_check_changed(self, pos):
        """If a checkbox inside the table is clicked, the value is
        stored into the loopstep."""
        r = pos.row()
        c = pos.column()
        if c == 0:
            name = self.tableWidget_channels.item(r, 1).text()
            if self.tableWidget_channels.item(r, c).checkState() > 0:
                self.loop_step.channel_list.append(name)
                self.loop_step.channel_list = list(set(self.loop_step.channel_list))
            elif name in self.loop_step.channel_list:
                self.loop_step.channel_list.remove(name)
            self.loop_step.update_used_devices()
        #     self.loop_step.channel_dict[name]['read'] =
        #     self.loop_step.update_used_devices()
        # if c == 2 and variables_handling.channels[name].output:
        #     self.loop_step.channel_dict[name]['use set'] = self.tableWidget_channels.item(r, c).checkState() > 0


    def build_channels_table(self):
        """This creates the table for all channels."""
        self.tableWidget_channels.clear()
        self.tableWidget_channels.setColumnCount(2)
        # self.tableWidget_channels.setRowCount(len(variables_handling.channels))
        self.tableWidget_channels.setRowCount(0)
        self.tableWidget_channels.setHorizontalHeaderLabels(['read', 'channel name'])
        searchtext = self.lineEdit_search.text()
        n = 0
        for i, channel in enumerate(sorted(variables_handling.channels, key=lambda x: x.lower())):
            if searchtext not in channel:
                continue
            self.tableWidget_channels.setRowCount(n+1)
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            if channel in self.loop_step.channel_list:
                item.setCheckState(2)
            else:
                item.setCheckState(False)
            self.tableWidget_channels.setItem(n, 0, item)
            item = QTableWidgetItem(channel)
            item.setFlags(item.flags() ^ Qt.ItemIsEditable)
            self.tableWidget_channels.setItem(n, 1, item)
            n += 1
            # if variables_handling.channels[channel].output:
            #     item = QTableWidgetItem()
            #     item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            #     if channel in self.loop_step.channel_dict:
            #         item.setCheckState(2 if self.loop_step.channel_dict[channel]['use set'] else False)
            #     else:
            #         item.setCheckState(False)
            # else:
            #     item = QTableWidgetItem()
            #     item.setFlags(item.flags() ^ Qt.ItemIsEditable)
            # self.tableWidget_channels.setItem(i, 2, item)
        self.tableWidget_channels.resizeColumnsToContents()
        # for channel in self.loop_step.channel_dict:
        #     if channel not in variables_handling.channels:
        #         self.loop_step.channel_dict.pop(channel)


class Trigger_Channels_Step(Loop_Step):

    def __init__(self, name='', parent_step=None, step_info=None, **kwargs):
        super().__init__(name, parent_step, step_info, **kwargs)
        self.step_type = 'Trigger Channels'
        if step_info is None:
            step_info = {}
        self.read_step = step_info['read_step'] if 'read_step' in step_info else ''

    def get_protocol_string(self, n_tabs=1):
        """In the protocol, at first a list `channels` is defined,
        including all the channels, that are selected to be read. Then
        bps.trigger_and_read is called on these channels."""
        tabs = '\t' * n_tabs
        protocol_string = super().get_protocol_string(n_tabs)
        read_step = variables_handling.current_protocol.loop_step_dict[self.read_step]
        protocol_string += read_step.get_channels_string(tabs)
        step_name = read_step.variable_name()
        protocol_string += f'{tabs}grp_{step_name} = bps._short_uid("trigger")\n'
        protocol_string += f'{tabs}yield from helper_functions.trigger_multi(channels_{step_name}, grp_{step_name})\n'
        return protocol_string

    def get_protocol_short_string(self, n_tabs=0):
        short_string = super().get_protocol_short_string(n_tabs)
        read_step = variables_handling.current_protocol.loop_step_dict[self.read_step]
        short_string = f'{short_string[:-1]} - {read_step.channel_list}\n'
        return short_string


class Trigger_Channels_Config(Loop_Step_Config):
    def __init__(self, loop_step:Trigger_Channels_Step, parent=None):
        super().__init__(parent, loop_step)
        label = QLabel('Corresponding Read-Step:')
        self.comboBox_read_step = QComboBox()
        self.layout().addWidget(label, 1, 0)
        self.layout().addWidget(self.comboBox_read_step, 1, 1, 1, 4)
        triggerable = []
        for name, step in variables_handling.current_protocol.loop_step_dict.items():
            if step.step_type == 'Read Channels' and step.split_trigger:
                triggerable.append(name)
        self.comboBox_read_step.addItems(triggerable)

    def update_step_config(self):
        self.loop_step.read_step = self.comboBox_read_step.currentText()
        super().update_step_config()
