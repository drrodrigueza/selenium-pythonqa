# Created by drodriguez at 5/7/2022
  @WMS
@ReciboRapido
Feature: Recibo Rápido
  Ingreso de mercancía a CEDIS de pedidos Extranjeros y Zona Libre
  Pedidos que aplican PPK
  Pedidos que aplican PPK con Cambio de cantidad de Enganche
  Pedidos que no aplican PPK
  Pedidos con materiales compuestos

  Background:
    Given Cargo el DOM de la aplicación: login
    And En el campo Usuario CD escribo Scenario:User
    And En el campo Clave escribo Scenario:Pass
    And le doy click en Ingresar
    And esperamos
    And Capturo pantalla LoginCedis
    And Ingresamos a Scenario:ReciboRapido
    And Cargo el DOM de la aplicación: recibomercancia
    And le doy click en Shalom
    And esperamos

  @RECIBO_PPK
  Scenario: RECIBO RÁPIDO - APLICA PREPACK
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDO
    And En el campo EAN escaneamos/ingresamos Scenario:EAN1
    #And En el campo EAN escaneamos/ingresamos Scenario:EAN2
    #And En el campo EAN escaneamos/ingresamos Scenario:EAN3
    #And En el campo EAN escaneamos/ingresamos Scenario:EAN4
    #And En el campo EAN escaneamos/ingresamos Scenario:EAN5
    And Capturo pantalla MaterialesEntrada
    And le doy click en IMPRIMIR
    And En el campo IMPRESORA SIN FOTO ingresamos Scenario:IMPRESORAZEBRA
    And En el campo IMPRESORA CON FOTO ingresamos Scenario:IMPRESORAEPSON
    And esperamos
    And le doy click en ACEPTAR
    And le doy click en MODAL CERRAR
    And esperamos
    And le doy click en OCULTAR IMPRESOS
    And le doy click en Refresh
    And esperamos
    And esperamos
    And le doy click en Refresh
    And le doy click en ETIQUETAS CEDIS
    And En el campo IMPRESORA SIN FOTO ingresamos Scenario:IMPRESORAZEBRA
    And le doy click en ACEPTAR
    And le doy click en MODAL CERRAR
    And esperamos
    And le doy click en Refresh
    And esperamos
    And Ingresamos a Scenario:ListadoBultos
    And le doy click en Shalom
    And En el campo Filtro Pedido escaneamos/ingresamos Scenario:PEDIDO
    And le doy click en Bultos Tiendas
    And esperamos
    And Capturo pantalla Bto-Tiendas
    And le doy click en Bultos CEDIS
    And esperamos
    And Capturo pantalla Bto-CEDIS
    And le doy click en Bultos Enganche
    And esperamos
    And Capturo pantalla Bto-ENGANCHE
    And Ingresamos a Scenario:ReciboRapido
    And esperamos
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDO
    And le doy click en Prepack
    And esperamos
    And Capturo pantalla PorPasarAPulmon
    And le doy click en Seleccionar materiales
    And esperamos
    And le doy click en Pasar a Pulmon
    And esperamos
    And le doy click en Guardar
    And esperamos
    And le doy click en Refrescar
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

  @RECIBO_PPK2
  Scenario: RECIBO RÁPIDO - APLICA PREPACK Cambio de CTD Enganche
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDO2
    And En el campo EAN escaneamos/ingresamos Scenario:EAN2
    And le doy click en Modif Enganche
    And esperamos
    And En el campo M002 escaneamos/ingresamos Scenario:M002
    And En el campo M007 escaneamos/ingresamos Scenario:M007
    And En el campo M009 escaneamos/ingresamos Scenario:M009
    And esperamos
    And Capturo pantalla ModificaEnganche
    And le doy click en Guardar
    #And En el campo EAN escaneamos/ingresamos Scenario:EAN2
    #And En el campo EAN escaneamos/ingresamos Scenario:EAN3
    #And En el campo EAN escaneamos/ingresamos Scenario:EAN4
    #And En el campo EAN escaneamos/ingresamos Scenario:EAN5
    And Capturo pantalla MaterialesEntrada
    And le doy click en IMPRIMIR
    And En el campo IMPRESORA SIN FOTO ingresamos Scenario:IMPRESORAZEBRA
    And En el campo IMPRESORA CON FOTO ingresamos Scenario:IMPRESORAEPSON
    And esperamos
    And le doy click en ACEPTAR
    And le doy click en MODAL CERRAR
    And esperamos
    And le doy click en OCULTAR IMPRESOS
    And esperamos
    And le doy click en Refresh
    And esperamos
    And esperamos
    And le doy click en Refresh
    And le doy click en ETIQUETAS CEDIS
    And En el campo IMPRESORA SIN FOTO ingresamos Scenario:IMPRESORAZEBRA
    And le doy click en ACEPTAR
    And le doy click en MODAL CERRAR
    And esperamos
    And le doy click en Refresh
    And esperamos
    And Ingresamos a Scenario:ListadoBultos
    And le doy click en Shalom
    And En el campo Filtro Pedido escaneamos/ingresamos Scenario:PEDIDO2
    And le doy click en Bultos Tiendas
    And esperamos
    And Capturo pantalla Bto-Tiendas
    And le doy click en Bultos CEDIS
    And esperamos
    And Capturo pantalla Bto-CEDIS
    And le doy click en Bultos Enganche
    And esperamos
    And Capturo pantalla Bto-ENGANCHE
    And Ingresamos a Scenario:ReciboRapido
    And esperamos
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDO2
    And le doy click en Prepack
    And esperamos
    And Capturo pantalla PorPasarAPulmon
    And le doy click en Seleccionar materiales
    And esperamos
    And le doy click en Pasar a Pulmon
    And esperamos
    And le doy click en Guardar
    And esperamos
    And le doy click en Refrescar
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

  @RECIBO_NOPPK
  Scenario: RECIBO RÁPIDO - NO APLICA PREPACK
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDONE
    And En el campo EAN escaneamos/ingresamos Scenario:EAN6
    #And En el campo EAN escaneamos/ingresamos Scenario:EAN2
    #And En el campo EAN escaneamos/ingresamos Scenario:EAN3
    #And En el campo EAN escaneamos/ingresamos Scenario:EAN4
    #And En el campo EAN escaneamos/ingresamos Scenario:EAN5
    And Capturo pantalla MaterialesEntrada
    And le doy click en IMPRIMIR
    And En el campo IMPRESORA CON FOTO ingresamos Scenario:IMPRESORAEPSON
    And esperamos
    And le doy click en ACEPTAR
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
    And En el campo Filtro Pedido escaneamos/ingresamos Scenario:PEDIDONE
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

  @RECIBO_COMP
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
    And En el campo IMPRESORA CON FOTO ingresamos Scenario:IMPRESORAEPSON
    And esperamos
    And le doy click en ACEPTAR
    And le doy click en SI
    And le doy click en MODAL CERRAR
    And esperamos
    And le doy click en OCULTAR IMPRESOS
    And le doy click en Refresh
    And esperamos
    And esperamos
    And Ingresamos a Scenario:ListadoBultos
    And le doy click en Shalom
    And En el campo Filtro Pedido escaneamos/ingresamos Scenario:PEDIDOCOMP
    And le doy click en Bultos Tiendas
    And esperamos
    And Capturo pantalla Bto-Tiendas
    And Ingresamos a Scenario:MANIFIESTOS
    And esperamos
    And Capturo pantalla Manifiestos
    And le doy click en ID Manifiesto
    And esperamos
    And le doy click en Ver Asiento
    And esperamos
    And Capturo pantalla DetalleManifiesto












