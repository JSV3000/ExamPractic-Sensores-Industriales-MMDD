# ExamPractic-Sensores-Industriales-MMDD
Este proyecto realiza un análisis de datos sobre las mediciones de sensores industriales distribuidos en cuatro plantas para identificar alertas de temperatura, calcular métricas de operación y monitorear el estado de las máquinas.

##Dataset 
*Nombre del dataset: sensores_industriales.csv
Fuente: Archivo proporcionado por el maestro.
Descripción: El dataset contiene 100,000 mediciones secuenciales que incluyen el identificador de la medición, fecha y hora, identificador del sensor, planta de instalación, temperatura en grados Celsius y vibración en mm/s. Nota importante: Todos los datos utilizados en este proyecto son datos simulados.

##Objetivo El objetivo principal es procesar y analizar el registro histórico de los sensores mediante Python para extraer estadísticas operativas, identificar la temperatura máxima registrada, y aislar las lecturas críticas (mayores a 85 °C) para generar un reporte de alertas de mantenimiento reproducible.

##Requisitos Se requiere Python 3 y las siguientes dependencias, las cuales están detalladas con sus versiones en el archivo requirements.txt:

##Instalacion *Clonar el repositorio: git clone https://github.com/JSV3000/ExamPractic-Sensores-Industriales-MMDD.git* Entrar al proyecto: cd ExamPractic-Sensores-Industriales
*Crear el entorno: python -m venv .venv 
*Activarlo e instalar dependencias: source .venv/bin/activate pip install -r requirements.txt (linux / mac) o .venv\Scripts\activate
pip install -r requirements.txt (windows)

##Ejecucion Para ejecutar el análisis, realizar los cálculos y exportar el archivo de resultados, ejecuta el siguiente comando desde la terminal en la raíz del proyecto:  python analisis.py

##Analisis realizados 
Cuantificación del volumen de registros y recuento de sensores distintos operando en la red.
Cálculo del comportamiento térmico (temperatura promedio) segmentado por cada planta industrial.
Búsqueda de la temperatura máxima histórica, identificando el sensor exacto y la fecha de ocurrencia (incluyendo el manejo de empates).
Detección y conteo de alertas críticas correspondientes a lecturas que superan el umbral de seguridad de 85 °C.
Identificación de la instalación o planta con mayor incidencia de sobrecalentamientos.
Exportación de un subconjunto de datos filtrado (resultados/alertas.csv) exclusivamente con las mediciones en estado de alerta.

##Resultados y conclusiones A partir del codigo, el sistema logra aislar las mediciones que superan los 85 °C, exportándolas a un archivo independiente para su fácil revisión. El análisis permite identificar rápidamente cuál de las cuatro plantas concentra la mayor cantidad de alertas térmicas y cuál mantiene el promedio de temperatura más elevado. Esto facilita a los equipos de mantenimiento la toma de decisiones basadas en datos para priorizar inspecciones físicas en los sensores y máquinas que presentan el mayor estrés térmico, optimizando así los recursos operativos antes de ampliar el sistema a miles de sensores.