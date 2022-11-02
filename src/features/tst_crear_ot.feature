# Created by drodriguez at 11/7/2022
Feature:Creación de OT
  se coloca la información de la historia de usuario
  # Enter feature description here

  @OT
  @TIENDA
  Scenario: Crear OT Demanda
    Given Cargo el DOM de la aplicación: login
    And En el campo Usuario TDA escribo Scenario:User
    And En el campo Clave escribo Scenario:Pass
    And le doy click en Ingresar
    And esperamos
    And Capturo pantalla Logintienda
    And Ingresamos a Scenario:OrdendeTrasnporte
    And esperamos
    And Ingresamos a Scenario:CrearOTDemanda
    And esperamos
    And Cargo el DOM de la aplicación: crearot
    And esperamos el elemento Marquesa
    And le doy click en Marquesa
    And esperamos
    And En el campo Material escaneamos/ingresamos Scenario:MaterialOT
    And En el campo Cantidad solicitada escaneamos/ingresamos Scenario:Cantidad
    And le doy click en Agregar
    And Capturo pantalla Material-OT
    And le doy click en Guardar
    And esperamos
    And Capturo pantalla OtGenerada
    And Ingresamos a Scenario:ListaOT
    And esperamos
    Then Capturo pantalla OtMarquesa



