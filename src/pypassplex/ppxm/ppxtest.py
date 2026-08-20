import pypassplex as ppx

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

def fullTest():
    # test all character sets disabled.
    test(ppx.passgen.generate, {
        "upper": False,
        "lower": False,
        "symbols": False,
        "numbers": False,
        "length": 10
    }, 102, False)