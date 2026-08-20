import pypassplex as ppx
from importlib.metadata import version
from pypassplex.ppxm.demos import passGenDemo, phraseGenDemo
from pypassplex.ppxm.ppxtest import fullTest
import webbrowser

ppxver = version("pypassplex")

if ppxver[-2] == "b":
    beta = True
else:
    beta = False

def main():
    while True:
        print("┌" + "─"*50 + "┐")
        print("│ PyPassPlex Manager                               │")
        print("└" + "─"*50 + "┘")
        print(f" Version: {ppxver}; Beta: {beta}")
        print("""
│ GETTING STARTED
│ 1 - Password demo
│ 2 - Passphrase demo

│ DOCUMENTATION
│ 3 - View online documentation
│ 4 - View security policy

│ DEBUG
│ 5 - Report an issue
│ 6 - PyPassPlex test script

│ OTHER
│ 7 - Quit
""")

        choice = 0
        while choice > 7 or choice < 1:
            choice = int(input("Please choose an option (1-7)"))

        match choice:
            case 1:
                passGenDemo()
            case 2:
                phraseGenDemo()
            case 3:
                webbrowser.open("https://lukes-05.github.io/pypassplex/docs")
            case 4:
                webbrowser.open("https://github.com/lukes-05/pypassplex/blob/main/SECURITY.md")
            case 5:
                webbrowser.open("https://lukes-05.github.io/pypassplex/contribute")
            case 6:
                fullTest()
            case 7:
                raise SystemExit

if __name__ == "__main__":
    main()