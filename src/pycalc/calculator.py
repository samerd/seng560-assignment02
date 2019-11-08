'''
Created on Nov 7, 2019

@author: samerd
'''
import re

import pycalc
from pycalc.menu import MenuItemHandler


class Calculator(MenuItemHandler):
    """
    Calculator menu handler.
    handles 'Calculate' user menu

    @cvar BINARY_OP_REGEX: regular expression for catching binary operations
    @cvar UNARY_OP_REGEX: regular expression for catching unary operations
    @cvar OP_MAPPING: maps for each operation symbol the operation function
                      that should be called
    """
    BINARY_OP_REGEX = re.compile(
        r'\s*(\-{0,1}[\d\.]+)\s*(\+|\-|\*|\/|\^)\s*(\-{0,1}[\d\.]+)\s*')
    UNARY_OP_REGEX = re.compile(
        r'\s*(V|v)\s*(\-{0,1}[\d\.]+)\s*')

    OP_MAPPING = {
        '+': pycalc.add,
        '-': pycalc.substract,
        '*': pycalc.multiply,
        '/': pycalc.divide,
        '^': pycalc.exponent,
        'V': pycalc.sqrt,
    }

    def on_select(self):
        """
        called when the user selected 'Calculate' option.
        it displays a menu description and asks the user to enter a question
        """
        print("Please enter a question in one of the following formats:")
        print("    1- op1 operator op2")
        print("    2- operator op")
        print("Where operator can be: +,-,*,/,^,V")
        print("   ^ denotes power and V denotes square root")
        question = input("Question: ")
        self.solve(question)

    def solve(self, question):
        """
        parses and solves the question of the user
        """
        # check if the question matches binary operation
        match = self.BINARY_OP_REGEX.match(question)
        if match:
            # read LHS operand
            op1 = self.get_number(match.group(1))
            if op1 is None:
                return
            # read operator
            operator = match.group(2)
            # read RHS operand
            op2 = self.get_number(match.group(3))
            if op2 is None:
                return
            # calculate the operation
            self.handle_binary_operator(op1, operator, op2)
            return
        # check match of unary operation
        match = self.UNARY_OP_REGEX.match(question)
        if match:
            # read operator
            operator = match.group(1).upper()
            # read operand
            op = self.get_number(match.group(2))
            if op is None:
                return
            # calculate the operation
            self.handle_unary_operator(operator, op)
            return
        # no match found
        print("Invalid question!")

    def get_number(self, operand):
        """
        try to read the number.
        first try to read it as int (base 10)
        in case of error try to read it as float
        if neither valid print an error
        """
        try:
            num = int(operand)
        except ValueError:
            try:
                num = float(operand)
            except ValueError:
                print("Invalid number %s" % operand)
                num = None
        return num

    def _call_operation(self, operator, *args):
        # call the appropriate operation according to the operator
        # use the OP_MAPPING to find the operation function
        func = self.OP_MAPPING.get(operator)
        if not func:
            print("Unsupported operator: %s!" % operator)
            return
        try:
            result = func(*args)
            print("Result: %s" % result)
        except Exception as exc:
            print(str(exc))

    def handle_binary_operator(self, op1, operator, op2):
        self._call_operation(operator, op1, op2)

    def handle_unary_operator(self, operator, op):
        self._call_operation(operator, op)
