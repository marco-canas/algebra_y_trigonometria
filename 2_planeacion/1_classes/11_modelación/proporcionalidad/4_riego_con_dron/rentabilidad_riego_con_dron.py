# Este es una programa para calcular la rentabilidad de hacer riego con Dron en el Bajo Cauca Antioqueño

def valor_por_hectarea_fumigacion_manual():
    valor_mano_obra_por_hectarea = int(input('Entre el valor de la mano de obra por hectarea para fumigar: '))
    valor_agroquimico_por_hectarea = int(input("Entre el valor del agroquímico necesario para funigar una hectárea: "))
    valor_de_bombear_agua_para_hectarea = int(input('Entre el costo de obtención del agua para fumigar una hectárea: '))
    valor_por_hectarea = valor_mano_obra_por_hectarea+valor_agroquimico_por_hectarea+valor_de_bombear_agua_para_hectarea 
    return print('el valor total de fumigar manualmente es: ', valor_por_hectarea)


def tiempo_total_fumigacion_manual_por_hectarea():
    tiempo_fumigacion_manual_por_hectarea = 1
    return print('el tiempo empleado total de fumigar manualmente es de: ', tiempo_fumigacion_manual_por_hectarea, 'día')
