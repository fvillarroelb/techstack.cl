# Importar librerías
import requests,textwrap,json,sys
import pandas as pd
sys.path.append('./redis')
from cache import RedisCache
from datetime import datetime
from datetime import date
from datetime import timedelta
from IPython.display import display

class BolsaComercio:


    def getDividend(self):
        redis = RedisCache()
        json_obj = redis.getValue('DIVIDENDOS')
        if json_obj is None:
            print('El objeto JSON-DIVIDENDOS está vacío')
            url = "https://www.bolsadesantiago.com/api/RV_ResumenMercado/getDividendos"

            payload = "{\"fec_pagoini\":\"2022-01-01\",\"fec_pagofin\":\"2022-12-31\",\"nemo\":\"\"}"
            headers = {
            'Cookie': 'BIGipCookie=000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000; __uzma=79e6e54d-0428-459d-87dc-38886db00d91; __uzmb=1663001672; __uzme=5773; BIGipCookie=000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000; f5avraaaaaaaaaaaaaaaa_session_=DKLHEFMBKHADHCDKCHGCDLMOPGNNFKGMGOFOBIJJKCKDOHJMODBJKBCCAOPGEDOPGFBDDBMNJDPMOGGGKMFACGLBPGOHFDPHBPDCHNMBPGEONNPHJPLDBNFCLFIAIGEI; BIGipServerPool-Push_HTML5_corporativa=684715681.20480.0000; __ssds=2; __ssuzjsr2=a9be0cd8e; __uzmaj2=7d3cd1fb-fd7a-4538-9e8a-154eb558831c; __uzmbj2=1663001673; gb-wbchtbt-uid=1663001674795; _ga=GA1.2.1805551646.1663001675; _gid=GA1.2.745080428.1663001675; _csrf=SHnFl6DaiW6u0B6u2zIEAKdd; __gads=ID=4d6cf2779c3a94b1:T=1663001687:S=ALNI_MZzoILu4slPkv0O5jiQuyIfdMtfFQ; __gpi=UID=000009644fd6d262:T=1663001687:RT=1663001687:S=ALNI_MbR93GQ2YGRn3kInX8TUEIU5v_QOA; _gat=1; __uzmcj2=400402251886; __uzmdj2=1663002427; BIGipServerPool-www.bolsadesantiago.com-HTML5_corporativa=735047329.20480.0000; __uzmc=1655310040454; __uzmd=1663002432; BIGipCookie=000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000; f5avraaaaaaaaaaaaaaaa_session_=FOHGNLLEDDPOHPPPOBDKGGNMFLBHGHFOGICKPFANNGEHOFPCAKPFNHLGPJMJJDOKJEDDDMDGHPIEPEKEOMGAGFGLEJMBLDJGMIBMNBJKINCGCBNKDFGBMBIMKEGEIFNM; BIGipServerPool-www.bolsadesantiago.com-HTML5_corporativa=718270113.20480.0000; __uzma=fe31de40-675b-48b6-b761-ff4a7a94c4e2; __uzmb=1663002361; __uzmc=4746610312280; __uzmd=1677500306; __uzme=9505; _csrf=q3bJQH8z97ajc55kn1uInjvW',
            'Origin': 'https://www.bolsadesantiago.com',
            'Referer': 'https://www.bolsadesantiago.com/dividendos',
            'sec-sh-ua': '"Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"',
            'sec-sh-platform': 'Windows',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27',
            'x-csrf-token': '9G8bMVxi-wPn9NrW2JM8AvOoJOdmpVpP0_IQ',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json;charset=UTF-8',
            'sec-ch-ua-mobile': '?0',
            'Authorization': 'Bearer JfVKcG3p-9q5QagRMW2gIZZuwzc3-6uqVHwI'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            # Convertir la cadena JSON en un objeto de Python
            json_obj = json.loads(response.text)
            # Convertir a cadena de texto
            json_string = json.dumps(json_obj)
            print('SAVE CACHE')
            redis.saveValue('DIVIDENDOS',json_string)
            return json_obj
        else:
            print('GET CACHE')
            return json.loads(json_obj)
       


    def getDividendDf(self):
        json_obj = self.getDividend()

        #jsonExcel = JsonToExcel()
        #TODO - problemas la llamar al methodo con un parametro 

        # Cargar el JSON en un DataFrame
        df = pd.DataFrame.from_dict(json_obj['listaResult'])
        #reordenar columnas
        df = df[['nemo', 'descrip_vc','val_acc', 'fec_lim', 'fec_pago', 'num_acc_ant', 'num_acc_der', 'num_acc_nue', 'pre_ant_vc', 'pre_ex_vc']]  # Reordenar las columnas del DataFrame
        df['fec_lim'] = pd.to_datetime(df['fec_lim'])
        # Cambiar los nombres de las columnas
        df = df.rename(columns={
            'descrip_vc': 'Descripción',
            'fec_lim': 'Fecha límite',
            'fec_pago': 'Fecha de pago',
            'nemo': 'Nemo',
            'num_acc_ant': 'Núm. de acciones ant.',
            'num_acc_der': 'Núm. de acciones der.',
            'num_acc_nue': 'Núm. de acciones nue.',
            'pre_ant_vc': 'Precio anterior',
            'pre_ex_vc': 'Precio de ejercicio',
            'val_acc': 'Valor de la acción'
        })

        # INTENTO
        #obtenemos la fecha de hoy
        hoy = pd.Timestamp(date.today())

        not_hoy = pd.Timestamp(date.today()) - pd.Timedelta(days=20)
        # creamos una función para resaltar las filas que cumplan la condición
        def highlight_rows(row):
            if (row['Fecha límite'] - hoy).days < 0:
                var =(row['Fecha límite'] - hoy).days
                return ['background-color: #993939'] * len(row)
            elif (row['Fecha límite'] - hoy).days >= 0 and (row['Fecha límite'] - hoy).days < 45 :
                print('es rojo')
                return ['background-color: #c0d449'] * len(row)
            else:
                return [''] * len(row)
     
        # Guardar el DataFrame en un archivo Excel
        df.to_excel('datos.xlsx', index=False, columns=[
            'Nemo',
            'Descripción',
            'Valor de la acción',
            'Precio anterior',
            'Precio de ejercicio',
            'Fecha límite',
            'Fecha de pago',
            'Núm. de acciones ant.',
            'Núm. de acciones der.',
            'Núm. de acciones nue.'
        ])

        # aplicamos la función a cada fila del DataFrame
        styled_df = df.style.apply(highlight_rows, axis=1)
        return styled_df





