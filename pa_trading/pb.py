"""
grupo de comandos pa - price action
comando pb - pullbacks
"""
import click
from pa_trading._pb import pullback



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
    click.echo("%.2f" % recuo1)
    click.echo("%.2f" % recuo2)
    click.echo("%.2f" % recuo3)


if __name__ == "__main__":
    pb()
