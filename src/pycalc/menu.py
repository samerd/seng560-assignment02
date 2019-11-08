'''
Created on Nov 7, 2019

@author: samerd
'''
from collections import OrderedDict


class MenuItemHandler():
    """
    class MenuItemHandler: is an interface for implementing a menu handler
    """

    def on_select(self):
        """
        on_select function will be invoked when the handler is selected
        called by MenuItem.handle function
        """
        raise NotImplementedError(
            "%s.%s is not implemented" % (self.__class__.__name__,
                                          self.on_select.__name__))


class MenuItem():
    """
    class MenuItem: represent a menu item.
    @ivar _key: key used to select the menu item
    @ivar _description: Menu Item description
    @ivar _handler: handler that can be called when the item is selected
    """

    def __init__(self, key, description, handler):
        self._key = key
        self._description = description
        self._handler = handler

    @property
    def key(self):
        return self._key

    @property
    def description(self):
        return self._description

    def display(self):
        """
        prints the menu item on screen
        """
        print("%s: %s" % (self._key, self._description))

    def handle(self):
        """
        should be called when the menu item is selected
        """
        self._handler.on_select()


class Menu():
    """
    supports menu functionality.
    menu displays menu items and prompts the user for a choice.
    @ivar _menu_items: an ordered map of MenuItem objects
    """

    def __init__(self):
        self._menu_items = OrderedDict()

    def add_menu_item(self, key, description, handler):
        """
        creates a menu item and add it to the list of menu items
        """
        menu_item = MenuItem(key, description, handler)
        self._menu_items[key] = menu_item

    def display(self):
        """
        displays the menu items and prompts the user for selection.
        @return: the selected menu item
        """
        for menu_item in self._menu_items.values():
            menu_item.display()
        choice = input("Choice: ")
        choice = choice.strip()
        selected_item = self._menu_items.get(choice)
        if not selected_item:
            print("Invalid choice '%s'" % choice)
        return selected_item
