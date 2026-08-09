#  ____  ______  __    To contribute to PyPassPlex, please go to
# |  _ \|  _ \ \/ /    https://lukes-05.github.io/pypassplex/contribute
# | |_) | |_) \  /     
# |  __/|  __//  \     Copyright (C) 2026 LukeS-05 - This library is licensed under the
# |_|   |_|  /_/\_\    MIT License
# ______________________________________________________________________________________

import secrets, string, math
from importlib.metadata import version

__version__ = version("pypassplex")
__all__ = ["generate", "entropy"]

def buildPool(upper=True, lower=True, numbers=True, symbols=True):
    # 1 - CHECK BOOLEAN VALUES HAVE BEEN PASSED
    if not(isinstance(upper, bool)) or not(isinstance(lower, bool)) or not(isinstance(numbers, bool)) or not(isinstance(symbols, bool)):
        raise TypeError(f"[201] (passgen@PPX v{__version__}) - Character pool config (e.g. upper) must be given as booleans.")

    # 2 - INITIALISE CHARACTERS VARIABLE
    characters = ""

    # 3 - APPEND TO POOL
    if upper: characters += string.ascii_uppercase
    if lower: characters += string.ascii_lowercase
    if numbers: characters += string.digits
    if symbols: characters += string.punctuation

    # 4 - RETURN POOL
    return characters

def validateParameters(upper=True, lower=True, numbers=True, symbols=True, length=10):
    selected = sum([upper, lower, numbers, symbols])
                
    # VALIDATE LENGTH AND SELECTED CATEGORIES
    if length < selected: raise ValueError(f"[203] (passgen@PPX v{__version__}) - Length must be greater than or equal to the number of character types selected ({selected}).")
    if selected == 0: raise ValueError(f"[204] (passgen@PPX v{__version__}) - You must select at least one type of character.")
    
def generate(upper=True, lower=True, numbers=True, symbols=True, length=10, returnPool=False):
    # 1 - DATA TYPE VALIDATION
    if not(isinstance(length, int)) or isinstance(length, bool): 
        raise TypeError(f"[202] (passgen@PPX v{__version__}) - Password length must be given as an integer.")

    # 2 - BUILD CHARACTER POOL
    characters = buildPool(upper, lower, numbers, symbols)
    # 3 - VALIDATION
    validateParameters(upper, lower, numbers, symbols, length)
    
    # 4 - INITIALISE CHARSLIST
    charslist = []

    # 5 - GUARANTEE EACH CHARACTER TYPE APPEARS IN THE PASSWORD
    if upper: charslist.append(secrets.choice(string.ascii_uppercase))
    if lower: charslist.append(secrets.choice(string.ascii_lowercase))
    if numbers: charslist.append(secrets.choice(string.digits))
    if symbols: charslist.append(secrets.choice(string.punctuation))

    # 6 - CHOOSE EACH CHARACTER
    while len(charslist) < length:
        # use secrets module to choose from character pool
        charslist.append(secrets.choice(characters))

    # 7 - SHUFFLE PASSWORD SO REQUIRED CHARS AREN'T ALWAYS AT BEGINNING (i.e. Aa1@)
    secrets.SystemRandom().shuffle(charslist)
    password = "".join(charslist)

    # 8 - RETURN PASSWORD (AND POOL if returnPool)
    if returnPool: return password, characters
    return password

# UPGRADED ENTROPY FUNCTION IN 0.9.0
def entropy(upper=True, lower=True, numbers=True, symbols=True, length=10, pool=None):
    if not(isinstance(length, int)) or isinstance(length, bool): # 0.9.0 - handled booleans passed to length parameter
        raise TypeError(f"[206] (passgen@PPX v{__version__}) - Password length must be given as an integer.")

    # HANDLED NEGATIVE LENGTHS (0.7.1)
    if length < 0:
        raise ValueError(f"[208] (passgen@PPX v{__version__}) - Length must not be a negative number.")

    # OLD ENTROPY LOGIC
    if pool is not None:
        # DATA TYPE VALIDATION
        if not(isinstance(pool, str)) or pool == "":
            raise TypeError(f"[209] (passgen@PPX v{__version__}) - Character pool must be given as a non-empty string.")
        characters = pool
    # NEW LOGIC (SIMILAR TO GENERATE())
    else:
        characters = buildPool(upper, lower, numbers, symbols)
        validateParameters(upper, lower, numbers, symbols, length)

    poolsize = len(set(characters))
    passwordentropy = length * math.log2(poolsize)

    return passwordentropy