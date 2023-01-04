# pa-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca


def tamanho_perna(preco_final, preco_inicial):
    return float(preco_final - preco_inicial)


def metade_perna(tamanho):
    return float(tamanho / 2)


def terco_perna(tamanho):
    return float(tamanho / 3)


def retracao_um_terco(preco_final, terco):
    return float(preco_final - terco)


def retracao_metade(preco_final, metade):
    return float(preco_final - metade)


def retracao_dois_tercos(preco_final, terco):
    return float(preco_final - terco * 2)
