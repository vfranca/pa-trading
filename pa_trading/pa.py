# pa-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca
import click


# Importa os comandos
from pa_trading.l import l
from pa_trading.pb import pb
from pa_trading.tr import tr
from pa_trading.p2 import p2
from pa_trading.b import b


# Cria o grupo de comandos pa
@click.group()
def pa():
    """grupo de comandos pa (price action)."""
    pass


# Adiciona os comandos
pa.add_command(l)
pa.add_command(pb)
pa.add_command(tr)
pa.add_command(p2)
pa.add_command(b)


if __name__ == "__main__":
    pa()
