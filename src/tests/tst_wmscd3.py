import codecs # Python standard library
codecs.encode("A strange character","utf-8")
from src.functions.Functions import Functions as Selenium
import unittest
import  allure

@allure.feature(u'Recibo Rápido')
@allure.story(u'002: Entrada de pedido Extranjero')
@allure.testcase(u"Caso de Prueba 004", u'https://trello.com/c/kRNA8SBg/1-caso-de-prueba-003-recibo-rapido')
@allure.severity(allure.severity_level.BLOCKER)
@allure.description(u"""Se realiza la entrada del pedido:</br>
se deben escanear los materiales e imprimir los shipping </br>
se recibe mercancía para todos los centros y T9</br>
 </br></br>""")

#AJUSTE DE INVENTARIO

class test_004(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar al WMS de CEDIS'):
            Selenium.abrir_navegador(self)

    def test_004(self):

        # CARGA EL JSON CON LOS VALORES DE LOS ID DE LA APP
        Selenium.get_json_file(self, "login")

        # ACCEDE A LAS KEYS (ENTIDADES) DEL JSON
        Selenium.get_entity(self, "Logo")

        Selenium.esperar_elemento(self, "Sesion")

        with allure.step(u'PASO 2: Ingresarmos Usuario'):
            Selenium.get_elements(self, "Usuario CD").send_keys(self.User)

        with allure.step(u'PASO 3: Ingresarmos Contraseña'):
            Selenium.get_elements(self, "Clave").send_keys(self.Pass)

        # BOTÓN INGRESAR
        with allure.step(u'PASO 4: Ingresamos al sistema'):
            Selenium.get_elements(self, "Ingresar").click()
            Selenium.esperar(self)

        # CARGA EL JSON CON LOS VALORES DE LOS ID DE LA APP
        Selenium.get_json_file(self, "ajustes")

        Selenium.page_has_loaded(self)

        # GESTIÓN DE AUDITORIA - AJUSTE DE INVENTARIO
        Selenium.new_window(self, self.AjusteInventario)
        Selenium.switch_to_windows_name(self, "Ajuste de Inventario")
        Selenium.get_entity(self, "Titulo")
        Selenium.get_elements(self, "Shalom").click()
        assert Selenium.get_text(self, "Titulo") == "Cargar ajuste"
        Selenium.esperar(self)
        Selenium.page_has_loaded(self)

        #TIPO DE AJUSTE
        Selenium.send_especific_keys(self,"Tipos","Enter")
        Selenium.get_elements(self, "Tipos").click()
        Selenium.get_elements(self, "Tipos").send_keys(self.Ajuste1)
        Selenium.esperar(self)

        #SELECCIONAR CSV
        Selenium.get_elements(self, "Seleccionar CSV").send_keys("C:\\fakepath\\ajuste_inventario (7).csv")

        ##GUARDAR CAPTURA
        Selenium.capturar_pantalla(self, "Bto-CEDIS")
        Selenium.esperar(self)


        Selenium.switch_to_windows_name(self, "Principal")
        Selenium.esperar(self)

    def tearDown(self):

        Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
