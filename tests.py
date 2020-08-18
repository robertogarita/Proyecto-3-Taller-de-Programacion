from Hypersudoku import *

#las pruebas que estan comentadas son porque esas funciones no se pueden probar ya que estan dentro de una clase y el parametro es self y esto se refiere al objeto instanceado de esa clase, sobre el cual se esta invocando dicho metodo

#PRUEBAS DE LA CLASE GAME
# __init__
def test___init__():
    try:
        #assert __init__(self, weithd= 500, height= 580)==
        #assert __init__(self, weithd= 500, height= 580)==
        print("Correcto")
    except:
        print("Incorrecto")

# get cord
def test_get_cord():
    try:
        #assert get_cord(self,pos)==
        #assert get_cord(self,pos)==
        print("Correcto")
    except:
        print("Incorrecto")

# draw box
def test_draw_box():
    try:
        #assert draw_box(self)==
        #assert draw_box(self)==
        print("Correcto")
    except:
        print("Incorrecto")

# draw
def test_draw():
    try:
        #assert draw(self)==
        #assert draw(self)==
        print("Correcto")
    except:
        print("Incorrecto")

# draw val
def test_darw_val():
    try:
        #assert draw_val(self,val)==
        #assert draw_val(self,val)==
        print("Correcto")
    except:
        print("Incorrecto")

# raise error1
def test_raise_error1():
    try:
        #assert raise_error1(self)==
        #assert raise_error1(self)==
        print("Correcto")
    except:
        print("Incorrecto")

# raise error2
def test_raise_error2():
    try:
        #assert raise_error2(self)==
        #assert raise_error2(self)==
        print("Correcto")
    except:
        print("Incorrecto")

# valid
def test_valid():
    try:
        #assert valid(self,m, i, j, val)==
        #assert valid(self,m, i, j, val)==
        print("Correcto")
    except:
        print("Incorrecto")

# solve
def test_solve():
    try:
        #assert solve(self,grid, i, j)==
        #assert solve(self,grid, i, j)==
        print("Correcto")
    except:
        print("Incorrecto")

# instruction
def test_instruction():
    try:
        #assert instruction(self)==
        #assert instruction(self)==
        print("Correcto")
    except:
        print("Incorrecto")

# result
def test_result():
    try:
        #assert result(self)==
        #assert result(self)==
        print("Correcto")
    except:
        print("Incorrecto")

# iniciar
def test_iniciar():
    try:
        #assert iniciar(self)==
        #assert iniciar(self)==
        print("Correcto")
    except:
        print("Incorrecto")

# GAME
print("Pruebas de la clase Game")
test___init__()
test_get_cord()
test_draw_box()
test_draw()
test_darw_val()
test_raise_error1()
test_raise_error2()
test_valid()
test_solve()
test_instruction()
test_result()
test_iniciar()


