# -*- coding: utf-8 -*-
import pytest
import unittest
import os
from behave import *
from selenium.webdriver.common.keys import Keys
from functions.Functions import Functions as Selenium
from functions.Inicializar import Inicializar

use_step_matcher("re")

class StepsDefinitions(Inicializar):

    @given("Abrir la aplicacion")
    def step_impl(self):
        Selenium.abrir_navegador(self)
        Selenium.page_has_loaded(self)

    @given("Inicializo en la URL (.*)")
    def step_impl(self, URL):
        Selenium.abrir_navegador(self, URL=URL)

    @given("Abro la aplicacion con el navegador (.*)")
    def step_impl(self, navegador):
        Selenium.abrir_navegador(self, navegador=navegador)

    @then("cierro la aplicación")
    def step_impl(self):
        Selenium.tearDown(self)

    @step("Cargo el DOM de la aplicación: (.*)")
    def step_impl(self, DOM):
        Selenium.get_json_file(self, DOM)

    @step("En el campo (.*) escribo (.*)")
    def step_impl(self, locator, text):
        Selenium.esperar_elemento(self, locator)
        text = Selenium.ReplaceWithContextValues(self, text)
        Selenium.get_elements(self, locator).send_keys(text)

    @step("Capturo pantalla (.*)")
    def step_impl(self, descripcion):
        Selenium.captura(self, descripcion)

    @step("Tomar captura (.*)")
    def step_impl(self, Captura):
        Selenium.capturar_pantalla(self, Captura)

    @step("le doy click en (.*)")
    def step_impl(self, element):
        Selenium.esperar_elemento(self, element)
        Selenium.get_elements(self, element).click()

    @step("esperamos")
    def step_impl(self):
        Selenium.esperar(self)

    @step("Ingresamos a la (.*)")
    def step_impl(self, URL):
        Selenium.new_window(self, URL="https://qa-tiendas-frontend.titan.com.pa/seguridad/usuario/crear")
        Selenium.switch_to_windows_name(self, "Gestión de Seguridad")

    @step("En el campo (.*) ingresamos (.*)")
    def step_impl(self, locator, text):
        Selenium.esperar_elemento(self, locator)
        text = Selenium.ReplaceWithContextValues(self, text)
        Selenium.get_elements(self, locator).send_keys(text)
        Selenium.send_especific_keys(self, locator, "Enter")

    @step("validamos el (.*) de (.*)")
    def step_impl(self, locator, text):
        Selenium.esperar_elemento(self, locator)
        Selenium.assert_text(self, locator, "No se pudo crear usuario")


    @step("Entramos a la Gestion de (.*)")
    def step_impl(self, URL):
        Selenium.new_window(self, URL="https://qa-cedis-front.titan.com.pa/seguridad/usuario/crear")
        Selenium.switch_to_windows_name(self, "Crear Usuario")


    @step("Se guarda el dato del (.*)")
    def step_impl(self, text):
        text = Selenium.ReplaceWithContextValues(self, text)
        Selenium.create_variable_scenary(self,text, Selenium.leer_celda(self, text))


    @step("Ingresamos a (.*)")
    def step_impl(self, text):
        text = Selenium.ReplaceWithContextValues(self, text)
        Selenium.new_window(self, URL=text)
        Selenium.switch_to_windows_name(self, text)
        Selenium.page_has_loaded(self)


    @step("En el campo (.*) escaneamos/ingresamos (.*)")
    def step_impl(self, elemento, text):
        text = Selenium.ReplaceWithContextValues(self, text)
        Selenium.create_variable_scenary(self, text, Selenium.leer_celda(self, text))
        text2 = Selenium.get_variable_scenary(self, text)
        Selenium.get_elements(self, elemento).clear()
        Selenium.get_elements(self, elemento).send_keys(text2)
        Selenium.send_especific_keys(self, elemento, "Enter")


    @step("selecciono (.*)")
    def step_impl(self, elemento):
        Selenium.send_especific_keys(self, elemento, "Enter")


    @step("esperamos el elemento (.*)")
    def step_impl(self, elemento):
        Selenium.esperar_elemento(self, elemento)

    @step("cargamos el archivo (.*)")
    def step_impl(self, entity):
        Selenium.esperar_elemento(self, entity)
        basedir = os.path.abspath(os.path.join(__file__, "../.."))
        CSV = "C:\Python310_SeleniumFramework\src\Data/ajuste_inventario.csv"
        Selenium.get_elements(self, entity).send_keys(CSV)
        Selenium.send_especific_keys(self, entity, "Enter")

    @step("En el campo (.*) agregamos/escaneamos (.*)")
    def step_impl(self, elemento, text):
        Selenium.esperar_elemento(self, elemento)
        text = Selenium.ReplaceWithContextValues(self, text)
        Selenium.create_variable_scenary(self, text, Selenium.leer_celda(self, text))
        text2 = Selenium.get_variable_scenary(self, text)
        Selenium.get_elements(self, elemento).clear()
        Selenium.get_elements(self, elemento).send_keys(text2)



