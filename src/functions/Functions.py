# -*- coding= utf-8 -*-
import allure
import openpyxl
from functions.Inicializar import Inicializar
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, NoSuchWindowException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.ie.options import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as OpcionesChrome
from selenium.webdriver.edge.options import Options as OpcionesEdge
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pytest
import json
import time
import datetime
import re
import os
Scenario = {}
diaGlobal= time.strftime(Inicializar.DateFormat)  # formato aaaa/mm/dd
horaGlobal = time.strftime(Inicializar.HourFormat)  # formato 24 houras

class Functions(Inicializar):

    ##########################################################################
    ##############   -=_INICIALIZAR DRIVERS_=-   #############################
    ##########################################################################
    def abrir_navegador(self, URL=Inicializar.URL, navegador=Inicializar.NAVEGADOR):
        print("Directorio Base: " + Inicializar.basedir)
        self.ventanas = {}
        print("----------------")
        print(navegador)
        print("---------------")

        if navegador == ("EDGE"):
            self.driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            print(self.ventanas)
            return self.driver

        if navegador == ("CHROME"):
            options = OpcionesChrome()
            options.add_argument('start-maximized')
            self.driver = webdriver.Chrome(chrome_options=options, executable_path=ChromeDriverManager().install())
            self.driver.implicitly_wait(10)
            self.driver.get(URL)
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            print(self.ventanas)
            return self.driver

        if navegador == ("FIREFOX"):
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.driver.get(URL)
            self.ventanas = {'Principal': self.driver.window_handles[0]}
            return self.driver

    def tearDown(self):
        print("Se cerrará  el DRIVER")
        self.driver.quit()


    ##########################################################################
    ##############       -=_JSON     HANDLE _=-              #################
    ##########################################################################

    # CARGAMOS EL ARCHIVO JSON
    def get_json_file(self, file):
        json_path = Inicializar.Json + "/" + file + '.json'
        try:
            with open(json_path, "r") as read_file:
                self.json_strings = json.loads(read_file.read())
                print("get_json_file: "+ json_path)
                return self.json_strings
        except FileNotFoundError:
            self.json_strings = False
            pytest.skip(u"get_json_file: No se encontro el Archivo " + file)
            Functions.tearDown(self)

    # LEER CONTENIDO DEL JSON
    def get_entity(self, entity):
        if self.json_strings is False:
            print ("Define el DOM para esta prueba")
        else:
            try:
                self.json_ValueToFind = self.json_strings[entity]["ValueToFind"]
                self.json_GetFieldBy = self.json_strings[entity]["GetFieldBy"]
                return True

            except KeyError:
                pytest.skip(u"get_entity: No se encontro la key a la cual se hace referencia: " + entity)
                #self.driver.close()
                Functions.tearDown(self)
                return None

    ##########################################################################
    ##############     -=_BEHAVIOR DRIVEN TEST_=-            #################
    ##########################################################################
    # ACCESAR A LAS KEYS DEL JSON
    def get_elements(self, entity, MyTextElement = None):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element(By.ID, self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element(By.NAME, self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print (self.json_ValueToFind)
                    elements = self.driver.find_element(By.XPATH,self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)

                print("get_elements - " + self.json_GetFieldBy + ": " + self.json_ValueToFind)
                return elements

            except NoSuchElementException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
            except TimeoutException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)


    def get_text(self, entity, MyTextElement = None):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    elements = self.driver.find_element(By.ID, self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "name":
                    elements = self.driver.find_element(By.NAME, self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "xpath":
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print (self.json_ValueToFind)
                    elements = self.driver.find_element(By.XPATH, self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "link":
                    elements = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind)

                if self.json_GetFieldBy.lower() == "css":
                    elements = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind)

                print("get_text - " + self.json_GetFieldBy + ": " + self.json_ValueToFind)
                print("Text Value : " + elements.text)
                return elements.text

            except NoSuchElementException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)
            except TimeoutException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

    # CREAR STOP
    def esperar_elemento(self, locator, MyTextElement=None):
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            return print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.ID, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.NAME, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 20)
                    if MyTextElement is not None:
                        self.json_ValueToFind = self.json_ValueToFind.format(MyTextElement)
                        print(self.json_ValueToFind)

                        wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                        wait.until(EC.element_to_be_clickable((By.XPATH, self.json_ValueToFind)))
                        print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                        return True

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                    print(u"Esperar_Elemento: Se visualizo el elemento " + locator)
                    return True

            except TimeoutException:
                print(u"Esperar_Elemento: No presente " + locator)
                Functions.tearDown(self)
            except NoSuchElementException:
                print(u"Esperar_Elemento: No presente " + locator)
                Functions.tearDown(self)

    # SELECCIONAR DE LISTA DESPLEGABLE
    def get_select_elements(self, entity):
        Get_Entity = Functions.get_entity(self, entity)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    select = Select(self.driver.find_element(By.ID, self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "name":
                    select = Select(self.driver.find_element(By.NAME, self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "xpath":
                    select = Select(self.driver.find_element(By.XPATH, self.json_ValueToFind))

                if self.json_GetFieldBy.lower() == "link":
                    select = Select(self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind))

                print("get_select_elements - " +self.json_GetFieldBy + " :" + self.json_ValueToFind)
                return select

            # USO

            #       select by visible text  #       select_by_visible_text('Banana')

            #       select by value  #       select_by_value('1')

            except NoSuchElementException:
                print("No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

            except TimeoutException:
                print("No se encontró el elemento: " + self.json_ValueToFind)
                Functions.tearDown(self)

    # CAMBIO DE VENTANAS
    def switch_to_windows_name(self, ventana):
        if ventana in self.ventanas:
            self.driver.switch_to.window(self.ventanas[ventana])
            Functions.page_has_loaded(self)
            print ("volviendo a " + ventana + " : " + self.ventanas[ventana])
        else:
            self.nWindows = len(self.driver.window_handles) - 1
            self.ventanas[ventana] = self.driver.window_handles[int(self.nWindows)]
            self.driver.switch_to.window(self.ventanas[ventana])
            self.driver.maximize_window()
            print(self.ventanas)
            print ("Estas en " + ventana + " : " + self.ventanas[ventana])
            Functions.page_has_loaded(self)

    ######################   -=_JAVASCRIPT_=-   #############################
    ##########################################################################
    # NUEVA VENTANA
    def new_window(self, URL):
        self.driver.execute_script(f'''window.open("{URL}","_blank");''')
        Functions.page_has_loaded(self)

    def page_has_loaded(self):
        driver = self.driver
        print("Checking if {} page is loaded.".format(self.driver.current_url))
        page_state = driver.execute_script('return document.readyState;')
        yield
        WebDriverWait(driver, 30).until(lambda driver: page_state == 'complete')
        assert page_state == 'complete', "No se completo la carga"

    ##############   -=_Wait Elements_=-   #############################
    ##########################################################################
    def esperar(self, timeLoad=8):
        print ("Esperar: Inicia ("+str(timeLoad)+")")
        try:
                totalWait = 0
                while (totalWait < timeLoad):
                    #print("Cargando ... intento: " + str(totalWait))
                    time.sleep(1)
                    totalWait = totalWait + 1
                    #print(totalWait)
        finally:
            print ("Esperar: Carga Finalizada ... ")

    #ENVIAR TECLAS ESPECÍFICAS
    def send_especific_keys(self, element, key):
        if key == 'Enter':
            Functions.get_elements(self, element).send_keys(Keys.ENTER)
        if key == 'Tab':
            Functions.get_elements(self, element).send_keys(Keys.TAB)
        if key == 'Space':
            Functions.get_elements(self, element).send_keys(Keys.SPACE)
        time.sleep(3)

    def send_key_text(self, entity, text):
        Functions.get_elements(self, entity).clear()
        Functions.get_elements(self, entity).send_keys(text)

    def select_by_text(self, entity, text):
        Functions.get_select_elements(self, entity).select_by_visible_text(text)

 ##########################################################################
 #################   -=_VERIFICACION _=-                ###################
 ##########################################################################
    # Crear Step
    def check_element(self, locator):  # devuelve true o false
        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            try:
                if self.json_GetFieldBy.lower() == "id":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.ID, self.json_ValueToFind)))
                    print(u"check_element: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "name":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.NAME, self.json_ValueToFind)))
                    print(u"check_element: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "xpath":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.XPATH, self.json_ValueToFind)))
                    print(u"check_element: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "link":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.LINK, self.json_ValueToFind)))
                    print(u"check_element: Se visualizo el elemento " + locator)
                    return True

                if self.json_GetFieldBy.lower() == "css":
                    wait = WebDriverWait(self.driver, 20)
                    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                    print(u"check_element: Se visualizo el elemento " + locator)
                    return True

            except NoSuchElementException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                return False
            except TimeoutException:
                print("get_text: No se encontró el elemento: " + self.json_ValueToFind)
                return False

    def assert_text(self, locator, TEXTO):

        Get_Entity = Functions.get_entity(self, locator)

        if Get_Entity is None:
            print("No se encontro el valor en el Json definido")
        else:
            if self.json_GetFieldBy.lower() == "id":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.ID, self.json_ValueToFind)))
                ObjText = self.driver.find_element(By.ID, self.json_ValueToFind).text

            if self.json_GetFieldBy.lower() == "name":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.NAME, self.json_ValueToFind)))
                ObjText = self.driver.find_element(By.NAME, self.json_ValueToFind).text

            if self.json_GetFieldBy.lower() == "xpath":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.XPATH, self.json_ValueToFind)))
                ObjText = self.driver.find_element(By.XPATH, self.json_ValueToFind).text

            if self.json_GetFieldBy.lower() == "link":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, self.json_ValueToFind)))
                ObjText = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.json_ValueToFind).text

            if self.json_GetFieldBy.lower() == "css":
                wait = WebDriverWait(self.driver, 15)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.json_ValueToFind)))
                ObjText = self.driver.find_element(By.CSS_SELECTOR, self.json_ValueToFind).text

        print("Verificar Texto: el valor mostrado en: " + locator + " es: " + ObjText + " el esperado es: " + TEXTO)
        assert TEXTO == ObjText, "Los valores comparados no coinciden"

    ##########################################################################
    #################   -=DATA DE ESCENARIO=-                ################
    ##########################################################################
    # Crear Step
    def create_variable_scenary(self, key, value):
        Scenario[key] = value
        print(Scenario)
        print ("Se almaceno la key " + key + " : " + value)

    # Crear Step
    def save_variable_scenary(self, element, variable):
        Scenario[variable] = Functions.get_text(self, element)
        print(Scenario)
        print ("Se almaceno el valor " + variable + " : " + Scenario[variable])

    # Crear Step
    def get_variable_scenary(self, variable):
        self.variable = Scenario[variable]
        print(f"get_variable_scenary: {self.variable}")
        return self.variable

    # Crear Step
    def compare_with_variable_scenary(self, element, variable):
        variable_scenary = str(Scenario[variable])
        element_text = str(Functions.get_text(self, element))
        _exist = (variable_scenary in element_text)
        print (_exist)
        print (f'Comparando los valores... verificando que si {variable_scenary} esta presente en {element_text} : {_exist}')
        assert _exist == True, f'{variable_scenary} != {element_text}'

    # Crear Step
    def textDateEnvironmentReplace(self, text):
        if text == 'today':
            self.today = datetime.date.today()
            text = self.today.strftime(Inicializar.DateFormat)
            print(text)

        if text == 'yesterday':
            self.today = datetime.date.today() - datetime.timedelta(days=1)
            text = self.today.strftime(Inicializar.DateFormat)

        if text == 'Last Month':
            self.today = datetime.date.today() - datetime.timedelta(days=30)
            text = self.today.strftime(Inicializar.DateFormat)

        return text

    # EXCEL
    # LEER CELDA
    def leer_celda(self, celda):
        wb = openpyxl.load_workbook(Inicializar.Excel)
        sheet = wb["DataTest"]
        valor = str(sheet[celda].value)
        print(u"------------------------------------")
        print(u"El libro de excel utilizado es: " + Inicializar.Excel)
        print(u"El valor de la celda es: " + valor)
        print(u"------------------------------------")
        return valor

    # ESCRIBIR CELDA
    def escribir_celda(self, celda, valor):
        wb = openpyxl.load_workbook(Inicializar.Excel)
        hoja = wb["DataTest"]
        hoja[celda] = valor
        wb.save(Inicializar.Excel)
        print(u"------------------------------------")
        print(u"El libro de excel utilizado es de es: " + Inicializar.Excel)
        print(u"Se escribio en la celda " + str(celda) + u" el valor: " + str(valor))
        print(u"------------------------------------")

    ##############   -=_CAPTURA DE PANTALLA_=-   #############################
    ##########################################################################

    def hora_Actual(self):
        self.hora = time.strftime(Inicializar.HourFormat)  # formato 24 horas
        return self.hora

    def crear_path(self):
        dia = time.strftime("%d-%m-%Y")  # formato aaaa/mm/dd
        GeneralPath = Inicializar.Path_Evidencias
        DriverTest = Inicializar.NAVEGADOR
        TestCase = self.__class__.__name__
        horaAct = horaGlobal
        x = re.search("Context", TestCase)
        if (x):
            path = f"{GeneralPath}/{dia}/{DriverTest}/{horaAct}/"
        else:
            path = f"{GeneralPath}/{dia}/{TestCase}/{DriverTest}/{horaAct}/"

        if not os.path.exists(path):  # si no existe el directorio lo crea
            os.makedirs(path)

        return path

    def capturar_pantalla(self, TestCase="Captura"):
        PATH = Functions.crear_path(self)
        img = f'{PATH}/{TestCase}_(' + str(Functions.hora_Actual(self)) + ')' + '.png'
        self.driver.get_screenshot_as_file(img)
        print(img)
        return img

    def captura(self, Descripcion):
        allure.attach(self.driver.get_screenshot_as_png(), Descripcion, attachment_type=allure.attachment_type.PNG)


    def ReplaceWithContextValues(self, text):
        PatronDeBusqueda = r"(?<=Scenario:)\w+"
        variables = re.findall(str(PatronDeBusqueda), text, re.IGNORECASE)
        for variable in variables:
            if variable == 'today':
                dateToday = str(datetime.date.today().strftime("%Y-%m-%dT%H:%M:%S"))
                text = re.sub('(Scenario:)([^&.]+)', dateToday, text, re.IGNORECASE)
                continue
            text = re.sub('(Scenario:)([^.]+)', Inicializar.Scenario[variable], text, re.IGNORECASE)
        return text