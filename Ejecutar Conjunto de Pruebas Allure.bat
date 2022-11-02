echo. ##################### PRUEBAS #####################
cd .\src\tests
python -m pytest prueba001.py --alluredir ..\allure-results
python -m pytest tst_wmscd2.py --alluredir ..\allure-results


pause