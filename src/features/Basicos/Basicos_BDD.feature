# Created by drodriguez at 4/7/2022
@Selenium
Feature: Funciones basicas de Selenium con BDD

  @Navegador
  Scenario: Abrir el navegador
    Given Abrir la aplicacion

  @Navegador
  Scenario: Abrir url
    Given Inicializo en la URL https://qa-cedis-front.titan.com.pa/seguridad/login

  @Navegador
  Scenario: Abrir con navegador
    Given Abro la aplicacion con el navegador CHROME
    Then cierro la aplicación

  @DOM
  Scenario: Seteamos el DOM - Archivo JSON
    Given Abrir la aplicacion
    And Cargo el DOM de la aplicación: login
    And En el campo Usuario CD escribo 6334
    And En el campo Clave ingresamos titan123
    And le doy click en el botón Ingresar
    And Tomar captura Logincedis
    And esperamos
    Then cierro la aplicación

   @Captura
  Scenario: Tomar captura de pantalla
    Given Abrir la aplicacion
    And Cargo el DOM de la aplicación: login
    And En el campo Usuario CD escribo 6334
    And Capturo pantalla Sesión
    And Tomar captura Login
    Then cierro la aplicación

  Scenario: RECIBO RÁPIDO - NO APLICA PREPACK
    Given Cargo el DOM de la aplicación: login
    And En el campo Usuario CD escribo Scenario:User
    And En el campo Clave escribo Scenario:Pass
    And le doy click en Ingresar
    And esperamos
    And Capturo pantalla LoginCedis
    And Ingresamos a Scenario:MANIFIESTOS
    And Cargo el DOM de la aplicación: recibomercancia
    And esperamos
    And le doy click en ID Manifiesto
    And esperamos
    And le doy click en Ver Asiento
    And esperamos