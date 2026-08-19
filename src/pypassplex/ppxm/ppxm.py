import pypassplex as ppx
from importlib.metadata import version
import demos

ppxver = version("pypassplex")

if ppxver[-2] == "b":
    beta = True
else:
    beta = False

print(fr""" ____  ______  __
|  _ \|  _ \ \/ /   PyPassPlex Manager
| |_) | |_) \  /    - Current version: {ppxver}
|  __/|  __//  \    - Beta release: {beta}
|_|   |_|  /_/\_\ 
---------------------------------------------------""")

choice = int(input("""
GETTING STARTED
1 - Password demo
2 - Passphrase demo

DOCUMENTATION
3 - View online documentation
4 - View security policy

DEBUG
5 - Report an issue
6 - PyPassPlex test script

Please choose an option (1-6)"""))

match choice:
    case 1:
        demos.passGenDemo()
    case 2:
        demos.phraseGenDemo()