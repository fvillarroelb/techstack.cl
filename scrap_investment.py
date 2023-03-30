# Importar librerías
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,os
from selenium import webdriver
from PIL import Image
from io import BytesIO

class ScrapInvestment:


    def ratios(self):
# Realizar solicitud HTTP a la página web
        nemo = 'nemo_request'
        url = 'https://www.investing.com/equities/vapores-ratios'



        # configuración del navegador
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')  # modo sin ventana

        chromedriver = "cron-dividend-ipsa\chrome"
        os.environ["webdriver.chrome.driver"] = chromedriver
        # inicializar el driver de Chrome
        driver = webdriver.Chrome(chromedriver, options=options)
        # navegar a la página de Vapores
        driver.get(url)
        # esperar a que se cargue la página y aceptar las cookies
        wait = WebDriverWait(driver, 10)

        # Imprimir imagen
        #printScreen(driver.get_screenshot_as_png())

        # Esperar a que la tabla se cargue
        
        tabla = driver.find_element(By.XPATH, "//div[@id='rrtable_wrapper']/table")

        # Obtener el HTML de la tabla
        tabla_html = tabla.get_property("outerHTML")


        # Cerrar el navegador
        driver.quit()
        return print(tabla_html)



def printScreen(screen):
        contador = 1
        bytes_io = BytesIO()
        bytes_io.write(screen)

        # Crear instancia de la clase Image utilizando el objeto BytesIO
        imagen = Image.open(bytes_io)

        # Guardar la imagen como PNG
        imagen.save('screenshot/mi_imagen_guardada_'+str(contador)+'.png', 'PNG')


