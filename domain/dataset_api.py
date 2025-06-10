import requests
import pandas as pd
from domain.dataset import Dataset

class DatasetAPI(Dataset):
    """
    Clase que representa un conjunto de datos cargados desde una API.
    Hereda de la clase Dataset.
    """
    def __init__(self, fuente):
        super().__init__(fuente)
        """
        Inicializa el conjunto de datos con la fuente proporcionada.
        """
    
    def cargar_datos(self):
        try:
            # Cargar datos desde la API
            response = requests.get(self.fuente)
            if response.status_code != 200:
                raise Exception(f"Error al acceder a la API: {response.status_code}")
            
            else:
                print(f"Acceso a la API exitoso: {self.fuente}")
                df = pd.json_normalize(response.json())
                def es_lista(col):  
                    """
                    Verifica si una columna es una lista.
                    """
                    return isinstance(col, list)
                
                def lista_a_string(col):
                    """
                    Convierte una lista a una cadena separada por comas.
                    """
                    if es_lista(col):
                        return ', '.join(map(str, col))

                # Verificar si alguna columna contiene listas
                for col in df.columns:
                    if df[col].apply(es_lista).any():
                        # Si la columna contiene listas, convertirlas a cadenas
                        df[col] = df[col].apply(lista_a_string)
                    else:
                        df[col] = df[col].astype(str).str.strip().str.lower()
                    
                self.datos = df
                print(self.datos)
                print("Datos cargados desde la API con éxito.")

                if self.validar_datos():
                    print("Datos validados correctamente.")
                    self.transformar_datos()
                else:
                    print("Los datos no son válidos.")
                    raise ValueError("Los datos no son válidos.")    
        except Exception as e:
            print(f"Error al cargar los datos desde la API: {e}")
            raise