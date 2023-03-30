import json
import pandas as pd


class JsonToExcel:


    def convertToExcel(json_file):
        # Cargar el JSON en un DataFrame
        df = pd.DataFrame.from_dict(json_obj['listaResult'])
        #reordenar columnas
        df = df[['nemo', 'descrip_vc','val_acc', 'fec_lim', 'fec_pago', 'num_acc_ant', 'num_acc_der', 'num_acc_nue', 'pre_ant_vc', 'pre_ex_vc']]  # Reordenar las columnas del DataFrame
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