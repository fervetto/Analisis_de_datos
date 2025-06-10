import sqlite3
import pandas as pd

class DataSaver:
    """
    Clase para guardar datos en una base de datos SQLite.
    """
    def __init__(self, db_name):
        """
        Inicializa la conexión a la base de datos SQLite.
        """
        self.__db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
    
    def guardar_datos(self, df, table_name):
        """
        Guarda un DataFrame en una tabla de la base de datos.
        
        :param df: DataFrame a guardar.
        :param table_name: Nombre de la tabla donde se guardarán los datos.
        """
        if df is None or df.empty:
            print("El DataFrame está vacío o no se ha cargado correctamente.")
            return
        
        if  not isinstance(df, pd.DataFrame):
            print("El objeto proporcionado no es un DataFrame de pandas. Se recibe un objeto de tipo:", type(df))
            return
    
        try:
            df.to_sql(table_name, self.conn, if_exists='replace', index=False)
            print(f"Datos guardados en la tabla '{table_name}' con éxito.")
            
        except Exception as e:
            print(f"Error al guardar los datos: {e}")
    
        self.conn.close()

