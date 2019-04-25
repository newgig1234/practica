# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona

import sqlite3 

def borrar_persona(id_persona):
    cursor = db.cursor()
    cSQL = 'DELETE FROM persona WHERE id_persona = ?'
    cursor.execute(cSQL, id_persona)
    db.commit()
    


@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()

el connect con la base deberia ir en crear tabla y el db.close en borrar tabla