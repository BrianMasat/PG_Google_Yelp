import schedule
import time
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests as rq

def run_etl():

    url_one = 'https://es.wikipedia.org/wiki/Anexo:Estados_de_los_Estados_Unidos_por_PIB'
    page_one = rq.get(url_one).text


    # Parseamos el html utilizando BeautifulSoup
    soup_one = bs(page_one, 'html.parser')
    table_one = soup_one.find('table')


    # Creamos un DataFrame vacio
    df_pbi = pd.DataFrame(columns=['estados', 'PBI (millones de $)', 'PBI nacional (% del total)', 'poblacion (millones)', 'PBI per capita ($)', 'ranking nacional'])


    # Obtenemos las filas de la tabla
    for row in table_one.find_all('tr')[1:]:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]

        if len(cols) >= 5:
            estados = cols[0]
            pbi_millones = cols[1]
            porcentaje_pbi = cols[2]
            poblacion = cols[3]
            pbi_per_capita = cols[4]
            ranking = cols[5]

            row_data = {'estados': estados, 'PBI (millones de $)': pbi_millones, 'PBI nacional (% del total)': porcentaje_pbi,
                        'poblacion (millones)': poblacion, 'PBI per capita ($)': pbi_per_capita, 'ranking nacional': ranking}
            df_pbi = pd.concat([df_pbi, pd.DataFrame([row_data])])


    df_pbi = df_pbi.iloc[1:]
    df_pbi


# Programa la ejecución mensualmente a una hora específica (por ejemplo, a las 2 AM)
schedule.every().month.at("00:00").do(run_etl)

while True:
    schedule.run_pending()
    time.sleep(1)