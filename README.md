### Ejemplo de carga de archivo csv desde Kaggle a Azure SQL utiliando Python
### Se proporciona el archivo load_csv.py desarrollado en Python para leer un archivo csv ubicado en
### https://www.kaggle.com/datasets/anoopjohny/consumer-complaint-database/data
### Requerimientos:
### - Ambiente con Phython 3 y librerias kaggle, pandas y sqlalchemy instaladas
### - Azure SQL de prueba
### - Arhivo kaggle.json generado previamente desde Kaggle que permite la conexión desatentida y uso de la API KaggleApi desde Python, este archivo se debe copiar al ambiente de ejecución de Python
### Consideraciones:
### - El archivo python está desarrollado de una forma simple para una carga de prueba inicial de datos, para el manejo de errores se deben añadir pasos adionales en el programa.
### - Para llevar esta solución a la nube Azure como una tarea automática se propone el uso de Azure Logic Apps como herramienta de planificación de ejecuciones y orquetación, el uso de Azure Funtions para ejecutar desde Logic Apps el código phyton, un Azure SQL como repositorio de los datos leidos, Un Azure Blob Stoage para guardar metada y el uso de Azure Key Vault como buena practica para guardar los datos de conexión a los origines y destino de los datos.
![image](https://github.com/acols/kaggle/assets/27938147/467ab832-1c1c-4abd-8479-08a15896fbd4)


