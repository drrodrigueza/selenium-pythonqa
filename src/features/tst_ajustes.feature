# Created by drodriguez at 22/7/2022
Feature: Ajuste Masivo
  # Ajustes de inventario con carga CSV

  Scenario: Ajuste Masivo en CEDIS
    Given Cargo el DOM de la aplicación: login
    And En el campo Usuario CD escribo Scenario:User
    And En el campo Clave escribo Scenario:Pass
    And le doy click en Ingresar
    And esperamos
    And Capturo pantalla LoginCedis
    And Ingresamos a Scenario:Ajustes
    And Cargo el DOM de la aplicación: ajustes
    And le doy click en Shalom
    And En el campo Tipos ingresamos Scenario:TipoAjuste
    And esperamos
    #And le doy click en Seleccionar CSV
    And En el campo Seleccionar CSV ingresamos CSV
    And esperamos