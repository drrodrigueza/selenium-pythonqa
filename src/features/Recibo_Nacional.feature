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

  @ReciboNacional @RN_CEDIS_PPK
  Scenario: RECIBO NACIONAL - APLICA PREPACK - SOLO ENGANCHE
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

  @ReciboNacional @RN_CEDIS_PPK2
  Scenario: RECIBO NACIONAL - APLICA PREPACK Cambio de CTD Enganche Varios Centros
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDONAC2
    And En el campo EAN NAC escaneamos/ingresamos Scenario:EAN11
    And En el campo CANTIDAD A RECIBIR escaneamos/ingresamos Scenario:CantNac2
    And En el campo UNIDAD DE EMPAQUE escaneamos/ingresamos Scenario:Empaque
    And esperamos
    And Capturo pantalla ReciboNac
    And le doy click en GUARDAR
    And esperamos
    And le doy click en Modif Enganche
    And esperamos
    And En el campo M002N escaneamos/ingresamos Scenario:M002
    And En el campo M007N escaneamos/ingresamos Scenario:M007
    And En el campo M009N escaneamos/ingresamos Scenario:M009
    And esperamos
    And Capturo pantalla ModificaEnganche
    And le doy click en Guardar
    And Capturo pantalla MaterialesEntrada
    And le doy click en Imprimir
    And esperamos
    And En el campo IMPRESORA SIN FOTO ingresamos Scenario:IMPRESORAZEBRA
    And En el campo IMPRESORA CON FOTO ingresamos Scenario:IMPRESORAEPSON
    And le doy click en ACEPTAR
    And le doy click en MODAL CERRAR
    And esperamos
    And esperamos
    And le doy click en Vista Bultos CEDIS
    And Capturo pantalla Bultos-CEDIS-C
    And esperamos
    And esperamos
    And le doy click en ETIQUETAS CEDIS
    And En el campo IMPRESORA SIN FOTO ingresamos Scenario:IMPRESORAZEBRA
    And le doy click en ACEPTAR
    And le doy click en MODAL CERRAR
    And esperamos
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

  @ReciboNacional @RN_CEDIS_COMP
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

  @ReciboNacional @RN_CEDIS_COMP2
  Scenario: RECIBO NACIONAL - MATERIALES COMPUESTOS VARIOS CENTROS
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDONACOMP2
    And En el campo EAN NAC escaneamos/ingresamos Scenario:EAN13
    And En el campo CANTIDAD A RECIBIR escaneamos/ingresamos Scenario:CantNCOMP2
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
    #And esperamos
    #And le doy click en ACEPTAR
    #And le doy click en SI
    #And le doy click en MODAL CERRAR
    And esperamos
    And le doy click en ETIQUETAS CEDIS
    And En el campo IMPRESORA SIN FOTO ingresamos Scenario:IMPRESORAZEBRA
    And le doy click en ACEPTAR
    And le doy click en MODAL CERRAR
    And esperamos
    And Ingresamos a Scenario:ListadoBultos
    And le doy click en Shalom
    And En el campo Filtro Pedido escaneamos/ingresamos Scenario:PEDIDONACOMP2
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

  @ReciboNacional @RN_CEDIS_COMB
  Scenario: RECIBO NACIONAL - COMBINADO (PPK - COMPUESTO - REGULAR - CONTENEDOR)
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDONACOMB
    # Recibo material PPK
    And En el campo EAN NAC escaneamos/ingresamos Scenario:EANPPK
    And En el campo CANTIDAD A RECIBIR escaneamos/ingresamos Scenario:CantNCOMB
    And En el campo UNIDAD DE EMPAQUE escaneamos/ingresamos Scenario:EmpaqueCOMB
    And esperamos
    And Capturo pantalla ReciboNac
    And le doy click en GUARDAR
    And esperamos
    And le doy click en Modif Enganche
    And esperamos
    And En el campo M005N escaneamos/ingresamos Scenario:M005
    And esperamos
    And Capturo pantalla ModificaEnganche
    And le doy click en Guardar
    And Capturo pantalla MaterialesEntrada
    And le doy click en Imprimir
    And esperamos
    And En el campo IMPRESORA SIN FOTO ingresamos Scenario:IMPRESORAZEBRA
    And En el campo IMPRESORA CON FOTO ingresamos Scenario:IMPRESORAEPSON
    And le doy click en ACEPTAR
    And le doy click en MODAL CERRAR
    And esperamos
    And Ingresamos a Scenario:ListadoBultos
    And le doy click en Shalom
    And En el campo Filtro Pedido escaneamos/ingresamos Scenario:PEDIDONACOMB
    And le doy click en Bultos Enganche
    And esperamos
    And Capturo pantalla Bto-ENGANCHE
    And Ingresamos a Scenario:ReciboNacional
    And esperamos
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDONACOMB
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
    And esperamos
    And Ingresamos a Scenario:MANIFIESTOS
    And esperamos
    And Capturo pantalla Manifiestos
    And le doy click en ID Manifiesto
    And esperamos
    And le doy click en Ver Asiento
    And esperamos
    And Capturo pantalla DetalleManifiesto
    # Recibo material COMPUESTO
    And Ingresamos a Scenario:ReciboNacional
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDONACOMB
    And En el campo EAN NAC escaneamos/ingresamos Scenario:EANCOMP
    And En el campo CANTIDAD A RECIBIR escaneamos/ingresamos Scenario:CantNCOMB
    And En el campo UNIDAD DE EMPAQUE escaneamos/ingresamos Scenario:EmpaqueCOMB
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
    And En el campo Filtro Pedido escaneamos/ingresamos Scenario:PEDIDONACOMB
    And le doy click en Bultos Tiendas
    And esperamos
    And Capturo pantalla Bto-Tiendas
    And esperamos
    And Ingresamos a Scenario:MANIFIESTOS
    And esperamos
    And Capturo pantalla Manifiestos
    And le doy click en ID Manifiesto
    And esperamos
    And le doy click en Ver Asiento
    And esperamos
    And Capturo pantalla DetalleManifiesto
    # Recibo material REGULAR
    And Ingresamos a Scenario:ReciboNacional
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDONACOMB
    And En el campo EAN NAC escaneamos/ingresamos Scenario:EANREG
    And En el campo CANTIDAD A RECIBIR escaneamos/ingresamos Scenario:CantNCOMB
    And En el campo UNIDAD DE EMPAQUE escaneamos/ingresamos Scenario:EmpaqueCOMB
    And esperamos
    And Capturo pantalla ReciboNac
    And le doy click en GUARDAR
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
    And En el campo Filtro Pedido escaneamos/ingresamos Scenario:PEDIDONACOMB
    And le doy click en Bultos Tiendas
    And esperamos
    And Capturo pantalla Bto-Tiendas
    And esperamos
    And Ingresamos a Scenario:MANIFIESTOS
    And esperamos
    And Capturo pantalla Manifiestos
    And le doy click en ID Manifiesto
    And esperamos
    And le doy click en Ver Asiento
    And esperamos
    And Capturo pantalla DetalleManifiesto
    # Recibo material BULTO CONTENEDOR
    And Ingresamos a Scenario:ReciboNacional
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDONACOMB
    And le doy click en Bulto contenedor
    And En el campo Codigo EAN agregamos/escaneamos Scenario:EANCT1
    And En el campo Cantidad agregamos/escaneamos Scenario:CantNCONT
    And le doy click en Agregar Material
    And esperamos
    And En el campo Codigo EAN agregamos/escaneamos Scenario:EANCT2
    And En el campo Cantidad agregamos/escaneamos Scenario:CantNCONT2
    And le doy click en Agregar Material
    And esperamos
    And En el campo Codigo EAN agregamos/escaneamos Scenario:EANCT3
    And En el campo Cantidad agregamos/escaneamos Scenario:CantNCONT3
    And le doy click en Agregar Material
    And esperamos
    And Capturo pantalla ReciboNaContenedor
    And le doy click en GUARDAR
    And esperamos
    And le doy click en Imprimir
    And esperamos
    And En el campo IMPRESORA SIN FOTO ingresamos Scenario:IMPRESORAZEBRA
    And esperamos
    And le doy click en ACEPTAR
    And le doy click en SI
    And le doy click en MODAL CERRAR
    And esperamos
    And Ingresamos a Scenario:ListadoBultos
    And le doy click en Shalom
    And En el campo Filtro Pedido escaneamos/ingresamos Scenario:PEDIDONACOMB
    And le doy click en Bultos Tiendas
    And esperamos
    And esperamos
    And Ingresamos a Scenario:MANIFIESTOS
    And esperamos
    And Capturo pantalla Manifiestos
    And le doy click en ID Manifiesto
    And esperamos
    And le doy click en Ver Asiento
    And esperamos
    And Capturo pantalla DetalleManifiesto

   @ReciboNacional @RN_CEDIS_CONT
  Scenario: RECIBO NACIONAL - CONTENEDOR
    And En el campo PEDIDO escaneamos/ingresamos Scenario:PEDIDONACOMB
    And esperamos
    And le doy click en Bulto contenedor
    And En el campo Codigo EAN agregamos/escaneamos Scenario:EANCT1
    And En el campo Cantidad agregamos/escaneamos Scenario:CantNCONT
    And le doy click en Agregar Material
    And esperamos
    And En el campo Codigo EAN agregamos/escaneamos Scenario:EANCT2
    And En el campo Cantidad agregamos/escaneamos Scenario:CantNCONT
    And le doy click en Agregar Material
    And esperamos
    And En el campo Codigo EAN agregamos/escaneamos Scenario:EANCT3
    And En el campo Cantidad agregamos/escaneamos Scenario:CantNCONT
    And le doy click en Agregar Material
    And esperamos
    And Capturo pantalla ReciboNaContenedor
    And le doy click en GUARDAR
    And esperamos
    And le doy click en Imprimir
    And esperamos
    And En el campo IMPRESORA SIN FOTO ingresamos Scenario:IMPRESORAZEBRA
    And esperamos
    And le doy click en ACEPTAR
    And le doy click en SI
    And le doy click en MODAL CERRAR
    And esperamos
    And esperamos
    And Ingresamos a Scenario:ListadoBultos
    And le doy click en Shalom
    And En el campo Filtro Pedido escaneamos/ingresamos Scenario:PEDIDONACOMB
    And le doy click en Bultos Tiendas
    And esperamos
    And Capturo pantalla Bto-Tiendas
    And esperamos
    And esperamos
    And Ingresamos a Scenario:MANIFIESTOS
    And esperamos
    And Capturo pantalla Manifiestos
    And le doy click en ID Manifiesto
    And esperamos
    And le doy click en Ver Asiento
    And esperamos
    And Capturo pantalla DetalleManifiesto



