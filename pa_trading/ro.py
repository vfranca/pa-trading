# pa-trading
# Copyright 2021 Valmir França da Silva
# http://github.com/vfranca
import click


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
    click.echo("%.2f range restante" % range_restante)
    click.echo("%.2f max" % max_projetada)
    click.echo("%.2f min" % min_projetada)


if __name__ == "__main__":
    ro()
