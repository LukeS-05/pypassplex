import pypassplex as ppx
from importlib.metadata import version

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
1 - PyPassPlex demo

DOCUMENTATION
2 - View documentation
3 - View security policy

DEBUG
4 - Report an issue
5 - PyPassPlex test script

Please choose an option (1-5)"""))