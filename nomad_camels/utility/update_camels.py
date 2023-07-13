"""A module used to update CAMELS. The import of nomad_camels is necessary,
since otherwise it would not show in the imported distributions for reading its
current version."""

import os
import sys
import subprocess
from importlib.metadata import distributions
import nomad_camels  # has to be imported for the distribution version number!
import requests
from nomad_camels.ui_widgets import warn_popup

from PySide6.QtWidgets import QMessageBox


def get_version():
    """Goes through all imported distributions and returns the version of
    nomad-camels"""
    for d in distributions():
        if d.metadata['Name'] == 'nomad-camels':
            return d.version
    return None

def update_camels():
    """Calls a subprocess that updates CAMELS via pip."""
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                           '--no-cache-dir', 'nomad-camels', '--upgrade',])

def question_message_box(parent=None):
    """
    Retrieves the currently installed version and the available version of
    nomad-camels. If the are the same, a message is displayed, and function
    exits. Otherwise, a question-box appears, whether the user wants to install
    the newer version of CAMELS. If yes, first `update_camels` and then
    `restart_camels` are called.

    Parameters
    ----------
    parent : QWidget
        (Default value = None)
        The parent widget to be used for the message boxes.
    """
    installed_version = get_version()
    url = f'https://raw.githubusercontent.com/FAU-LAP/NOMAD-CAMELS/development/nomad_camels_version.txt'
    available_version = requests.get(url).text
    if installed_version == available_version:
        warn_popup.WarnPopup(parent,
                             'Your version of NOMAD-CAMELS is already up to date',
                             'Already up to date', info_icon=True)
        return
    update_dialog = QMessageBox.question(parent, 'Update NOMAD-CAMELS',
                                         f'Your current version of NOMAD-CAMELS is {installed_version}\n'
                                         f'The newest available version is {available_version}\n'
                                         f'Do you want to update now? (NOMAD-CAMELS will have to restart)',
                                         QMessageBox.Yes | QMessageBox.No)
    if update_dialog != QMessageBox.Yes:
        return
    update_camels()
    restart_camels(parent)

def restart_camels(parent=None, ask_restart=True):
    """Restarts CAMELS. If `ask_restart`, a question-messagebox appears first,
    to make sure the user actually wants to restart.

    Parameters
    ----------
    parent : QWidget
        (Default value = None)
        The parent widget to be used for the message boxes.
    ask_restart : bool
        (Default value = True)
        If True, the user is asked whether to restart CAMELS.
    """
    if ask_restart:
        restart_dialog = QMessageBox.question(parent, 'Restart NOMAD-CAMELS now?',
                                              'Do you want to restart NOMAD-CAMELS now?',
                                              QMessageBox.Yes | QMessageBox.No)
        if restart_dialog != QMessageBox.Yes:
            return
    os.execl(sys.executable, sys.executable, *sys.argv)

def check_up_to_date():
    """Gets the installed and available version of CAMELS and checks whether
    they are the same. Returns the outcome as a bool."""
    installed_version = get_version()
    url = f'https://raw.githubusercontent.com/FAU-LAP/NOMAD-CAMELS/development/nomad_camels_version.txt'
    available_version = requests.get(url).text
    return installed_version == available_version

def auto_update(parent):
    """
    Called if auto-update is set in the preferences. If the currently installed
    version is not up to date, `question_message_box` is called.

    Parameters
    ----------
    parent : QWidget
        (Default value = None)
        The parent widget to be used for the message boxes.
    """
    if not check_up_to_date():
        question_message_box(parent)


if __name__ == '__main__':
    update_camels()
