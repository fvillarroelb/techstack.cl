import requests, json,sys
import nodejs
import pandas as pd
sys.path.append('./bolsa-comercio')
from bolsa_comercio import BolsaComercio
from json_to_excel import JsonToExcel
from scrap_investment import ScrapInvestment
from flask import Flask, render_template
from my_strategy import MyStrategy
from joblib import dump, load
from dividendos import Dividendos

##init flask
app = Flask(__name__)


@app.route('/')
def index():
    bolsa_comercio = BolsaComercio()
    df = bolsa_comercio.getDividendDf()
    table = df.to_html()
    # Agregar el id a la tabla
    table = table.replace('<table', '<table id="table_dividendos"')
     

    # Imprime la cadena HTML
    #print(index)
    return render_template('index.html',tabla=table)

@app.route('/dividendos')
def hello():
    return 'Hello, World'


if __name__ == '__main__':
    app.run()
#scrap = ScrapInvestment()
#scrap.ratios()

