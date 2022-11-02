import codecs # Python standard library
codecs.encode("A strange character","utf-8")
from src.functions.Functions import Functions as Selenium
import unittest
import  allure

@allure.feature(u'Recibo Rápido')
@allure.story(u'002: Entrada de pedido Extranjero')
@allure.testcase(u"Caso de Prueba 003", u'https://trello.com/c/kRNA8SBg/1-caso-de-prueba-003-recibo-rapido')
@allure.severity(allure.severity_level.BLOCKER)
@allure.description(u"""Se realiza la entrada del pedido:</br>
se deben escanear los materiales e imprimir los shipping </br>
se recibe mercancía para todos los centros y T9</br>
 </br></br>""")

#RECIBO RÁPIDO - NO PREPACK

class test_003(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar al WMS de CEDIS'):
            Selenium.abrir_navegador(self)

    def test_003(self):

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
        Selenium.get_json_file(self, "recibomercancia")

        Selenium.page_has_loaded(self)

        #GUARDAR NÚMERO DE PEDIDO DESDE EL EXCEL
        with allure.step(u'PASO 5: Se extrae y guarda el pedido a trabajar'):
            Selenium.create_variable_scenary(self,"Pedido", Selenium.leer_celda(self, self.PEDIDO))

        Selenium.textDateEnvironmentReplace(self, "today")

        # LISTADO DE MATERIALES

        ## GUARDAR EAN DESDE EL EXCEL
        with allure.step(u'PASO 6: Se extraen y guardan los materiales a recibir'):
            Selenium.create_variable_scenary(self, "EAN1", Selenium.leer_celda(self, self.EAN1))
            Selenium.create_variable_scenary(self, "EAN2", Selenium.leer_celda(self, self.EAN2))
            Selenium.create_variable_scenary(self, "EAN3", Selenium.leer_celda(self, self.EAN3))
            Selenium.create_variable_scenary(self, "EAN4", Selenium.leer_celda(self, self.EAN4))
            #Selenium.create_variable_scenary(self, "EAN5", Selenium.leer_celda(self, self.EAN5))
            Selenium.esperar(self)

        # GESTIÓN DE RECIBO - RECIBO RÁPIDO
        Selenium.new_window(self, self.ReciboRapido)
        Selenium.switch_to_windows_name(self, "Recibo Rápido")
        Selenium.get_entity(self, "Titulo")
        Selenium.get_elements(self, "Shalom").click()
        assert Selenium.get_text(self, "Titulo") == "Recibo Rápido"
        Selenium.page_has_loaded(self)
        #INGRESAR PEDDIO
        Selenium.esperar(self)
        with allure.step(u'PASO 6: Se ingresa el pedido'):
            Pedido = Selenium.get_variable_scenary(self, "Pedido")
            Selenium.get_elements(self, "PEDIDO").send_keys(Pedido)
            Selenium.send_especific_keys(self, "PEDIDO", "Enter")
        #ESCANEAR EAN'S
        with allure.step(u'PASO 7: Se escanean los materiales'):
            Ean1 = Selenium.get_variable_scenary(self, "EAN1")
            Selenium.get_elements(self, "EAN").send_keys(Ean1)
            Selenium.send_especific_keys(self, "EAN", "Enter")
            Selenium.esperar(self)
            Selenium.get_elements(self, "EAN").clear()
            Ean2 = Selenium.get_variable_scenary(self, "EAN2")
            Selenium.get_elements(self, "EAN").send_keys(Ean2)
            Selenium.send_especific_keys(self, "EAN", "Enter")
            Selenium.esperar(self)
            Ean3 = Selenium.get_variable_scenary(self, "EAN3")
            Selenium.get_elements(self, "EAN").send_keys(Ean3)
            Selenium.send_especific_keys(self, "EAN", "Enter")
            Selenium.esperar(self)
            Ean4 = Selenium.get_variable_scenary(self, "EAN4")
            Selenium.get_elements(self, "EAN").send_keys(Ean4)
            Selenium.send_especific_keys(self, "EAN", "Enter")
            Selenium.esperar(self)

        #IMPRIMIR SHIPPING
        with allure.step(u'PASO 8: Se imprimen los shipping'):
            Selenium.get_elements(self, "IMPRIMIR").click()
            Selenium.esperar(self)
            Selenium.get_elements(self, "IMPRESORA SIN FOTO").send_keys(self.IMPRESORAZEBRA)
            Selenium.send_especific_keys(self, "IMPRESORA SIN FOTO", "Enter")
            Selenium.esperar(self)
            Selenium.get_elements(self, "ACEPTAR").click()
            Selenium.esperar(self)
            Selenium.get_elements(self, "MODAL CERRAR").click()
            Selenium.esperar(self)
            Selenium.esperar(self)
        ##REFRESCAR
        Selenium.get_elements(self, "Refresh").click()
        Selenium.esperar(self)

        #IMPRIMIR SHIPPING CEDIS
        with allure.step(u'PASO 9: Se imprimen los shipping tipo CEDIS'):
            Selenium.get_elements(self, "IMPRIMIR CEDIS").click()
            Selenium.esperar(self)
            Selenium.get_elements(self, "IMPRESORA SIN FOTO").send_keys(self.IMPRESORAZEBRA)
            Selenium.send_especific_keys(self, "IMPRESORA SIN FOTO", "Enter")
            Selenium.get_elements(self, "ACEPTAR").click()
            Selenium.esperar(self)
            Selenium.get_elements(self, "MODAL CERRAR").click()

        ##GUARDAR CAPTURA
        with allure.step(u'PASO 10: Se toma captura de los materiales recibidos'):
            Selenium.captura(self, "ReciboRapido")
            Selenium.esperar(self)

        #LISTADO DE BULTOS POR PEDIDO
        Selenium.new_window(self, self.ListadoBultos)
        Selenium.switch_to_windows_name(self, "Listado de Bultos por Pedido")
        Selenium.get_elements(self, "Shalom").click()
        Selenium.esperar(self)

        # FILTRO DE PEDIDO
        Selenium.get_elements(self, "Filtro Pedido").send_keys(Pedido)
        Selenium.send_especific_keys(self, "Filtro Pedido", "Enter")

        #BULTOS DE TIENDAS
        with allure.step(u'PASO 11: Se toma captura de lista de bultos de tiendas'):
            Selenium.get_elements(self, "Bultos Tiendas").click()
            Selenium.esperar(self)
            ##GUARDAR CAPTURA
            Selenium.captura(self, "Bto-Tiendas")
            Selenium.esperar(self)

        # BULTOS DE CEDIS
        with allure.step(u'PASO 12: Se toma captura de lista de bultos de CEDIS'):
            Selenium.get_elements(self, "Bultos CEDIS").click()
            Selenium.esperar(self)
            ##GUARDAR CAPTURA
            Selenium.captura(self, "Bto-CEDIS")
            Selenium.esperar(self)

        with allure.step(u'PASO 12: Regresa a la pantalla principal'):
            Selenium.switch_to_windows_name(self, "Principal")
            Selenium.get_elements(self, "Shalom").click()
            Selenium.esperar(self)

    def tearDown(self):
        with allure.step(u'PASO 14: Cerramos el navegador'):
            Selenium.tearDown(self)


if __name__ == '__main__':
    unittest.main()
