'''
Created on Nov 7, 2019

@author: samerd
'''
import pycalc
from pycalc.menu import Menu, MenuItemHandler


class Converter(MenuItemHandler):
    """
    Coverter menu handler.
    handles 'Convert' user menu

    @cvar FMT_TO_BASE_MAP: maps for each format its integer base.
    @cvar FORMATTER_MAPPING: maps for each format the converter function.
    """

    FMT_TO_BASE_MAP = dict(
        b=2,
        o=8,
        d=10,
        h=16)

    FORMATTER_MAPPING = dict(
        b=pycalc.to_bin,
        o=pycalc.to_oct,
        d=pycalc.to_decimal,
        h=pycalc.to_hex)

    def __init__(self):
        """
        initialize the menu that will be used to select the input or output
        format
        """

        self._menu = Menu()
        self._menu.add_menu_item('b', 'Binary', None)
        self._menu.add_menu_item('o', 'Octal', None)
        self._menu.add_menu_item('d', 'Decimal', None)
        self._menu.add_menu_item('h', 'Hexadecimal', None)

    def str_to_int(self, int_fmt, num_str):
        """
        Converts a string to integer based on the given format
        """
        try:
            num = int(num_str, self.FMT_TO_BASE_MAP[int_fmt])
        except ValueError:
            print("Invalid number %s of type %s" % (num_str, int_fmt))
            num = None
        return num

    def on_select(self):
        """
        called when the user selects 'Convert' menu item.
        it asks the user to enter:
        1- input format
        2- output format
        3- the number to be converted
        then it prints the converted number.
        """
        # read input format
        print("Please enter input format:")
        input_format = self._menu.display()
        if not input_format:
            print("Invalid format!")
            return
        # read output format
        print("Please enter output format:")
        output_format = self._menu.display()
        if not output_format:
            print("Invalid format!")
            return
        # read the number to be converted
        num_str = input("Please enter number to convert: ")
        print("Converting %s from %s to %s" % (
            num_str, input_format.description, output_format.description))
        num = self.str_to_int(input_format.key, num_str)

        # find the formatter and convert the number
        formatter = self.FORMATTER_MAPPING.get(output_format.key)
        if not formatter:
            print("Unsupported format!")
            return
        print("Result: %s" % formatter(num))
