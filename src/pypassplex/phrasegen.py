#  ____  ______  __    To contribute to PyPassPlex, please go to
# |  _ \|  _ \ \/ /    https://lukes-05.github.io/pypassplex/contribute
# | |_) | |_) \  /     
# |  __/|  __//  \     Copyright (C) 2026 LukeS-05 - This library is licensed under the
# |_|   |_|  /_/\_\    MIT License
# ______________________________________________________________________________________

import secrets, math
from importlib.metadata import version
import importlib.resources as resources
from .errors import error


__version__ = version("pypassplex") 
__all__ = ["generate","entropy"]

# 0.7.1 - NEW WORDSLIST FUNCTION TO REPLACE IDENTICAL CODE IN TWO FUNCTIONS
def wordsList(file=None, wordlist=None):
    # 1 - GENERATE WORDLIST
    # RULE 1 - IF BOTH ARE PASSED, RAISE VALUEERROR
    if file and wordlist: error(ValueError, 212, "phrasegen")
    # RULE 2 - IF NEITHER IS PASSED, USE EFF WORDS LIST
    if not file and not wordlist: 
        try:
            with resources.files("pypassplex").joinpath("eff-words.txt").open("r", encoding="utf-8") as f:
                words = f.read().splitlines()
        except Exception as e:
            error(RuntimeError, 219, "phrasegen", e)
    # RULE 3 - IF ONLY FILE IS PASSED, USE FILE
    elif file:
        try:
            # 0.7.1 - FIX FOR UnicodeDecodeError
            with open(file, "r", encoding="utf-8") as f:
                words = f.read().splitlines()
        except FileNotFoundError as e:
            error(FileNotFoundError, 212, "phrasegen", e)
    # RULE 4 - IF ONLY WORD LIST IS PASSED, USE WORD LIST
    elif wordlist:
        if not(isinstance(wordlist, list)):
            error(ValueError, 214, "phrasegen")
        words = wordlist
    # 2 - REMOVE SPACES FROM WORD LIST
    words = [w for w in words if w.strip()]

    words = list(dict.fromkeys(words))

    if not(words):
        error(ValueError, 215, "phrasegen")

    # 3 - RETURN WORDS
    return words

def generate(file=None, wordlist=None, length=4, delimiter="-", case="lower"):
    if length <= 0:
        error(ValueError, 208, "phrasegen")
    
    words = wordsList(file, wordlist)

    if case not in ["lower", "upper", "title"]:
        error(ValueError, 218, "phrasegen")
    
    passphrase = "" # nosec 
    for i in range(length):
        chosen = secrets.choice(words)
        
        if case=="lower": passphrase += chosen.lower()
        elif case == "upper": passphrase += chosen.upper()
        elif case == "title": passphrase += chosen.title()

        # to prevent delimiter at the end
        if i != (length-1):
            passphrase += delimiter
        
    return passphrase

def entropy(file=None, wordlist=None, length=4):
    if length <= 0:
        error(ValueError, 208, "phrasegen")
    
    words = wordsList(file, wordlist)
        
    phraseentropy = length * math.log2(len(set(words))) # 0.7.1 - DON'T ALLOW DUPLICATE WORDS
    return phraseentropy