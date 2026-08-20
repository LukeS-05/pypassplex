import pypassplex as ppx
import time

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

def fullTest():
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

    input("Test ended. Press any key to continue")