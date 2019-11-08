'''
Created on Nov 7, 2019

@author: samerd
'''

import sys

# in this module we are importing the reused library and give it local names.
# so in case we change the reused library, we can make the change in one place
try:
    # pylint: disable=useless-import-alias
    from seng560Calc import add as add
    from seng560Calc import subtract as substract
    from seng560Calc import multiply as multiply
    from seng560Calc import divide as divide
    from seng560Calc import exponent as exponent
    from seng560Calc import squareroot as sqrt

    from seng560Calc import convertToBin as to_bin
    from seng560Calc import convertToOct as to_oct
    from seng560Calc import convertToInt as to_decimal
    from seng560Calc import convertToHex as to_hex

except ImportError:
    print("missing library seng560Calc!, please clone the repository "
          "and add it to your PYTHONPATH\n"
          "URL: https://github.com/jdc0051/seng560Calc")
    sys.exit(1)
