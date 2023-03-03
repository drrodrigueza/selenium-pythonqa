import os


class Inicializar:
    # Directorio Base
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    # JsonData
    Json = basedir + u"/pages"

    Environment = 'Cedis'

    # BROWSER DE PRUEBAS
    NAVEGADOR = u'CHROME'

    # DIRECTORIO DE LA EVIDENCIA
    Path_Evidencias = basedir + u'/Data/Capturas'

    # HOJA DE DATOS EXCEL
    Excel = basedir + u'/data/DataTest.xlsx'

    # CSV = basedir + u'/data/ajuste_inventario.csv'


    PerfilChrome = basedir + u'/Data/perfiles/TestChrome'

    if Environment == 'Tienda':
        URL = 'https://qa-tiendas-frontend.titan.com.pa/seguridad/login'
        PEDIDO = "A2"
        Scenario = {
            "User": "6334",
            "Pass": "titan123",
            "NPERSONAL": "6334",
            "NUSUARIO": "6334",
            "NOMBRE": "Diango",
            "APELLIDO": "Rodríguez",
            "ROL1": "Auxiliar de Piso",
            "ROL2": "Auxiliar de Bodega",
            "TIENDA1": "ALBROOK",
            "TIENDA2": "METROMALL",
            "DEPARTAMENTO1": "ELECTRO",
            "DEPARTAMENTO2": "DAMA",
            "DetallePedido": "https://qa-tiendas-frontend.titan.com.pa/recibo/pedidocompra/consultar/",
            "ReciboRapido": "https://qa-cedis-front.titan.com.pa/recibo/pedidocompramaterial/recibo-rapido",
            "ListadoBultos": "https://qa-cedis-front.titan.com.pa/recibo/pedidocompramaterial/pedido-bulto",
            "OrdendeTrasnporte": "https://qa-tiendas-frontend.titan.com.pa/inicio/%C3%B3rdenes%20de%20transporte/da9e26a3-f530-47e6-8829-a5b7c8cd5a68",
            "CrearOTDemanda": "https://qa-tiendas-frontend.titan.com.pa/transporte/ordentransporte/crear/orden",
            "MANIFIESTOS": "https://qa-cedis-front.titan.com.pa/transaccion/manifiesto",
            "ListaOT": "https://qa-tiendas-frontend.titan.com.pa/transporte/ordentransporte",
            "MaterialOT": "G3",
            "Cantidad": "H3",
            "PEDIDO": "A2",
            "EAN1": "B2",
            "EAN2": "B3",
            "EAN3": "B4",
            "EAN4": "B5",
            "EAN5": "B6",
            # "UMP": round(CANTIDAD1 / 2),
            "IMPRESORAZEBRA": "Epson test",
            "IMPRESORAEPSON": "Isla07"
        }

    if Environment == 'Cedis':
        URL = 'https://qa-cedis-front.titan.com.pa/seguridad/login'
        Link = 'https://qa-cedis-front.titan.com.pa'
        PEDIDO = "A2"
        Scenario = {
            "User": "6334",
            "Pass": "titan123",
            "NPERSONAL": "6334",
            "NUSUARIO": "6334",
            "NOMBRE": "Diango",
            "APELLIDO": "Rodríguez",
            "ROL1": "Auditor",
            "ROL2": "Supervisor de Recibo",
            "TIENDA1": "ALBROOK",  # Almacenes
            "TIENDA2": "METROMALL",
            "DEPARTAMENTO1": "ELECTRO",
            "DEPARTAMENTO2": "DAMA",
            "DetallePedido": Link + "/recibo/pedidocompra/consultar/",
            "ReciboRapido": Link + "/recibo/pedidocompramaterial/recibo-rapido",
            "ListadoBultos": Link + "/recibo/pedidocompramaterial/pedido-bulto",
            "OrdendeTrasnporte": Link + "/inicio/%C3%B3rdenes%20de%20transporte/da9e26a3-f530-47e6-8829-a5b7c8cd5a68",
            "CrearOTDemanda": Link + "/transporte/ordentransporte/crear/orden",
            "MANIFIESTOS": Link + "/transaccion/manifiesto",
            "ListaOT": Link + "/transporte/ordentransporte",
            "Ajustes": Link + "/inventario/materialubicacion/ajuste-inventario",
            "ReciboNacional": Link + "/recibo/pedidocompramaterial/recibo-nacional",
            "ReciboNacionalTda": Link + "/recibo/pedidocompramaterial/recibo-nacional-tiendas",
            "ArmarBox": Link + "/enganche/bultoarmado/crear",
            "TipoAjuste": "Diferencia en Inventario",
            "MaterialOT": "G3",
            "Cantidad": "H3",
            "PEDIDO": "A2",
            "PEDIDO2": "A3",
            "PEDIDONE": "A9",
            "PEDIDOCOMP": "A17",
            "PEDIDONAC": "A21",
            "PEDIDONAC2": "A22",
            "PEDIDONACOMP": "A24",
            "PEDIDONACOMP2": "A26",
            "PEDIDONACOMB": "H21",
            "PEDIDONACONT": "H31",
            "PEDIDONACTDA": "A41",
            "CantNac": "C21",
            "CantNac2": "C22",
            "CantNCOMP": "C24",
            "CantNCOMP2": "C26",
            "CantNCOMB": "I23",
            "CantNCONT": "I26",
            "CantNCONT2": "I27",
            "CantNCONT3": "I28",
            "Empaque": "F21",
            "EmpaqueCOMP": "F24",
            "EmpaqueCOMB": "J23",
            "EAN1": "B2",
            "EAN2": "B3",
            "EAN3": "B4",
            "EAN4": "B5",
            "EAN5": "B6",
            "EAN6": "B9",
            "EAN7": "B17",
            "EAN8": "B18",
            "EAN9": "B19",
            "EAN10": "B21",
            "EAN11": "B22",
            "EAN12": "B24",
            "EAN13": "B26",
            "EANPPK": "H23",
            "EANCOMP": "H24",
            "EANREG": "H25",
            "EANCT1": "H26",
            "EANCT2": "H27",
            "EANCT3": "H28",
            "EANCT4": "H32",
            "EANCT5": "H33",
            "EANCT6": "H34",
            "M002": "K2",
            "M007": "K3",
            "M009": "K4",
            "M005": "L23",
            "NPartes": "C17",
            # "UMP": round(CANTIDAD1 / 2),
            "IMPRESORAZEBRA": "Epson test",
            "IMPRESORAEPSON": "Isla07",
            "Bulto": "A32",
            "EAN": "B32",
            "Enganchador": "C32",
            "Preparador": "D32",
            "Destino": "E32",
            "Cant": "F32",
            "CSV": "basedir + u'/data/ajuste_inventario.csv'"
        }

    if Environment == 'Local':
        URL = 'localhost:4200/seguridad/login'
        Link = 'localhost:4200'
        PEDIDO = "A2"
        Scenario = {
            "User": "6334",
            "Pass": "titan123",
            "NPERSONAL": "6334",
            "NUSUARIO": "6334",
            "NOMBRE": "Diango",
            "APELLIDO": "Rodríguez",
            "ROL1": "Auditor",
            "ROL2": "Supervisor de Recibo",
            "TIENDA1": "ALBROOK",  # Almacenes
            "TIENDA2": "METROMALL",
            "DEPARTAMENTO1": "ELECTRO",
            "DEPARTAMENTO2": "DAMA",
            "DetallePedido": Link + "/recibo/pedidocompra/consultar/",
            "ReciboRapido": Link + "/recibo/pedidocompramaterial/recibo-rapido",
            "ListadoBultos": Link + "/recibo/pedidocompramaterial/pedido-bulto",
            "OrdendeTrasnporte": Link + "/inicio/%C3%B3rdenes%20de%20transporte/da9e26a3-f530-47e6-8829-a5b7c8cd5a68",
            "CrearOTDemanda": Link + "/transporte/ordentransporte/crear/orden",
            "MANIFIESTOS": Link + "/transaccion/manifiesto",
            "ListaOT": Link + "/transporte/ordentransporte",
            "Ajustes": Link + "/inventario/materialubicacion/ajuste-inventario",
            "ReciboNacional": Link + "/recibo/pedidocompramaterial/recibo-nacional",
            "ReciboNacionalTda": Link + "/recibo/pedidocompramaterial/recibo-nacional-tiendas",
            "ArmarBox": Link + "/enganche/bultoarmado/crear",
            "TipoAjuste": "Diferencia en Inventario",
            "MaterialOT": "G3",
            "Cantidad": "H3",
            "PEDIDO": "A2",
            "PEDIDO2": "A3",
            "PEDIDONE": "A9",
            "PEDIDOCOMP": "A17",
            "PEDIDONAC": "A21",
            "PEDIDONAC2": "A22",
            "PEDIDONACOMP": "A24",
            "PEDIDONACOMP2": "A26",
            "PEDIDONACOMB": "H21",
            "PEDIDONACONT": "H31",
            "PEDIDONACTDA": "A41",
            "CantNac": "C21",
            "CantNac2": "C22",
            "CantNCOMP": "C24",
            "CantNCOMP2": "C26",
            "CantNCOMB": "I23",
            "CantNCONT": "I26",
            "CantNCONT2": "I27",
            "CantNCONT3": "I28",
            "Empaque": "F21",
            "EmpaqueCOMP": "F24",
            "EmpaqueCOMB": "J23",
            "EAN1": "B2",
            "EAN2": "B3",
            "EAN3": "B4",
            "EAN4": "B5",
            "EAN5": "B6",
            "EAN6": "B9",
            "EAN7": "B17",
            "EAN8": "B18",
            "EAN9": "B19",
            "EAN10": "B21",
            "EAN11": "B22",
            "EAN12": "B24",
            "EAN13": "B26",
            "EAN14": "B41",
            "EANPPK": "H23",
            "EANCOMP": "H24",
            "EANREG": "H25",
            "EANCT1": "H26",
            "EANCT2": "H27",
            "EANCT3": "H28",
            "EANCT4": "H32",
            "EANCT5": "H33",
            "EANCT6": "H34",
            "M002": "K2",
            "M007": "K3",
            "M009": "K4",
            "M005": "L23",
            "NPartes": "C17",
            # "UMP": round(CANTIDAD1 / 2),
            "IMPRESORAZEBRA": "Epson test",
            "IMPRESORAEPSON": "Isla07",
            "Bulto": "A32",
            "EAN": "B32",
            "Enganchador": "C32",
            "Preparador": "D32",
            "Destino": "E32",
            "Cant": "F32",
            "CSV": "basedir + u'/data/ajuste_inventario.csv'"
        }
