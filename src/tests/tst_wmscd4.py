
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedTagNameException

### PRUEBA DE RECIBO NACIONAL CEDIS

class test_cd04(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.USUARIO = "6334"
        self.CLAVE = "titan123"
        self.PEDIDO = "4500144619"
        self.EAN= "2040000639167"
        self.CANTIDAD = 8
        self.UMP = round(self.CANTIDAD / 2)
        self.IMPRESORAZEBRA = "Epson test"
        self.IMPRESORACOLOR = "Isla07"

    def test_cd04(self):
        # INGRESO AL WMS DE CEDIS
        self.driver.get("https://qa-cedis-front.titan.com.pa/seguridad/login")

        # COLOCAR USUARIO
        self.driver.find_element(By.XPATH, "//*[@id='nro_personal']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='nro_personal']").send_keys(self.USUARIO)

        # COLOCAR CONTRAEÑA
        self.driver.find_element(By.XPATH, "//*[@id='password']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(self.CLAVE)

        # BOTÓN INGRESAR
        self.driver.find_element(By.XPATH,"/html/body/app-root/block-ui/main/div[3]/div/app-login/div/div/div/div[2]/form/div[3]/button").click()
        time.sleep(5)

        # GESTIÓN DE RECIBO
        self.driver.find_element(By.XPATH,
                                 "/html/body/app-root/block-ui/main/div[3]/div/app-inicio/div/div[2]/div/div[6]/a/div").click()
        time.sleep(3)

        # RECIBO NACIONAL
        self.driver.find_element(By.XPATH,
                                 "/html/body/app-root/block-ui/main/div[3]/div/app-inicio/div/div[2]/div/div[11]/a/div").click()

        # INGRESE NÚMERO DE PEDIDO
        self.driver.find_element(By.XPATH,"//*[@id='Pedido']").send_keys(self.PEDIDO)
        self.driver.find_element(By.XPATH, "//*[@id='Pedido']").send_keys(Keys.ENTER)
        time.sleep(3)

        #INGRESE EL EAN
        self.driver.find_element(By.XPATH,"//*[@id='Código EAN']").send_keys(self.EAN)
        self.driver.find_element(By.XPATH, "//*[@id='Código EAN']").send_keys(Keys.ENTER)
        time.sleep(3)

        # INGRESE LA CANTIDAD A RECIBIR
        self.driver.find_element(By.XPATH, "//*[@id='cantidad_recibida']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='cantidad_recibida']").send_keys(self.CANTIDAD)
        self.driver.find_element(By.XPATH, "//*[@id='cantidad_recibida']").send_keys(Keys.ENTER)

        # INGRESE UNIDAD DE EMPAQUE
        self.driver.find_element(By.XPATH, "//*[@id='unidEmpaque']").send_keys(self.UMP)
        self.driver.find_element(By.XPATH, "//*[@id='unidEmpaque']").send_keys(Keys.ENTER)
        time.sleep(3)

        # GUARDAR
        self.driver.find_element(By.XPATH,
                                    "/html/body/ngb-modal-window/div/div/div/div[2]/div[2]/button[1]").click()
        time.sleep(3)

        # IMPRIMIR
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Imprimir')]").click()
        time.sleep(3)

        # SELECCIONE IMPRESORAS
        self.driver.find_element(By.XPATH, "//*[@id='impresoraSinFoto']/div/div/div[2]/input").send_keys(self.IMPRESORAZEBRA)
        self.driver.find_element(By.XPATH, "//*[@id='impresoraSinFoto']/div/div/div[2]/input").send_keys(Keys.ENTER)
        time.sleep(3)

        # ACEPTAR
        self.driver.find_element(By.XPATH,
                                 "/html/body/ngb-modal-window/div/div/div/div[2]/form/div[3]/button[1]").click()
        time.sleep(5)

        #MODAL CERRAR
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Cerrar')]").click()
        time.sleep(5)

        # GESTIÓN DE RECIBO
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Gestión de Recibo')]").click()

        # LISTADO DE BULTOS POR PEDIDO
        self.driver.find_element(By.XPATH,
                                 "//body/app-root[1]/block-ui[1]/main[1]/div[3]/div[1]/app-inicio[1]/div[1]/div[2]/div[1]/div[3]/a[1]/div[1]").click()
        time.sleep(15)

        # FILTRO DE PEDIDO
        self.driver.find_element(By.XPATH, "//thead/tr[2]/th[2]/input[1]").send_keys(self.PEDIDO)
        self.driver.find_element(By.XPATH, "//thead/tr[2]/th[2]/input[1]").send_keys(Keys.ENTER)
        time.sleep(10)

        # FILTRO DE MATERIAL
        self.driver.find_element(By.XPATH, "//thead/tr[2]/th[7]/input[1]").send_keys(self.EAN)
        self.driver.find_element(By.XPATH, "//thead/tr[2]/th[7]/input[1]").send_keys(Keys.ENTER)
        time.sleep(10)

        # GUARDAR IMAGEN
        title = "lista_bultos"
        tupla = time.localtime()
        ticks = time.strftime("%d%m%y-%H%M%S", tupla)
        self.driver.get_screenshot_as_file(f"../Data/Capturas/{title}-{ticks}.png")

        # GESTIÓN DE RECIBO
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Gestión de Recibo')]").click()
        time.sleep(3)

        # RECIBO NACIONAL
        self.driver.find_element(By.XPATH,
                                 "/html/body/app-root/block-ui/main/div[3]/div/app-inicio/div/div[2]/div/div[11]/a/div").click()
        time.sleep(3)

        # INGRESE NÚMERO DE PEDIDO
        self.driver.find_element(By.XPATH, "//*[@id='Pedido']").send_keys(self.PEDIDO)
        self.driver.find_element(By.XPATH, "//*[@id='Pedido']").send_keys(Keys.ENTER)
        time.sleep(3)

        # INGRESA A LA PESTAÑA DE PREPACK
        self.driver.find_element(By.XPATH, "//*[@id='pulmon']").click()
        time.sleep(10)

        ## SELECCIONAR MATERIALES
        self.driver.find_element(By.XPATH, "//thead/tr[1]/th[1]/input[1]").click()
        time.sleep(10)

        ## PASAR A PULMÓN
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Pasar a Pulmón')]").click()
        time.sleep(3)

        ## GUARDAR
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Guardar')]").click()
        time.sleep(6)

        # GUARDAR IMAGEN
        title = "pase_pulmon"
        tupla = time.localtime()
        ticks = time.strftime("%m%d%y-%H%M%S", tupla)
        self.driver.get_screenshot_as_file(f"../Data/Capturas/{title}-{ticks}.png")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
