#Es necesario importar las depencendias necesarias
from datetime import datetime
from datetime import timedelta

class Dividendos():
#no se usa nada de esta clase
    #deberia ir esto en otra clase solo para dividends
    def color_negative_red_value(val):
        color = 'red' if val < 0 else 'black'
        return 'color: %s' % color


    def color_negative_red_date(s, threshold):
        #Día actual
        today = date.today()
        #Fecha actual
        now = datetime.now()

        #Sumar dos días a la fecha actual
        new_date = now + timedelta(days=10)
        print(new_date)

        #Comparación
        if now < new_date:
            print("La fecha actual es menor que la nueva fecha")
            print(today)
            print(now)
            color = 'red' if val < 0 else 'black'
        
        return ['background-color: red' if v > threshold else '' for v in s] 