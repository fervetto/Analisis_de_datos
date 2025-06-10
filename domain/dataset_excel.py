from domain.dataset import Dataset
import pandas as pd
class DatasetExcel(Dataset):
    """
    Clase que representa un conjunto de datos cargados desde un archivo Excel.
    Hereda de la clase Dataset.
    """
    def __init__(self, fuente):
        """
        Inicializa el conjunto de datos con la fuente proporcionada.
        """
        super().__init__(fuente)
        self.__datos = None
        
    def cargar_datos(self):
        try:
            # Cargar datos desde el archivo Excel
            df = pd.read_excel(self.fuente)
            self.datos = df
            print(f"Datos cargados desde {self.fuente} con éxito.")
            if self.validar_datos():
                print("Datos validados con éxito.")
                self.transformar_datos()
        except Exception as e:
            print(f"Error al cargar los datos desde el archivo Excel: {e}")
            raise
    