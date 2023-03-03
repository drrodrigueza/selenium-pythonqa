# -*- coding= utf-8 -*-
# Created by drodriguez at 4/1/2023
  @WMS2
@Enganche @WMS2
Feature: Armado de Box
  Armado de boxes de bultos provenientes de la cancha

  Background:
    Given Cargo el DOM de la aplicación: login
    And En el campo Usuario CD escribo Scenario:User
    And En el campo Clave escribo Scenario:Pass
    And le doy click en Ingresar
    And esperamos
    And Capturo pantalla LoginCedis
    And Ingresamos a Scenario:ArmarBox
    And Cargo el DOM de la aplicación: enganche
    And esperamos

  @EngancheLiquidacion
  Scenario: ARMADO DE BOX - BULTOS LIQUIDACIÓN 1 MATERIAL
    And En el campo Bulto escaneamos/ingresamos Scenario:Bulto
    And esperamos
    And En el campo Codigo EAN escaneamos/ingresamos Scenario:EAN
    And esperamos
    And En el campo Enganchador escaneamos/ingresamos Scenario:Enganchador
    And En el campo Preparador escaneamos/ingresamos Scenario:Preparador
    And esperamos
    And En el campo Destino escaneamos/ingresamos Scenario:Destino
    And esperamos
    And le doy click en Modal Box
    And En el campo Cantidad escaneamos/ingresamos Scenario:Cant
    And esperamos
    And le doy click en Agregar Material
    And le doy click en Cerrar e Imprimir
    And esperamos
    And le doy click en Cerrar e Imprimir





