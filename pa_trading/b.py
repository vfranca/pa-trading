# pa-trading
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
import click


# Cria o comando b
@click.command()
@click.argument("bar", type=float)
@click.option("--period", "-p", default="m5", help="Período da barra.")
def b(bar, period):
    """Calcula o horário de fechamento da barra."""
    #  Define o período da barra
    minutos_barra = 5
    if period.upper() == "M3":
        minutos_barra = 3
    elif period.upper() == "M10":
        minutos_barra = 10
    elif period.upper() == "M15":
        minutos_barra = 15
    elif period.upper() == "M20":
        minutos_barra = 20
    elif period.upper() == "M30":
        minutos_barra = 30
    elif period.upper() == "H1":
        minutos_barra = 60
    # Calcula o total de minutos da barra
    minutos = bar * minutos_barra
    # Calcula o total de horas da  barra
    horas = minutos / 60
    # Calcula a hora da barra
    hora = horas + 9
    # Obtem os minutos a partir da hora
    minuto = abs(int(hora) - hora)
    minuto = round(minuto * 60)
    # Obtem a parte inteira da hora
    hora = int(hora)
    click.echo("%iH%i" % (hora, minuto))


if __name__ == "__main__":
    b()
