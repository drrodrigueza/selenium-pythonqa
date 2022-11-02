# Created by drodriguez at 9/8/2022
@ReciboNacional
Feature: Recibo Nacional
  Ingreso de mercancía a CEDIS de pedidos Nacionales
  Pedidos que aplican PPK
  Pedidos que aplican PPK con Cambio de cantidad de Enganche
  Pedidos que no aplican PPK
  Pedidos con bultos contenedor

  Background:
    Given Cargo el DOM de la aplicación: login
    And En el campo Usuario CD escribo Scenario:User
    And En el campo Clave escribo Scenario:Pass
    And le doy click en Ingresar
    And esperamos
    And Capturo pantalla LoginCedis
    And Ingresamos a Scenario:ReciboNacional
    And Cargo el DOM de la aplicación: recibomercancia
    And le doy click en Shalom
    And esperamos

  @RN_CEDIS_PPK
  Scenario: RECIBO NACIONAL - APLICA PREPACK
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDONAC
    And En el campo EAN NAC escaneamos/ingresamos Scenario:EAN10
    And En el campo CANTIDAD A RECIBIR escaneamos/ingresamos Scenario:CantNac
    And En el campo UNIDAD DE EMPAQUE escaneamos/ingresamos Scenario:Empaque
    And esperamos
    And Capturo pantalla ReciboNac
    And le doy click en GUARDAR
    And esperamos
    And le doy click en Imprimir
    And esperamos
    And En el campo IMPRESORA SIN FOTO ingresamos Scenario:IMPRESORAZEBRA
    And esperamos
    And le doy click en ACEPTAR
    And le doy click en MODAL CERRAR
    And esperamos
    And Ingresamos a Scenario:ListadoBultos
    And le doy click en Shalom
    And En el campo Filtro Pedido escaneamos/ingresamos Scenario:PEDIDONAC
    And le doy click en Bultos Enganche
    And esperamos
    And Capturo pantalla Bto-ENGANCHE
    And Ingresamos a Scenario:ReciboNacional
    And esperamos
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDONAC
    And le doy click en Pulmon
    And esperamos
    And Capturo pantalla PorPasarAPulmon
    And le doy click en Seleccionar materiales
    And esperamos
    And le doy click en Pasar a Pulmon Nac
    And esperamos
    And le doy click en Guardar
    And esperamos
    And le doy click en Refresh Pulmon Nac
    And esperamos
    And Capturo pantalla EnPulmon
    And Ingresamos a Scenario:MANIFIESTOS
    And esperamos
    And Capturo pantalla Manifiestos
    And le doy click en ID Manifiesto
    And esperamos
    And le doy click en Ver Asiento
    And esperamos
    And Capturo pantalla DetalleManifiesto


