# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
import unittest
import allure

@allure.feature(u'Recibo Rápido')
@allure.story(u'005: Entrada de pedido Extranjero')
@allure.testcase(u"Caso de Prueba 002", u'https://trello.com/c/kRNA8SBg/1-caso-de-prueba-002')
@allure.severity(allure.severity_level.BLOCKER)
@allure.description(u"""Se realiza la entrada del pedido:</br>
se deben escanear los materiales e imprimir los shipping </br>
 </br></br>""")

class test_005(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar al WMS de CEDIS'):
            Selenium.abrir_navegador(self)

    def test_005(self):
        # CARGA EL JSON CON LOS VALORES DE LOS ID DE LA APP
        Selenium.get_json_file(self, "login")

        # ACCEDE A LAS KEYS (ENTIDADES) DEL JSON
        Selenium.get_entity(self, "Logo")

        Selenium.esperar_elemento(self, "Sesion")

        with allure.step(u'PASO 2: Ingresamos Usuario'):
            Selenium.get_elements(self, "Usuario CD").send_keys(self.User)

        with allure.step(u'PASO 3: Ingresarmos Contraseña'):
            Selenium.get_elements(self, "Clave").send_keys(self.Pass)

        # BOTÓN INGRESAR
        with allure.step(u'PASO 4: Ingresarmos al sistema'):
            Selenium.get_elements(self, "Ingresar").click()
            Selenium.esperar(self)

        ##GUARDAR CAPTURA
        with allure.step(u'PASO 5: GUARDAR CAPTURA'):
            Selenium.captura(self, "INICIO")
            Selenium.esperar(self)

    def tearDown(self):
        with allure.step(u'PASO 6: Cerramos el navegador'):
            Selenium.tearDown(self)

    if __name__ == '__main__':
        unittest.main()
