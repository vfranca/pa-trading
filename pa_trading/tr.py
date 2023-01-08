# pa-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca
import click
from pa_trading.conf import formato_moeda


# Cria o comando tr
@click.command()
@click.argument("topo", type=float)
@click.argument("fundo", type=float)
@click.option("--digitos", "-d", default=2, help="Dígitos da moeda")
def tr(topo, fundo, digitos):
    """Exibe as regiões de uma lateralidade."""
    range = topo - fundo
    terco = range / 3
    terco_sup = topo - terco
    meio = (topo + fundo) / 2
    terco_inf = fundo + terco
    mm_alta = topo + range
    mm_baixa = fundo - range
    click.echo(formato_moeda % range)
    click.echo(formato_moeda % mm_alta)
    click.echo(formato_moeda % topo)
    click.echo(formato_moeda % terco_sup)
    click.echo(formato_moeda % meio)
    click.echo(formato_moeda % terco_inf)
    click.echo(formato_moeda % fundo)
    click.echo(formato_moeda % mm_baixa)


if __name__ == "__main__":
    tr()
