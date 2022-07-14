from datetime import datetime
from prueba import get_data, save_db, export_json
import sqlite3

def main():
    inicio=datetime.now()

    #obtener datos y creación DataFrame
    data = get_data('https://restcountries.com/v3.1/subregion/ame')
    #guardar datos en la Base de datos 
    data_db = save_db(data,'south_america')
    #exportar los datos 
    export_json(data_db,'south_america')

    final=datetime.now()
    print("Tiempo de ejecución: "+str(final - inicio))

if __name__=="__main__":
    main()