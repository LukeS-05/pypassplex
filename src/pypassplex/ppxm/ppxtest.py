import pypassplex as ppx
import time

def strToBool(text):
    while True:
        var = input(f"{text} (yes / no): ").lower().strip()
        if var == "": continue # if no input
        elif var[0] == "y": return True # if yes
        elif var[0] == "n": return False # if no

def test(function, arguments, id, shouldPass):
    try:
        function(**arguments)
        executed = True
        error = ""
    except Exception as e:
        executed = False
        error = e
    
    if (not(executed) and not(shouldPass)) or (executed and shouldPass):
        print(f"Test ID {id} was successful - {error}\nshouldPass = {shouldPass} and executed without error = {executed}")
    else:
        print(f"Test ID {id} was not successful - {error}\nshouldPass = {shouldPass} and executed without error = {executed}")

    print("-"*50)
    time.sleep(0.5)

def initTest():
    print("┌" + "─"*50 + "┐")
    print("│ PyPassPlex TEST SCRIPT                           │")
    print("└" + "─"*50 + "┘")
    passgen = strToBool("Test passgen module?")
    pingen = strToBool("Test pingen module?")
    phrasegen = strToBool("Test phrasegen module?")
    if passgen:
        passgenTest()
    if pingen:
        pingenTest()
    if phrasegen:
        phrasegenTest()

    input("Tests ended. Press any key to continue")
    
def passgenTest():
    print("Testing PyPassPlex... (passgen module)")
    # test all character sets disabled.
    test(ppx.passgen.generate, {
        "upper": False,
        "lower": False,
        "symbols": False,
        "numbers": False,
        "length": 10
    }, 102, False)

    # invalid pool data type
    test(ppx.passgen.generate, {
        "pool": 19894383,
        "length": 10
    }, 103, False)

    # invalid pool data type (with bool) 
    test(ppx.passgen.generate, {
        "pool": True,
        "length": 10
    }, 104, False)

    # invalid character toggle data type
    test(ppx.passgen.generate, {
        "upper": 213,
        "length": 10
    }, 105, False)

    # length is too small
    test(ppx.passgen.generate, {
        # by default, upper, lower, numbers and symbols are all true.
        "length": 2
    }, 106, False)

    # invalid data type for length
    test(ppx.passgen.generate, {
        
        "length": "one"
    }, 107, False)

    input("PASSGEN TEST ENDED")

def pingenTest():
    print("Not implemented")

    input("PINGEN TEST ENDED")

def phrasegenTest():
    print("Not implemented")

    input("PHRASEGEN TEST ENDED")