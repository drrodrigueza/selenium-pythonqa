# Created by drodriguez at 5/7/2022
  @TIENDA
  Scenario: Crear el usuario en el WMS de la Tienda
    Given Cargo el DOM de la aplicación: login
    And En el campo Usuario TDA escribo Scenario:User
    And En el campo Clave escribo Scenario:Pass
    And le doy click en Ingresar
    And esperamos

Feature: Creación de usuarios

    And Capturo pantalla Logintienda
    And Ingresamos a la pantalla
    And Cargo el DOM de la aplicación: creausuario
    And En el campo Num Personal escribo Scenario:NPERSONAL
    And En el campo Nombre Usuario escribo Scenario:NUSUARIO
    And En el campo Nombre escribo Scenario:NOMBRE
    And En el campo Apellido escribo Scenario:APELLIDO
    And En el campo Roles ingresamos Scenario:ROL1
    And En el campo Roles ingresamos Scenario:ROL2
    And En el campo Tiendas ingresamos Scenario:TIENDA1
    And En el campo Tiendas ingresamos Scenario:TIENDA2
    And En el campo Departamentos ingresamos Scenario:DEPARTAMENTO1
    And En el campo Departamentos ingresamos Scenario:DEPARTAMENTO2
    And En el campo Clave escribo Scenario:Pass
    And En el campo Repetir escribo Scenario:Pass
    And le doy click en Guardar
    And validamos el Mensaje de error
    And Capturo pantalla UserError
    Then esperamos

  @CEDIS
  Scenario: Crear el usuario en el WMS de CEDIS
    Given Cargo el DOM de la aplicación: login
    And En el campo Usuario CD escribo Scenario:User
    And En el campo Clave escribo Scenario:Pass
    And le doy click en Ingresar
    And esperamos
    And Capturo pantalla LoginCedis
    And Entramos a la Gestion de usuarios
    And Cargo el DOM de la aplicación: creausuario
    And En el campo Numero Personal escribo Scenario:NPERSONAL
    And En el campo Nombre escribo Scenario:NOMBRE
    And En el campo ApellidoCD escribo Scenario:APELLIDO
    And En el campo Roles ingresamos Scenario:ROL1
    And En el campo Roles ingresamos Scenario:ROL2
    And En el campo Almacenes ingresamos Scenario:TIENDA1
    And En el campo Almacenes ingresamos Scenario:TIENDA2
    And En el campo Password escribo Scenario:Pass
    And En el campo Repetir Password escribo Scenario:Pass
    And le doy click en Guardar
    And validamos el Mensaje error de error
    And Capturo pantalla UserErrorcd
    Then esperamos
