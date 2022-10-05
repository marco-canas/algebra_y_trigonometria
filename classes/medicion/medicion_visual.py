# Aqú voy a construir una función que estime la altura de un pararayos utilizando la línea visual
def medir_altura_visual(altura_persona, dpa, dap, altura_arbol):
    from sympy import * 
    altura_persona, altura_arbol, dpa, dap, h, x = var("altura_persona, altura_arbol, dpa, dap, h, x ") 
    ecuacion_1 = Eq(h/altura_arbol, (x+dpa+dap)/(dpa+x) )
    ecuacion_2 = Eq(altura_arbol/altura_persona, x/(x+dpa)) 
    altura_estimada = solve([ecuacion_1, ecuacion_2], (h, x))[0]
    return altura_estimada 


if __name__=='__main__':
        