# Created by drodriguez at 2/3/2023
Feature: Recibo Nacional Tendas
  Ingreso de mercancía a Tiendas de pedidos Nacionales
  Pedidos con Materiales compuestos

  Background:
    Given Cargo el DOM de la aplicación: login
    And En el campo Usuario CD escribo Scenario:User
    And En el campo Clave escribo Scenario:Pass
    And le doy click en Ingresar
    And esperamos
    And Capturo pantalla LoginCedis
    And Ingresamos a Scenario:ReciboNacional
    And Cargo el DOM de la aplicación: recibonactda
    And le doy click en Los Pueblos
    And esperamos


