import sqlite3

class database:
    def __init__(self,
                 db_name="planificacdoreficiente.db"):
        self.conn = sqlite3.connect(db_name)
        señf.cursor = self.conn.cursor()
        print("Conexion exitosa")

    def cerrar(self):
        self.conn.close()