#  ____  ______  __    To contribute to PyPassPlex, please go to
# |  _ \|  _ \ \/ /    https://lukes-05.github.io/pypassplex/contribute
# | |_) | |_) \  /     
# |  __/|  __//  \     Copyright (C) 2026 LukeS-05 - This library is licensed under the
# |_|   |_|  /_/\_\    MIT License
# ______________________________________________________________________________________

import string
from . import passgen
from importlib.metadata import version
from .errors import error

__version__ = version("pypassplex") 
__all__ = ["generate", "entropy"]

def generate(length=6):
    pincode= passgen.generate(pool=string.digits, length=length)
    return pincode
    
def entropy(length=6):
    if not(isinstance(length, int)):
        error(TypeError, 236, "pingen")
    
    if length < 1:
        error(ValueError, 237, "pingen")
    entropy = passgen.entropy(pool=string.digits, length=length)
    return entropy
