from os import path
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetExcel
from domain.dataset_api import DatasetAPI
# Ruta de CSV
csv_path = path.join(path.dirname(__file__), 'files/w_mean_prod.csv')
# Ruta de Excel
excel_path = path.join(path.dirname(__file__), 'files/w_mean_prod.xlsx')

# Cargar y transformar datos
csv = DatasetCSV(csv_path)
csv.cargar_datos()

excel= DatasetExcel(excel_path)
excel.cargar_datos()


# Cargar datos desde una API
api = DatasetAPI('https://apis.datos.gob.ar/georef/api/provincias')
api.cargar_datos()




# Transformar datos 
# Guardar en base de datos