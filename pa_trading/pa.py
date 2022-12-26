"""
scripts python
Copyright 2022 Valmir França da Silva

grupo de comandos pa (price action)
"""
import click


# Importa os comandos
from pa_trading.l import l
from pa_trading.pb import pb
from pa_trading.tr import tr
from pa_trading.p2 import p2


# Cria o grupo de comandos pa
@click.group()
def cli():
    """grupo de comandos pa (price action)."""
    pass


# Adiciona os comandos
cli.add_command(l)
cli.add_command(pb)
cli.add_command(tr)
cli.add_command(p2)


if __name__ == "__main__":
    cli()
