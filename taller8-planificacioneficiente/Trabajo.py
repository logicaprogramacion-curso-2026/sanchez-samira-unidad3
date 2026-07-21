class docente_dao:
    def __init__(self, db):
        self.db = db

    def crear_tabla(self):
        self.db.cursor.execute('''
CREATE TABLE docente
                               ''')