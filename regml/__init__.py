name = "Regularization Methods for Machine Learning"

# PEP0440 compatible formatted version, see:
# https://www.python.org/dev/peps/pep-0440/
#
# Generic release markers:
#   X.Y
#   X.Y.Z   # For bugfix releases
#
# Admissible pre-release markers:
#   X.YaN   # Alpha release
#   X.YbN   # Beta release
#   X.YrcN  # Release Candidate
#   X.Y     # Final release
#
# Dev branch marker is: 'X.Y.devN' where N is an integer.
#

__version__ = '0.1.0'
__year__    = '2016'
__author__  = 'Nikesh Bajaj - not exactly'

import sys

from .RegML_GUI import RegML

# for Python3
if sys.version_info >= (3,0):
    from tkinter import *

# for Python2
else:
    from Tkinter import *

def GUI():
    root = Tk()
    App = RegML(root)
    root.mainloop()
