from importlib.metadata import version
__version__ = version("pypassplex") 

descriptions = [
    [201, "Character pool config (e.g. upper) must be given as booleans."],
    [202, "Password length must be given as an integer."],
    [203, "Length must be greater than or equal to the number of character types selected."],
    [204, "You must select at least one type of character."],
    [206, "Password length must be given as an integer."],
    [208, "Length must be greater than 0."],
    [209, "Character pool must be given as a non-empty string."],
    [211, "File does not exist."],
    [212, "You must pass EITHER file or wordlist as argument\nBoth have been passed."],
    [214, "Wordlist must be a list"],
    [215, "Wordlist is empty"],
    [216, "Elements of the wordlist must be string values."],
    [218, "Case must be lower, upper or title"],
    [219, "Runtime Error"],
    [236, "PIN length must be given as an integer."],
    [237, "Length must be greater than or equal to 1 for a PIN."]
]

def error(type=ValueError, code=208, module="phrasegen", info=""):
    desc = "unknown"
    for i in range(0, len(descriptions)):
        if descriptions[i][0] == code:
            desc = descriptions[i][1]
    
    raise type(f"[{code}] ({module}@PPX{__version__}) - {desc} {info}")