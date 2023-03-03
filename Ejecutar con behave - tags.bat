echo. ##################### PRUEBAS ####################

echo. ##################### XML Y BEHAVE ####################
echo. behave --junit --tags=-skip --no-skipped

cd .\src\

echo. ##################### ELIMINAR CARPETA DE RESULTADOS ####################
del /f /q .\allure-results

behave -f allure_behave.formatter:AllureFormatter --tags=WMS --tags=-skip --no-skipped -o .\allure-results ./features -f pretty 

echo. behave -f allure_behave.formatter:AllureFormatter -o .\allure-results -f pretty

pause