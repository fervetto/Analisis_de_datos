from abc import ABC, abstractmethod

class Dataset(ABC):
    def __init__(self, fuente):
        self.__fuente = fuente
        self.__datos = None
        
    @property
    def datos(self):
        """
        Propiedad que devuelve los datos cargados.
        """
        return self.__datos
    @datos.setter
    def datos(self, datos):
        """
        Propiedad que establece los datos cargados.
        """
        self.__datos = datos  

    @property
    def fuente(self):
        """
        Propiedad que devuelve la fuente de datos.
        """
        return self.__fuente
        
    @abstractmethod
    def cargar_datos(self):
        """
        Método abstracto para cargar datos desde la fuente.
        Debe ser implementado por las subclases.
        """
        pass        
    def cargar_datos(self):
        """
        Método abstracto para cargar datos desde la fuente.
        Debe ser implementado por las subclases.
        """
        pass

    def validar_datos(self):
        """
        Método abstracto para validar los datos cargados.
        Debe ser implementado por las subclases.
        """
        if self.datos.isnull().sum().sum() > 0:
            print("Los datos contienen valores nulos.")
            raise ValueError("No se han cargado datos.")

        if self.datos.isnull().values.any():
            print("Los datos contienen valores nulos.")
            raise ValueError("Los datos contienen valores nulos.")
        
        if self.datos.duplicated().values.any():
            print("Los datos contienen duplicados.")
            raise ValueError("Los datos contienen duplicados.")
        
        return True

        """
        Método abstracto para transformar los datos cargados.
        Debe ser implementado por las subclases.
        """
    def transformar_datos(self):
        if self.datos is not None:
            self.__datos.columns = self.datos.columns.str.lower().str.replace(' ', '_')
            self.__datos = self.datos.drop_duplicates()
            for col in self.datos.select_dtypes(include=['object']).columns:
                self.__datos[col] = self.datos[col].str.strip().str.lower()
            print("Datos transformados con éxito.")
        else:
            print('No se han cargado datos para transformar.')
            raise ValueError("No se han cargado datos para transformar.")


        pass

    def mostrar_resumen(self):
        """
        Método abstracto para mostrar un resumen de los datos.
        Debe ser implementado por las subclases.
        """
        
        pass
