# Created by drodriguez at 9/11/2022
@ReciboNacional
Feature: Recibo Nacional - Compuestos
  Ingreso de mercancía a CEDIS de pedidos Nacionales
  Pedidos con Materiales compuestos

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

  @RECIBO_COMP_NAC
  Scenario: RECIBO RÁPIDO - MATERIALES COMPUESTOS
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDOCOMP
    And En el campo EAN escaneamos/ingresamos Scenario:EAN7
    And le doy click en Compuesto
    And esperamos
    And En el campo Partes escaneamos/ingresamos Scenario:NPartes
    And Capturo pantalla NumeroPartes
    And esperamos
    And le doy click en Guardar
    And esperamos
    And Capturo pantalla MaterialesEntrada
    And le doy click en IMPRIMIR
    And esperamos
    And En el campo IMPRESORA SIN FOTO ingresamos Scenario:IMPRESORAZEBRA
    And esperamos
    And le doy click en ACEPTAR
    And le doy click en SI
    And le doy click en MODAL CERRAR
    And esperamos
    And le doy click en OCULTAR IMPRESOS
    And le doy click en Refresh
    And esperamos
    And esperamos
    And le doy click en Refresh
    And le doy click en ETIQUETAS CEDIS
    And esperamos
    And En el campo IMPRESORA SIN FOTO ingresamos Scenario:IMPRESORAZEBRA
    And esperamos
    And le doy click en ACEPTAR
    And le doy click en MODAL CERRAR
    And esperamos
    And le doy click en Refresh
    And esperamos
    And Ingresamos a Scenario:ListadoBultos
    And le doy click en Shalom
    And En el campo Filtro Pedido escaneamos/ingresamos Scenario:PEDIDOCOMP
    And le doy click en Bultos Tiendas
    And esperamos
    And Capturo pantalla Bto-Tiendas
    And le doy click en Bultos CEDIS
    And esperamos
    And Capturo pantalla Bto-CEDIS
    And Ingresamos a Scenario:MANIFIESTOS
    And esperamos
    And Capturo pantalla Manifiestos
    And le doy click en ID Manifiesto
    And esperamos
    And le doy click en Ver Asiento
    And esperamos
    And Capturo pantalla DetalleManifiesto
