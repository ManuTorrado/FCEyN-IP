from pytest import MonkeyPatch, LogCaptureFixture
import runpy
from test import filasParecidas
from typing import List
from io import StringIO


def crearTest(
    monkeypatch: MonkeyPatch,
    capsys: LogCaptureFixture,
    nombre_archivo: str,
):
    def test(descripcion_test: str, respuestas: List[str], salida_esperada: str):
        if isinstance(respuestas, list):
            monkeypatch.setattr('sys.stdin', StringIO('\n'.join(respuestas)))
        else:
            monkeypatch.setattr('sys.stdin', StringIO(respuestas + '\n'))

        runpy.run_path(nombre_archivo, None, '__main__')
        salida = str(capsys.readouterr().out).rstrip('\n')
        assert salida == salida_esperada, descripcion_test

    return test


def test_quien_gana(monkeypatch, capsys):
    test = crearTest(monkeypatch, capsys, 'quienGana.py')
    test('jugador 1 gana con papel', ['papel piedra'], 'Jugador1')
    test('jugador 1 gana con piedra', ['piedra tijera'], 'Jugador1')
    test('jugador 1 gana con tijera', ['tijera papel'], 'Jugador1')

    test('jugador 2 gana con papel', ['piedra papel'], 'Jugador2')
    test('jugador 2 gana con piedra', ['tijera piedra'], 'Jugador2')
    test('jugador 2 gana con tijera', ['papel tijera'], 'Jugador2')

    test('jugador 1 empata con jugador 2', ['piedra piedra'], 'Empate')
    test('jugador 1 empata con jugador 2', ['papel papel'], 'Empate')
    test('jugador 1 empata con jugador 2', ['tijera tijera'], 'Empate')


def test_meseta_mas_larga(monkeypatch, capsys):
    test = crearTest(monkeypatch, capsys, 'mesetaMasLarga.py')

    test('meseta mas larga al principio', '1 1 2 3', '2')
    test('meseta mas larga al final', '2 3 1 1', '2')
    test('meseta mas larga a la mitad', ['1 1 2 2 2 3 3'], '3')
    test('multiples mesetas largas a la mitad', '1 2 2 2 3 3 3 4 4 4 5', '3')

    test('mesetas mas largas negativas', '1 -2 -2 -2 3 3 4 4 5', '3')


def test_fibonnaci(monkeypatch, capsys):
    test = crearTest(monkeypatch, capsys, 'fibonacciNoRecursivo.py')
    test('fibonacci 0', '0', '0')
    test('fibonacci 1', '1', '1')
    test('fibonacci 2', '2', '1')
    test('fibonacci 3', '3', '2')
    test('fibonacci 6', '6', '8')
    test('fibonacci 7', '7', '13')
    test('fibonacci 8', '8', '21')
    test('fibonacci 9', '9', '34')
    test('fibonacci 10', '10', '55')
    test('fibonacci 17', '17', '1597')
    test('fibonacci 50', '50', '12586269025')
    test('fibonacci 100', '100', '354224848179261915075')
    test('fibonacci 300', '300',
         '222232244629420445529739893461909967206666939096499764990979600')


def test_filas_parecidas(monkeypatch, capsys):
    test = crearTest(monkeypatch, capsys, 'filasParecidas.py')
    test('filas parecidas positivas con n 0, numeros positivos',
         ['3', '3', '1 2 3', '1 2 3', '1 2 3'], 'True')
    test('filas parecidas negativas con n 0, numeros negativos',
         ['3', '3', '-1 -2 -3', '-1 -2 -3', '-1 -2 -3'], 'True')

    test('filas parecidas positivas con n negativo (n=-1)',
         ['3', '3', '1 2 3', '0 1 2', '-1 0 1'], 'True')
    test('filas parecidas positivas con n negavito (n=-2)',
         ['3', '3', '1 2 3', '-1 0 1', '-3 -2 -1'], 'True')

    test('filas parecidas negativas con n negativo (n=-1)',
         ['3', '3', '-1 -2 -3', '-2 -3 -4', '-3 -4 -5'], 'True')
    test('filas parecidas negativas con n positivo (n=1)', [
         '3', '3', '-1 -2 -3', '0 -1 -2', '1 0 1'], 'True')

    test('filas parecidas positivas con n positivo (n=1)',
         ['3', '3', '1 2 3', '2 3 4', '3 4 5'], 'True')
    test('filas parecidas positivas con n positivo (n=2)',
         ['3', '3', '1 2 3', '3 4 5', '5 6 8'], 'True')

    test('filas parecidas mixtas con n positivo (n=1)', [
         '3', '4', '1 2 3 4 ', '2 3 4 5', '3 4 5 6'], 'True')
    test('filas parecidas mixtas con n negativo (n=-1)',
         ['3', '4', '1 2 3 4', '0 1 2 3', '-1 0 1 2'], 'True')
    test('filas parecidas mixtas positivas con n negativo (n=-10)',
         ['2', '3', '1 2 3', '-9 -8 -7'], 'True')

    test('filas parecidas con n matrices de dos filas y una columna #1 (siempre debe dar true)', [
         '2', '1', '5', '1'], 'True')
    test('filas parecidas con n matrices de dos filas y una columna #1 (siempre debe dar true)', [
         '2', '1', '2', '1'], 'True')
    test('filas parecidas con n matrices de dos filas y una columna #1 (siempre debe dar true)', [
         '2', '1', '10', '-100'], 'True')

    test('filas no parecidas mixtas positivas con n negativo',
         ['2', '3', '1 2 3', '-9 -10 -7'], 'False')
    test('1ra fila no parecida', [
         '5', '2', '100 200', '5 6', '1 2', '1 2', '1 2'], 'False')
    test('2da fila no parecida', ['5', '2', '1 2',
         '100 200', '1 2', '1 2', '1 2'], 'False')
    test('3ra fila no parecida', ['5', '2', '1 2',
         '1 2', '100 200', '1 2', '1 2'], 'False')
    test('4ta fila no parecida', ['5', '2', '1 2',
         '5 6', '1 2', '100 200', '1 2'], 'False')
    test('ultima fila no parecida', [
         '5', '2', '1 2', '1 2', '1 2', '1 2', '100 200'], 'False')

    test('debe dar false para 1 fila 1 columna', ['1', '1', '1'], 'False')


def test_se_puede_llegar(monkeypatch, capsys):
    test = crearTest(monkeypatch, capsys, 'sePuedeLlegar.py')
    test("se puede llegar", ['rosario', 'jujuy',
         'misiones,jujuy salta,chubut rosario,misiones'], '2')
    test("se puede llegar #2", ['rosario', 'buenos-aires',
         'rosario,jujuy san-telmo,jujuy chubut,buenos-aires jujuy,chubut'], '3')
    test("no se puede llegar #1", ['rosario', 'jujuy', 'misiones,jujuy'], '-1')
    test("no se puede llegar #2", [
         'rosario', 'jujuy', 'rosario,misiones, jujuy,chubut'], '-1')
    test("no se puede llegar #3", ['rosario', 'buenos-aires',
         'rosario,misiones, misiones,chubut, la-pampa,buenos-aires'], '-1')
    test("no se puede llegar #4", ['rosario', 'buenos-aires',
         'jujuy,chubut, cordoba,buenos-aires, rosario,misiones, chubut,la-pampa, la-pampa,mendoza'], '-1')
    test("no se puede llegar #5 (cíclica)", ['A', 'B', 'A,C, C,A, D,B'], '-1')
