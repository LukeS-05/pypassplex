import pypassplex as ppx
from importlib.metadata import version

ppxver = version("pypassplex")

if ppxver[-2] == "b":
    beta = True
else:
    beta = False

print(f""" ____  ______  __
|  _ \|  _ \ \/ /   PyPassPlex Manager
| |_) | |_) \  /    - Current version: {ppxver}
|  __/|  __//  \    - Beta release: {beta}
|_|   |_|  /_/\_\ """)