from domain.dataset import Dataset
import pandas as pd


class DatasetCSV(Dataset):
    """
    Clase que representa un conjunto de datos cargados desde un archivo CSV.
    Hereda de la clase Dataset.
    """
    def __init__(self, fuente):
        """
        Inicializa el conjunto de datos con la fuente proporcionada.
        """
    def cargar_datos(self):
        try:
            # Cargar datos desde el archivo CSV
            df = pd.read_csv(self.fuente)
            self.datos = df
            print(f"Datos cargados desde {self.fuente} con éxito.")
            if self.validar_datos():
                print("Datos validados con éxito.")
                # self.transformar_datos()
            
            # Validar datos
        except Exception as e:
            print(f"Error al cargar los datos desde el archivo CSV: {e}")
            raise
        