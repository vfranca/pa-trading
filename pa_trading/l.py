# pa-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca
import click


# Cria o comando l - linha de canal
@click.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def l(a, b):
    """Calcula proximo ponto da linha de canal."""
    gap = a - b
    c = b - gap
    click.echo("%.2f" % c)


if __name__ == "__main__":
    l()
