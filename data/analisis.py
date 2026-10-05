import pandas as pd
import os

# REGLA: Utilizar rutas relativas calculando los resultados desde el CSV
ruta_csv = "data/sensores_industriales.csv"
ruta_salida = "resultados/alertas.csv"

def analizar_datos():
    # Leer el archivo CSV
    try:
        df = pd.read_csv(ruta_csv)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en {ruta_csv}")
        return

    print("--- ANÁLISIS DE SENSORES INDUSTRIALES ---")

    # 1. Mostrar la cantidad de registros y de sensores distintos
    cantidad_registros = len(df)
    sensores_distintos = df['id_sensor'].nunique()
    print(f"\n1. Total de registros: {cantidad_registros}")
    print(f"   Sensores distintos: {sensores_distintos}")

    # 2. Calcular la temperatura promedio de cada planta
    promedio_por_planta = df.groupby('planta')['temperatura_c'].mean()
    print("\n2. Temperatura promedio por planta:")
    for planta, promedio in promedio_por_planta.items():
        print(f"   - {planta}: {promedio:.2f} °C")

    # 3. Encontrar la temperatura máxima e identificar el sensor y la fecha
    temp_maxima = df['temperatura_c'].max()
    # REGLA: Si hay empates, mostrar todos los resultados empatados
    registros_maximos = df[df['temperatura_c'] == temp_maxima]
    
    print(f"\n3. Temperatura máxima registrada: {temp_maxima} °C")
    print("   Detectada en:")
    for _, fila in registros_maximos.iterrows():
        print(f"   - Sensor: {fila['id_sensor']} | Fecha: {fila['fecha_hora']}")

    # 4. Contar las lecturas con temperatura mayor que 85 °C
    df_alertas = df[df['temperatura_c'] > 85]
    cantidad_alertas = len(df_alertas)
    print(f"\n4. Lecturas con alerta (mayor a 85 °C): {cantidad_alertas}")

    # 5. Identificar la planta con más alertas de temperatura
    if cantidad_alertas > 0:
        alertas_por_planta = df_alertas.groupby('planta').size()
        max_alertas = alertas_por_planta.max()
        # Manejo de empates en caso de que dos plantas tengan el mismo número máximo de alertas
        plantas_max_alertas = alertas_por_planta[alertas_por_planta == max_alertas].index.tolist()
        
        print(f"\n5. Planta(s) con más alertas ({max_alertas} alertas):")
        for planta in plantas_max_alertas:
            print(f"   - {planta}")
    else:
        print("\n5. No se registraron alertas de temperatura.")

    # 6. Exportar todas las lecturas con alerta conservando las columnas originales
    # Crear la carpeta 'resultados' si no existe
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
    
    df_alertas.to_csv(ruta_salida, index=False)
    print(f"\n6. Archivo de alertas exportado exitosamente a: '{ruta_salida}'")

if __name__ == "__main__":
    analizar_datos()