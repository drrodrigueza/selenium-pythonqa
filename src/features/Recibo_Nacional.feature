# Created by drodriguez at 9/8/2022

@ReciboNacional @WMS2
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
    And esperamos
    And esperamos
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

   @RN_CEDIS_PPK2
  Scenario: RECIBO NACIONAL - APLICA PREPACK Cambio de CTD Enganche
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDONAC2
    And En el campo EAN NAC escaneamos/ingresamos Scenario:EAN11
    And En el campo CANTIDAD A RECIBIR escaneamos/ingresamos Scenario:CantNac
    And En el campo UNIDAD DE EMPAQUE escaneamos/ingresamos Scenario:Empaque
    And esperamos
    And Capturo pantalla ReciboNac
    And le doy click en GUARDAR
    And esperamos
    And le doy click en Modif Enganche
    And esperamos
    And En el campo M002N escaneamos/ingresamos Scenario:M002
    ## solo esta permitiendo el cambio en M002
    #And En el campo M007N escaneamos/ingresamos Scenario:M007
    #And En el campo M009N escaneamos/ingresamos Scenario:M009
    And esperamos
    And Capturo pantalla ModificaEnganche
    And le doy click en Guardar
    And Capturo pantalla MaterialesEntrada
    And le doy click en Imprimir
    And esperamos
    And En el campo IMPRESORA SIN FOTO ingresamos Scenario:IMPRESORAZEBRA
    #And En el campo IMPRESORA CON FOTO ingresamos Scenario:IMPRESORAEPSON
    And le doy click en ACEPTAR
    And le doy click en MODAL CERRAR
    #And esperamos
    #And le doy click en ETIQUETAS CEDIS
    #And En el campo IMPRESORA SIN FOTO ingresamos Scenario:IMPRESORAZEBRA
    #And le doy click en ACEPTAR
    #And le doy click en MODAL CERRAR
    #And esperamos
    And esperamos
    And Ingresamos a Scenario:ListadoBultos
    And le doy click en Shalom
    And En el campo Filtro Pedido escaneamos/ingresamos Scenario:PEDIDONAC2
    And le doy click en Bultos Tiendas
    And esperamos
    And Capturo pantalla Bto-Tiendas
    And le doy click en Bultos CEDIS
    And esperamos
    And Capturo pantalla Bto-CEDIS
    And le doy click en Bultos Enganche
    And esperamos
    And Capturo pantalla Bto-ENGANCHE
    And Ingresamos a Scenario:ReciboNacional
    And esperamos
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDONAC2
    And le doy click en Pulmon
    And esperamos
    And Capturo pantalla PorPasarAPulmon
    And esperamos
    And esperamos
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

  @RN_CEDIS_COMP
  Scenario: RECIBO NACIONAL - MATERIALES COMPUESTOS
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDONACOMP
    And En el campo EAN NAC escaneamos/ingresamos Scenario:EAN12
    And En el campo CANTIDAD A RECIBIR escaneamos/ingresamos Scenario:CantNCOMP
    And En el campo UNIDAD DE EMPAQUE escaneamos/ingresamos Scenario:EmpaqueCOMP
    And esperamos
    And Capturo pantalla ReciboNac
    And le doy click en GUARDAR
    And esperamos
    And le doy click en CompuestoNac
    And esperamos
    And En el campo Partes escaneamos/ingresamos Scenario:NPartes
    And Capturo pantalla NumeroPartes
    And esperamos
    And le doy click en Guardar
    And esperamos
    And Capturo pantalla MaterialesEntrada
    And le doy click en Imprimir
    And esperamos
    And En el campo IMPRESORA CON FOTO ingresamos Scenario:IMPRESORAEPSON
    And esperamos
    And le doy click en ACEPTAR
    And le doy click en SI
    And le doy click en MODAL CERRAR
    And esperamos
    And Ingresamos a Scenario:ListadoBultos
    And le doy click en Shalom
    And En el campo Filtro Pedido escaneamos/ingresamos Scenario:PEDIDONACOMP
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



