# pa-trading
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
import click


# Cria o comando b
@click.command()
@click.argument("bar", type=float)
def b(bar):
    """Calcula o horário de fechamento da barra."""
    # Calcula o total de minutos da barra
    minutos = bar * 5
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
