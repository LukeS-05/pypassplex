#  ____  ______  __    To contribute to PyPassPlex, please go to
# |  _ \|  _ \ \/ /    https://lukes-05.github.io/pypassplex/contribute
# | |_) | |_) \  /     
# |  __/|  __//  \     Copyright (C) 2026 LukeS-05 - This library is licensed under the
# |_|   |_|  /_/\_\    MIT License
# ______________________________________________________________________________________

import secrets, string, math
from importlib.metadata import version
from .errors import error

__version__ = version("pypassplex")
__all__ = ["generate", "entropy"]

def buildPool(upper=True, lower=True, numbers=True, symbols=True):
    # 1 - CHECK BOOLEAN VALUES HAVE BEEN PASSED
    if not(isinstance(upper, bool)) or not(isinstance(lower, bool)) or not(isinstance(numbers, bool)) or not(isinstance(symbols, bool)):
        error(TypeError, 201, "passgen")

    # 2 - INITIALISE CHARACTERS VARIABLE
    characters = ""

    # 3 - APPEND TO POOL
    if upper: 
        characters += string.ascii_uppercase
    if lower: 
        characters += string.ascii_lowercase
    if numbers: 
        characters += string.digits
    if symbols: 
        characters += string.punctuation

    # 4 - RETURN POOL
    return characters

def validateParameters(upper=True, lower=True, numbers=True, symbols=True, length=10):
    selected = sum([upper, lower, numbers, symbols])
                
    # VALIDATE LENGTH AND SELECTED CATEGORIES
    if length < selected: 
        error(ValueError, 203, "passgen")
    if selected == 0: 
        error(ValueError, 204, "passgen")

def satisfiesRequirements(upper, lower, numbers, symbols, candidate):
    hasupper = False
    haslower = False
    hasnumbers = False
    hassymbols = False

    for i in candidate:
        if i in string.ascii_uppercase: 
            hasupper = True
        elif i in string.ascii_lowercase: 
            haslower = True
        elif i in string.digits: 
            hasnumbers = True
        elif i in string.punctuation: 
            hassymbols = True

    if upper and not(hasupper): 
        return False
    if lower and not(haslower): 
        return False
    if numbers and not(hasnumbers): 
        return False
    if symbols and not(hassymbols): 
        return False

    return True

def generateCandidate(pool, length):
    charslist = []
    # CHOOSE EACH CHARACTER
    while len(charslist) < length:
        # use secrets module to choose from character pool
        charslist.append(secrets.choice(pool))

    candidate = "".join(charslist)

    return candidate

def generate(upper=True, lower=True, numbers=True, symbols=True, length=10, pool=None):
    if not(isinstance(length, int)) or isinstance(length, bool): 
        error(TypeError, 202, "passgen")
    if length <= 0:
        error(ValueError, 208, "passgen")
    if pool is not None:
        if not(isinstance(pool, str)) or pool == "":
            error(TypeError, 209, "passgen")
        characters = "".join(dict.fromkeys(pool))
    else:
        # BUILD CHARACTER POOL
        characters = buildPool(upper, lower, numbers, symbols)
        # VALIDATION
        validateParameters(upper, lower, numbers, symbols, length)

    password = ""
    if pool is not None:
        password = generateCandidate(pool=characters, length=length)
    else:
        while not(satisfiesRequirements(upper, lower, numbers, symbols, password)):
            password = generateCandidate(pool=characters, length=length)
    
    # RETURN PASSWORD
    return password

# UPGRADED ENTROPY FUNCTION IN 0.9.0
def entropy(upper=True, lower=True, numbers=True, symbols=True, length=10, pool=None):
    if not(isinstance(length, int)) or isinstance(length, bool): # 0.9.0 - handled booleans passed to length parameter
        error(TypeError, 206, "passgen")

    # HANDLED NEGATIVE LENGTHS (0.7.1)
    if length <= 0:
        error(ValueError, 208, "passgen")

    # OLD ENTROPY LOGIC
    if pool is not None:
        # DATA TYPE VALIDATION
        if not(isinstance(pool, str)) or pool == "":
            error(TypeError, 209, "passgen")
        characters = "".join(dict.fromkeys(pool))
    # NEW LOGIC (SIMILAR TO GENERATE())
    else:
        characters = buildPool(upper, lower, numbers, symbols)
        validateParameters(upper, lower, numbers, symbols, length)

    poolsize = len(set(characters))
    passwordentropy = length * math.log2(poolsize)

    return passwordentropy