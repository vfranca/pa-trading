# pa-trading
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
from os import getenv

# Dígitos da moeda
digits = getenv("DIGITOS")
if digits == None:
    digits = 2
else:
    digits = int(digits)

# Formato da moeda
formato_moeda = "%." + str(digits) + "f"
