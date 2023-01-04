# pa-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca
from click.testing import CliRunner
from pytest import mark
from pa_trading.pa import pa

run = CliRunner()


def test_exibe_versao():
    res = run.invoke(pa, ["--version"])
    assert res.output == "pa-trading 0.5.0\n"


@mark.skip()
def test_exibe_aviso_sem_comando():
    res = run.invoke(pa)
    assert res.output == "Digite gr --help para ajuda\n"


def test_calcula_a_linha_de_canal_projetada():
    res = run.invoke(pa, ["l", "2", "3"])
    assert res.output == "4.00\n"


def test_calcula_os_recuos_de_uma_perna():
    res = run.invoke(pa, ["pb", "100", "10"])
    assert res.output == "70.00\n55.00\n40.00\n"


def test_calcula_o_movimento_projetado_perna1_igual_perna2():
    res = run.invoke(pa, ["p2", "100", "10", "55"])
    assert res.output == "90.00\n145.00\n50%\n"


def test_calcula_as_regioes_da_lateralidade():
    res = run.invoke(pa, ["tr", "190", "100"])
    assert (
        res.output == "90.00\n280.00\n190.00\n160.00\n145.00\n130.00\n100.00\n10.00\n"
    )


def test_calcula_o_horario_de_fechamento_da_barra():
    res = run.invoke(pa, ["b", "18"])
    assert res.output == "10H30\n"
