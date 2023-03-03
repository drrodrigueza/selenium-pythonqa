import codecs # Python standard library
codecs.encode("A strange character","utf-8")
from functions.Functions import Functions as Selenium
import unittest
import  allure

@allure.feature(u'Recibo Rápido')
@allure.story(u'002: Entrada de pedido Extranjero')
@allure.testcase(u"Caso de Prueba 002", u'https://trello.com/c/kRNA8SBg/1-caso-de-prueba-002')
@allure.severity(allure.severity_level.BLOCKER)
@allure.description(u"""Se realiza la entrada del pedido:</br>
se deben escanear los materiales e imprimir los shipping </br>
 </br></br>""")

#RECIBO RÁPIDO - APLICA PREPACK

class test_002(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar al WMS de CEDIS'):
            Selenium.abrir_navegador(self)

    def test_002(self):

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
        with allure.step(u'PASO 4: Ingresarmos al sistema'):
            Selenium.get_elements(self, "Ingresar").click()
            Selenium.esperar(self)

        #EXTRAER MATERIALES
        # GESTIÓN DE RECIBO - DETALLE DE PEDIDO BUSCAR NÚMERO DE PEDIDO
        #Selenium.new_window(self, self.DetallePedido + self.UUIDPedido)
        #Selenium.switch_to_windows_name(self, "Consulta Pedidos Compra")
        #
        #Selenium.esperar(self)

        # CARGA EL JSON CON LOS VALORES DE LOS ID DE LA APP
        Selenium.get_json_file(self, "recibomercancia")

        #Selenium.get_entity(self, "Titulo")
        #assert Selenium.get_text(self, "Titulo") == "Consulta Pedidos Compra"
        #Selenium.save_variable_scenary(self, "Pedido Compra", "Pedido")
        Selenium.page_has_loaded(self)

        #GUARDAR NÚMERO DE PEDIDO DESDE EL EXCEL
        with allure.step(u'PASO 5: Se extrae y guarda el pedido a trabajar'):
            Selenium.create_variable_scenary(self,"Pedido", Selenium.leer_celda(self, self.PEDIDO))

        Selenium.textDateEnvironmentReplace(self, "today")

        # LISTADO DE MATERIALES
        #Selenium.get_select_elements(self, "Estatus Creado").select_by_visible_text ("Creado")
        #Selenium.esperar(self)
        #assert Selenium.get_text(self, "Estatus1") == "Creado"

        #Selenium.save_variable_scenary(self, "EAN Pedido1", "EAN1")
        #Selenium.save_variable_scenary(self, "Cantidad Pedido1", "CANTIDAD1")
        #Selenium.save_variable_scenary(self, "EAN Pedido2", "EAN2")
        #Selenium.save_variable_scenary(self, "Cantidad Pedido2", "CANTIDAD2")
        #Selenium.save_variable_scenary(self, "EAN Pedido3", "EAN3")
        #Selenium.save_variable_scenary(self, "Cantidad Pedido3", "CANTIDAD3")
        #Selenium.save_variable_scenary(self, "EAN Pedido4", "EAN4")
        #Selenium.save_variable_scenary(self, "Cantidad Pedido4", "CANTIDAD4")
        #Selenium.save_variable_scenary(self, "EAN Pedido5", "EAN5")
        #Selenium.save_variable_scenary(self, "Cantidad Pedido5", "CANTIDAD5")

        # GUARDAR EAN DESDE EL EXCEL
        with allure.step(u'PASO 6: Se extraen y guardan los materiales a recibir'):
            Selenium.create_variable_scenary(self, "EAN1", Selenium.leer_celda(self, self.EAN1))
            Selenium.create_variable_scenary(self, "EAN2", Selenium.leer_celda(self, self.EAN2))
            Selenium.create_variable_scenary(self, "EAN3", Selenium.leer_celda(self, self.EAN3))
            Selenium.create_variable_scenary(self, "EAN4", Selenium.leer_celda(self, self.EAN4))
            Selenium.create_variable_scenary(self, "EAN5", Selenium.leer_celda(self, self.EAN5))
            Selenium.esperar(self)

        # GESTIÓN DE RECIBO - RECIBO RÁPIDO
        Selenium.cerrar_window(self, self.ReciboRapido)
        Selenium.switch_to_windows_name(self, "Recibo Rápido")
        Selenium.get_entity(self, "Titulo")
        assert Selenium.get_text(self, "Titulo") == "Recibo Rápido"
        Selenium.page_has_loaded(self)
        #INGRESAR PEDDIO
        Selenium.esperar(self)
        with allure.step(u'PASO 6: Se ingresa el pedido'):
            Pedido = Selenium.get_variable_scenary(self, "Pedido")
        #Selenium.get_elements(self, "PEDIDO").send_keys(Selenium.leer_celda(self, self.PEDIDO))
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
            Ean5 = Selenium.get_variable_scenary(self, "EAN5")
            Selenium.get_elements(self, "EAN").send_keys(Ean5)
            Selenium.send_especific_keys(self, "EAN", "Enter")
            Selenium.esperar(self)

        #IMPRIMIR SHIPPING
        with allure.step(u'PASO 8: Se imprimen los shipping'):
            Selenium.get_elements(self, "IMPRIMIR").click()
            Selenium.esperar(self)
            Selenium.get_elements(self, "IMPRESORA SIN FOTO").send_keys(self.IMPRESORAZEBRA)
            Selenium.send_especific_keys(self, "IMPRESORA SIN FOTO", "Enter")
            Selenium.get_elements(self, "IMPRESORA CON FOTO").send_keys(self.IMPRESORAEPSON)
            Selenium.send_especific_keys(self, "IMPRESORA CON FOTO", "Enter")
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
        Selenium.get_elements(self, "IMPRIMIR CEDIS").click()
        Selenium.esperar(self)
        Selenium.get_elements(self, "IMPRESORA SIN FOTO").send_keys(self.IMPRESORAZEBRA)
        Selenium.send_especific_keys(self, "IMPRESORA SIN FOTO", "Enter")
        Selenium.get_elements(self, "ACEPTAR").click()
        Selenium.esperar(self)
        Selenium.get_elements(self, "MODAL CERRAR").click()

        #LISTADO DE BULTOS POR PEDIDO
        Selenium.cerrar_window(self, self.ListadoBultos)
        Selenium.switch_to_windows_name(self, "Listado de Bultos por Pedido")
        Selenium.esperar(self)

        #BULTOS DE TIENDAS
        Selenium.get_elements(self, "Bultos Tiendas").click()
        Selenium.esperar(self)
        ##GUARDAR CAPTURA
        Selenium.capturar_pantalla(self, "Bto-Tiendas")
        Selenium.esperar(self)

        # BULTOS DE CEDIS
        Selenium.get_elements(self, "Bultos CEDIS").click()
        Selenium.esperar(self)
        ##GUARDAR CAPTURA
        Selenium.capturar_pantalla(self, "Bto-CEDIS")
        Selenium.esperar(self)

        # BULTOS DE ENGANCHE
        Selenium.get_elements(self, "Bultos Enganche").click()
        Selenium.esperar(self)
        ##GUARDAR CAPTURA
        Selenium.capturar_pantalla(self, "Bto-Eng")
        Selenium.esperar(self)

        #PASE A PULMÓN
        Selenium.switch_to_windows_name(self, "Recibo Rápido")
        Selenium.esperar(self)

        ##CAMBIO A PESTAÑA PREPACK
        Selenium.get_elements(self, "Prepack").click()
        Selenium.esperar(self)

        ##SELECCIONAR MATERIALES
        Selenium.get_elements(self, "Seleccionar materiales").click()
        Selenium.esperar(self)

        ##PASAR A PULMÓN
        Selenium.get_elements(self, "Pasar a Pulmon").click()
        Selenium.esperar(self)

        ##GUARDAR
        Selenium.get_elements(self, "Guardar").click()
        Selenium.esperar(self)

        ##REFRESCAR
        Selenium.get_elements(self, "Refrescar").click()
        Selenium.esperar(self)

        ##GUARDAR CAPTURA
        Selenium.capturar_pantalla(self, "PULMON")
        Selenium.esperar(self)

        Selenium.switch_to_windows_name(self, "Principal")
        Selenium.esperar(self)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
