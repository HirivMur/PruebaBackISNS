import requests
import pandas as pd
import hashlib
import sqlite3
import json

def get_data(url_api):   
    req=requests.get(url_api)
    data=pd.DataFrame(req.json())[['name','languages','population','subregion']]
    data = data[data['subregion'] == "South America"]
    
    names=[]
    names_sha1=[]

    for n in data['name']:
        names.append(n['common'])
        dato=n['common']
        names_sha1.append(hashlib.sha1(dato.encode('utf-8')).hexdigest())

    names=pd.DataFrame(names,columns = ['Name'])
    names_sha1=pd.DataFrame(names_sha1,columns = ['Name SHA1'])
  
    languages=[]
    for lan in data['languages']:
        languages_list=[]
        for item in lan:
            languages_list.append(lan[item])
        languages.append({"Language":",".join(languages_list)})

    languages=pd.DataFrame(languages,columns = ['Language'] )

    population=[]
    for p in data['population']:
        population.append(p)

    population=pd.DataFrame(population,columns = ['population'] )
    result = pd.concat([names,languages, population,names_sha1], axis=1)
    
    return result

def save_db(data,name_table):
    con = sqlite3.connect('prueba.db')
    data.to_sql(name_table, con, if_exists="replace")
    db = con.cursor()
    rows = db.execute("SELECT * from '%s' order by population" % name_table).fetchall()
    con.close()
    return rows
    
def export_json(data, name_file):
    json_data = json.dumps(data)
    with open(name_file+'.json', 'w') as the_file:
        the_file.write(json_data)

