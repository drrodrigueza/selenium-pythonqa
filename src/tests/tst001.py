# -*- coding: utf-8 -*-
from src.functions.Functions import Functions as Selenium
import unittest
import allure

@allure.feature(u'Creación de Usuario')
@allure.story(u'001: Error al crear un usuario')
@allure.testcase(u"Caso de Prueba 001", u'https://trello.com/c/iieoaKfU/2-caso-de-prueba-001-crear-de-usuario')
@allure.severity(allure.severity_level.BLOCKER)
@allure.description(u"""Se realiza la creación del usuario:</br>
el usuario a crear ya existe en el sistema </br>
debe mostrar el error que no se puede crear el usuario</br>
 </br></br>""")

#CREACIÓN DE USUARIO - WMS DE TIENDAS

class test_001(Selenium, unittest.TestCase):

    def setUp(self):
        with allure.step(u'PASO 1: Ingresar al WMS de Tiendas'):
            Selenium.abrir_navegador(self)

    def test_001(self):

        #CARGA EL JSON CON LOS VALORES DE LOS ID DE LA APP
        Selenium.get_json_file(self, "login")

        #ACCEDE A LAS KEYS (ENTIDADES) DEL JSON
        Selenium.get_entity(self, "Logo")

        assert Selenium.get_text(self, "Titulo") == "WMS Bodegas de Tiendas"

        Selenium.esperar_elemento(self, "Sesion")

        with allure.step(u'PASO 2: Ingresamos Usuario'):
         Selenium.get_elements(self,"Usuario TDA").send_keys(self.User)

        with allure.step(u'PASO 3: Ingresamos Contraseña'):
            Selenium.get_elements(self, "Clave").send_keys(self.Pass)
        with allure.step(u'PASO 4: Ingresamos al sistema'):
            Selenium.get_elements(self, "Ingresar").click()

        Selenium.esperar(self)

        with allure.step(u'PASO 5: Ingresamos a la creación de usuario'):
            Selenium.cerrar_window(self, "https://qa-tiendas-frontend.titan.com.pa/seguridad/usuario/crear")

            Selenium.switch_to_windows_name(self, "Gestión de Seguridad")
            Selenium.page_has_loaded(self, )
            Selenium.esperar(self)

        # CARGA EL JSON CON LOS VALORES DE LOS ID DE LA APP
        Selenium.get_json_file(self, "creausuario")

        assert Selenium.get_text(self, "Titulo") == "WMS Bodegas de Tiendas"

        Selenium.esperar_elemento(self, "Crear Usuario")
        with allure.step(u'PASO 5: Ingresamos a la creación de usuario'):
            Selenium.get_elements(self, "Num Personal").send_keys(self.User)
            Selenium.get_elements(self, "Nom User").send_keys(self.User)

            Selenium.get_elements(self, "Nombre").send_keys(self.NOMBRE)
            Selenium.get_elements(self, "Apellido").send_keys(self.APELLIDO)

            Selenium.get_elements(self, "Roles").send_keys(self.ROL1)
            Selenium.send_especific_keys(self,"Roles","Enter")
            Selenium.get_elements(self, "Roles").send_keys(self.ROL2)
            Selenium.send_especific_keys(self, "Roles", "Enter")

            Selenium.get_elements(self, "Tiendas").send_keys(self.TIENDA1)
            Selenium.send_especific_keys(self, "Tiendas", "Enter")
            Selenium.get_elements(self, "Tiendas").send_keys(self.TIENDA2)
            Selenium.send_especific_keys(self, "Tiendas", "Enter")

            Selenium.get_elements(self, "Departamentos").send_keys(self.DEPARTAMENTO1)
            Selenium.send_especific_keys(self, "Departamentos", "Enter")
            Selenium.get_elements(self, "Departamentos").send_keys(self.DEPARTAMENTO2)
            Selenium.send_especific_keys(self, "Departamentos", "Enter")

            Selenium.get_elements(self, "Clave").send_keys(self.Pass)
            Selenium.get_elements(self, "Repetir").send_keys(self.Pass)

            Selenium.esperar(self)

        Selenium.get_elements(self, "Guardar").click()
        Selenium.esperar(self)

        verificar = Selenium.get_text (self, "Mensaje")

        #assert verificar == True, "Usuario Creado"

        if verificar == True:
            unittest.TestCase.skipTest(self, "El usuario ya existe")

        Selenium.capturar_pantalla(self, "Usuario")
        Selenium.esperar(self)


        Selenium.switch_to_windows_name(self, "Principal")
        Selenium.esperar(self)


    def tearDown(self):
        Selenium.tearDown(self)

    if __name__ == '__main__':
        unittest.main()
