'''
Created on Nov 7, 2019

@author: samerd
'''
import os
import sys

# add src dir to PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

# pylint: disable=wrong-import-position
from pycalc.calculator import Calculator  # noqa
from pycalc.converter import Converter  # noqa
from pycalc.menu import Menu, MenuItemHandler  # noqa


class QuitHandler(MenuItemHandler):
    """
    This class used for terminating the application gracefully.
    menu items using this handler will exit the application.
    """

    def on_select(self):
        """
        exit the application gracefully
        """
        print("Exiting...")
        sys.exit(0)


class CalcApp():
    """
    Main application class
    @ivar _menu: main menu of the application
    """

    def __init__(self):
        """
        Initialize the menu and add required menu items
        """
        self._menu = Menu()
        self._menu.add_menu_item("1", "Calculate", Calculator())
        self._menu.add_menu_item("2", "Convert", Converter())
        self._menu.add_menu_item("q", "Quit", QuitHandler())

    def main_menu(self):
        """
        Application loop.
        will continue till the user selects 'Quit'
        """
        while True:
            selected_item = self._menu.display()
            if selected_item:
                selected_item.handle()
            print()


if __name__ == '__main__':
    # create the main application object
    app = CalcApp()
    # display the main menu
    app.main_menu()
