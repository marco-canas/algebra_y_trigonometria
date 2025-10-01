def crear_lista_estudiantes(ubicacion_lista):
    """
    """
    import pandas as pd     
    grupo_df = pd.read_csv(ubicacion_lista, sep = ';') 
    # cuando el .csv file proviene de un .xlsx file, debe utilizarse sep = ';'
    lista_estudiantes = list(grupo_df.nombre.values)
    return lista_estudiantes

#llamar a lista o tomar registro de asistencia a clase
def llamar_estudiantes_a_participar(lista):
    import numpy as np 
    from random import choice
    if len(lista) != 0:
        estudiante = choice(lista)
        lista.remove(estudiante)
        return print(estudiante)
    else:
        print('Todos los estudiantes han participado.\n \
               Muchas gracias y Felicitaciones')

ubicacion_lista='https://raw.githubusercontent.com/marco-canas/groups_list/main/1_algebra.csv'        
