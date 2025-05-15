from domain.dataset import Dataset
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
        
    