# Grupos-Relacionados-Diagnostico
GRD Data Analytics

Presento los siguientes archivos en llenguaje de codigo Python.
Los datos fueron procesado con Visual Studio Code

Hay 3 archivos en python .py
2019_top_20
2020_top_20
2021top20

Estos archivos en python generan una tabla con 20 filas de las agrupaciones de los diagnostico1-diagnostico2-procedimiento1-procedimiento2 para los años 2019, 2020 y 2021 
y su contador de cuantas veces se repiten esos codigos GRD.

Cada archivo Py es para un año diferente, y se genera una tabla automatica al correr el codigo en la misma localización del scrip o archivo py.
Ejmplo de tabla creada: tabla.csv_2020

Una vez obtenida las las tablas, las importe a excel. 
Luego importe a excel las hojas de los archivos excel CIE_9 y CIE_10 desde la pagina de FONASA

Fuente de los datos: 
https://www.fonasa.cl/sites/fonasa/datos-abiertos/bases-grd 
En base a búsqueda en octubre del 2023

Los top_20 de GRD combinados fueron cruzados con la descripción de sus respectivos códigos, asi se creo una tabla que incluyera
los codigos y sus descripciones con la formula BUSCARV, para luego pasar estas tablas a archivos de foto .jpg, creando 3 archivos:

top_20_2019.jpg
top_20_2020.jpg
top_20_2021.jpg

Estas tablas descriptivas permitirian el analisis de los GRD, pero se necesita mayor información.
