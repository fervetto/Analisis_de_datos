from os import path
from domain.dataset_csv import DatasetCSV
# Ruta de CSV
csv_path = path.join(path.dirname(__file__), 'files/w_mean_prod.csv')

# Cargar y transformar datos
csv = DatasetCSV(csv_path)
csv.cargar_datos()
# Guardar en base de datos