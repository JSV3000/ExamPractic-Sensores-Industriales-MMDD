
## Las 5V aplicadas al proyecto

| V         | Relacion con el sistema                                                                                                                                                                              | Ejemplo                                                                                                     | CSV Actual o Futura Ampliacion                                                                                     |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Volumen   | Nos referimos a los datos que genera nuestro sistema. En este caso tenemos 100,000 mediciones.                                                                                                       | Varios Sensores enviando datos de Temperatura cada segundo.                                                 | Actual y Futura a la vez.                                                                                          |
| Velocidad | Se refiere a la rapidez con la que se generan y se deberían procesar los datos. En nuestro caso es de 1 medición por minuto.                                                                         | Podría ser el contar las temperaturas mayores a 85 °C en el menor tiempo posible, por ejemplo, en segundos. | Futura para que se actualicen en segundos.                                                                         |
| Variedad  | Son los diferentes tipos de datos y formatos que existen. En el CSV se usan datos de tipo estructurado aunque se planean incorporar fotos y reportes de mantenimiento.                               | Las mediciones de temperatura, las fotos de algo y el reporte.                                              | Futura porque solo hay datos estructurados.                                                                        |
| Veracidad | Esto es la confiabilidad y calidad que se tienen de los datos. En este caso son 100,000 mediciones simuladas por lo que no se puede evaluar su veracidad.                                            | Cuando se comparar los datos de temperatura con la calibración y el estado real del sensor.                 | Futura porque actualmente solo son datos simulados                                                                 |
| Valor     | Esta es la utilidad que se obtienen de todos los datos para tomar decisiones. Aqui los datos nos permitiran saber donde se requiere mas atencion cuando haya temperaturas superiores al establecido. | Hacer una alerta cuando la temperatura sea mayor a 85 °C.                                                   | Actual y Fututa ya que los datos simulados permitirán saber como se podrá comportar y cuales necesitaría atencion. |


## Tipos de datos y procesamiento tradicional

| Lista                                          | Tipo de Dato     | Justificacion                                                                                                              |
| ---------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------- |
| El CSV de sensores.                            | Estructurado     | Es estructurado debido a que se cuentan con columnas y muchos registros definidos.                                         |
| Un mensaje JSON enviado por un sensor.         | Semiestructurado | Es semiestructurado debido a que si se cuenta con una estructura en sus campos y valores pero no posee esa forma de tabla. |
| Una fotografía de una máquina.                 | No estructurado  | No hay información escrita y mucho menos esta organizada como tabla.                                                       |
| El texto libre de un reporte de mantenimiento. | No estructurado  | No es estructurado debido a que no lleva una estructura fija por mas que tenga o pueda tener información escrita.          |
**¿Por qué 100,000 registros no convierten automáticamente al archivo en Big Data?**
No lo hacen debido a que por mas registros que se tengan, son registros simulados, ósea que son fijos, por lo tanto al no estar en constante actualización y no cumplir con las 5V actualmente se pueden procesar de cierta manera sencilla en python. 

Si fueran datos constantes, "Sin limite", ya pueden considerarse como Big Data.


## Batch y Streaming
En este caso se utiliza un tipo de procesamiento Batch debido a que los datos ya han sido almacenados y guardados en un archivo csv, por lo que no se procesan las mediciones conformen podrían llegar como en un tipo Streaming.

**¿Qué se utilizaría para generar una alerta pocos segundos después de recibir una lectura?**
Aquí se utilizaría un tipo de procesamiento Streaming, ya que este nos permite reaccionar de forma rápida ante la llegada de nuevos datos constantemente, como lo hacen en transferencias de bancos y así.

**¿Qué se utilizaría para generar un resumen al terminar el día?**
Aquí se volvería a utilizar un tipo de procesamiento Batch, debido a que para generar un resumen de cada día se necesitan datos que ya deben estar almacenados y a partir de ahí, generar el resumen con la información obtenida.


## Lambda y Kappa
**Escenario A**: la empresa quiere combinar una ruta que recalcule el historial por lotes con otra que procese las mediciones recientes rápidamente.

En este caso, la arquitectura ideal es Lambda, debido a que justamente combina ambos tipos de procesamiento que la empresa desea utilizar: Uno que recalcule el historia por lotes que seria un tipo de procesamiento Batch y a la vez, otro que procese las mediciones recientes rápidamente, el cual seria un tipo de procesamiento Streaming.

Lambda es la única que maneja ambos tipos de procesamiento, tanto Batch como Streaming.

                    ┌──────────────────┐
                    │     Sensores     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Almacenamiento   │
                    │   de datos       │
                    └───────┬──────────┘
                            │
                 ┌──────────┴──────────┐
                 │                     │
                 ▼                     ▼
        ┌─────────────────┐    ┌─────────────────┐
        │  Batch Layer    │    │  Speed Layer    │
        │                 │    │                 │
        │ Historial       │    │ Datos recientes │
        │ completo        │    │ en tiempo real  │
        └────────┬────────┘    └────────┬────────┘
                 │                      │
                 └──────────┬───────────┘
                            ▼
                   ┌─────────────────┐
                   │ Resultados /    │
                   │ Alertas /       │
                   │ Dashboard       │
                   └─────────────────┘


**Escenario B**: la empresa quiere una sola lógica de procesamiento de eventos y conservar las mediciones para volver a procesarlas cuando sea necesario.

En este caso, la única arquitectura que cuenta con una sola forma de procesamiento es la Kappa, por lo cual es la mas ideal. En este caso, lo datos se conservarían en un almacenamiento dedicado que permita volver a procesar los datos cuando sea necesario.

                 ┌──────────────────┐
                 │     Sensores     │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Flujo de eventos │
                 │   / Streaming    │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Almacenamiento   │
                 │ de eventos       │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Procesamiento    │
                 │     Kappa        │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Alertas /        │
                 │ análisis /       │
                 │ dashboard        │
                 └──────────────────┘
                          ▲
                          │
                   Reprocesamiento
                   de eventos



## Analítica descriptiva, predictiva y prescriptiva
**Analítica descriptiva**
Este tipo de analítica permite saber que ocurrió con los datos.

En el primer análisis (Hallazgo 1) se encontraron 6954 lecturas con una temperatura mayor a 85, que es lo establecido para las alertas, lo que seria un casi 7% del total de mediciones.

Además (Hallazgo 2), la Planta 3 fue la que presento la mayor cantidad de alertas, con un total de 1777 lecturas mayores a 85 grados, junto a ello, la temperatura mayor registrada es de 104.99 grados.

**Analítica predictiva**
Este otro tipo de analítica busca saber que podría ocurrir en el futuro utilizando información con la que ya se cuenta.

"¿Qué maquinas tienen mayor probabilidad de presentar temperatura superiores a 85 °C en un futuro?"

Para resolver esta pregunta se podría necesitar el historial de mantenimiento, las fallas ocurrida anteriormente, sus condiciones actuales, tipo y la antigüedad de la maquina, etc.


**Analítica prescriptiva**
Esta analítica busca saber que acción podría realizar una empresa ante una situación o un riesgo previsto.

En el caso del ejemplo anterior, podría ser el programar una inspección preventiva de las maquinas de la planta 3, que es donde se registro la mayor cantidad de alertas por temperatura.

En este caso, si es así, la empresa debería de checar datos como el saber cuales fueron las maquinas que generaron las alertas, si llegaron a ser aisladas o repetitivas, la evolución de la temperatura, las condiciones normales de operación, la antigüedad, entre muchos otros datos.