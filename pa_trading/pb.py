# pa-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca
import click
from pa_trading._pb import pullback
from pa_trading.conf import formato_moeda


# Cria o comando pb
@click.command()
@click.argument("preco_final", type=float)
@click.argument("preco_inicial", type=float)
def pb(preco_final, preco_inicial):
    """Calcula retracoes de uma perna."""
    tamanho = pullback.tamanho_perna(preco_final, preco_inicial)
    metade = pullback.metade_perna(tamanho)
    terco = pullback.terco_perna(tamanho)
    recuo1 = pullback.retracao_um_terco(preco_final, terco)
    recuo2 = pullback.retracao_metade(preco_final, metade)
    recuo3 = pullback.retracao_dois_tercos(preco_final, terco)
    click.echo(formato_moeda % recuo1)
    click.echo(formato_moeda % recuo2)
    click.echo(formato_moeda % recuo3)


if __name__ == "__main__":
    pb()
