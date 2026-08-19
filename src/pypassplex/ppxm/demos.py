import math
import pypassplex as ppx

# USED FOR CONVERTING Y/N (YES/NO) TO BOOLEAN.
def updateConfig(text):
    while True:
        var = input(f"{text} (yes / no): ").lower().strip()
        if var == "": continue # if no input
        elif var[0] == "y": return True # if yes
        elif var[0] == "n": return False # if no

def passGenDemo(): 
    # MAIN CODE
    # SETTINGS
    upperletters = updateConfig("Uppercase letters? ")
    lowerletters = updateConfig("Lowercase letters? ")
    numbers = updateConfig("Numbers? ")
    symbols = updateConfig("Symbols? ")

    try:
        length = int(input("Length of password: "))
    except ValueError:
        length = 12
        print("Length = 12")

    print("-"*80)

    # ------------------------------------ THIS IS WHERE PYPASSKIT IS USED!!!
    # GENERATE PASSWORD
    generated = ppx.passgen.generate(upperletters, lowerletters, numbers, symbols, length)

    # ENTROPY
    entropy = ppx.passgen.entropy(upperletters, lowerletters, numbers, symbols, length=len(generated))

    # -----------------------------------

    # PRINT PASSWORD AND ENTROPY
    print(f"Password - {generated}")
    print(f"Entropy - {math.floor(entropy)} bits")
    input("Press ENTER to continue")

def phraseGenDemo(): 
    # SETTINGS
    try:
        length = int(input("Number of words: "))
    except ValueError:
        length = 4
        print("Length = 4")

    delimiter = input("Delimiter (e.g. -): ")

    print("-"*80)

    # ------------------------------------ THIS IS WHERE PYPASSKIT IS USED!!!
    # GENERATE PASSWORD
    generated = ppx.phrasegen.generate(length=length, delimiter=delimiter)
    entropy = ppx.phrasegen.entropy(length=length)
    # -----------------------------------

    # PRINT PASSWORD AND ENTROPY
    print(f"Passphrase - {generated}")
    print(f"Entropy - {math.floor(entropy)} bits")
    input("Press ENTER to continue")
