# pa-trading
# Copyright 2021 Valmir França da Silva
# http://github.com/vfranca
import click
from pa_trading.conf import formato_moeda


# Cria o comando ro
@click.command()
@click.argument("max", type=float)
@click.argument("min", type=float)
@click.option("--range-medio", "-rm", type=float, default=2500)
def ro(max, min, range_medio):
    """Calcula estimativa de máxima e mínima do range operável no intraday."""
    # Calcula o range atual
    range_atual = max - min
    # Calcula o range restante estimado do dia
    range_restante = range_medio - range_atual
    # Calcula a máxima estimada do dia
    max_projetada = max + range_restante
    # Calcula a mínima estimada do dia
    min_projetada = min - range_restante
    formato = formato_moeda + " = range restante"
    click.echo(formato % range_restante)
    formato = formato_moeda + " = máxima"
    click.echo(formato % max_projetada)
    formato = formato_moeda + " = mínima"
    click.echo(formato % min_projetada)


if __name__ == "__main__":
    ro()
