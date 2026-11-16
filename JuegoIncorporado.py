#Versión Código implementando con los còdigos enviados
import os
import random
import time

emj_concentrese = [
    "💕", "😁", "👍", "🐝", "🐭", "🐹", "🐬", "🐟", "🐠", "🐡", 
    "🦀", "🦞", "🐙", "🥯", "🥖", "🥞", "🧇", "🍳", "🥚", "🥓", 
    "🌯", "🌮", "🥪", "🥙", "🧂", "🚲",  "🐰", "🚚", "🦽", "🕧", "🆒", "🥙"
]

def limpiar_pantalla():
    os.system("cls")

def seleccionar_nivel():
    while True:
        limpiar_pantalla()
        print("Juego de Concentrese versión Individual (o alterna y compite con amigos)")
        print("Selecciona el nivel de dificultad:")
        print("1. Fácil (4x4 - 8 parejas)")
        print("2. Intermedio (6x6 - 18 parejas)")
        print("3. Difícil (8x8 - 32 parejas)")
        print("")
        print("Escribe 's' o 'salir' para terminar el juego.")

        opcion = input("\nSelecciona una opción (1 a 3): ").strip().lower()

        if opcion in ["s", "salir"]:
            return None, None, None
        elif opcion == "1":
            return 4, 4, "Fácil"
        elif opcion == "2":
            return 6, 6, "Intermedio"
        elif opcion == "3":
            return 8, 8, "Difícil"
        else:
            print("\n Opción inválida. Elige un número del 1 al 3.")
            time.sleep(1.5)

def gen_tableros(cant_filas, cant_columnas):
    if not isinstance(cant_filas, int) or not isinstance(cant_columnas, int):
        raise TypeError("Las filas y columnas solo pueden ser números enteros.")
    if cant_filas <= 0 or cant_columnas <= 0:
        raise ValueError("Las columnas y filas deben ser mayores a 0.")
    
    cantidad_cart = cant_filas * cant_columnas
    if cantidad_cart % 2 != 0:
        raise ValueError("El número total de casillas para el tablero debe ser un número par.")
    
    cantidad_parejas = cantidad_cart // 2

    if cantidad_parejas > len(emj_concentrese):
        raise ValueError(f"El tablero requiere {cantidad_parejas} parejas, pero solo hay {len(emj_concentrese)} disponibles.")

    cartas_2_baraj = emj_concentrese[:cantidad_parejas] * 2
    random.shuffle(cartas_2_baraj)
    tabla_emojis = [
        cartas_2_baraj[indice_fila * cant_columnas : (indice_fila + 1) * cant_columnas]
        for indice_fila in range(cant_filas)
    ]
    matriz_cart_descubiertas = [[False] * cant_columnas for _ in range(cant_filas)]
    
    return tabla_emojis, matriz_cart_descubiertas

def pedir_coordenada(nombre_coord, max_val):
    while True:
        entrada = input(f"{nombre_coord} (0 a {max_val - 1} o 's' para salir): ").strip().lower()
        if entrada in ["s", "salir"]:
            return "salir"
        try:
            valor = int(entrada)
            if 0 <= valor < max_val:
                return valor
            else:
                print(f"Error: El número debe estar entre 0 y {max_val - 1}. Inténtalo de nuevo.")
        except ValueError:
            print("Error: Debes ingresar un número entero válido (no letras ni símbolos).")

def jugar_concentrese():
    filas, columnas, nivel = seleccionar_nivel()
    
    if filas is None: 
        print("\n¡Gracias por jugar! Hasta pronto.")
        return
    total_cartas = filas * columnas
    total_parejas = total_cartas // 2
    try:
        valores, descubiertas = gen_tableros(filas, columnas)
    except (TypeError, ValueError) as e:
        print(f"\n Error al generar el tablero: {e}")
        return

    parejas_encontradas = 0
    intentos = 0

    while parejas_encontradas < total_parejas:
        limpiar_pantalla()
        print(f"--- NIVEL: {nivel} | INTENTOS: {intentos} ---")
        print("Puedes escribir 'salir' para terminar el juego en cualquier momento.\n")
        encabezado_columnas = "    "
        for c in range(columnas):
            encabezado_columnas += f"{c:2} "
        print(encabezado_columnas)
        
        linea_separadora = "  "
        bloques_guiones = "----" * (columnas + 1)
        print(linea_separadora + bloques_guiones)
        for f in range(filas):
            fila_texto = f"{f} | "
            for c in range(columnas):
                if descubiertas[f][c]:
                    fila_texto += f"{valores[f][c]}  "
                else:
                    fila_texto += "⬛  "
            print(fila_texto)

        print("\n Giro Carta 1")
        f1 = pedir_coordenada("Fila", filas)
        if f1 == "salir":
            print("\n Decidiste terminar el juego. ¡Inténtalo cuando quieras!")
            return
        
        c1 = pedir_coordenada("Columna", columnas)
        if c1 == "salir":
            print("\n Decidiste terminar el juego. ¡Inténtalo cuando quieras!")
            return

        if descubiertas[f1][c1]:
            print("\n Opción repetida. La carta ya está descubierta. Intenta de nuevo.")
            time.sleep(1.5)
            continue
        
        descubiertas[f1][c1] = True
        limpiar_pantalla()
        print(f"--- NIVEL: {nivel} | INTENTOS: {intentos} ---")
        print(encabezado_columnas)
        print(linea_separadora + bloques_guiones)
        for f in range(filas):
            fila_texto = f"{f} | "
            for c in range(columnas):
                if descubiertas[f][c]:
                    fila_texto += f"{valores[f][c]}  "
                else:
                    fila_texto += "⬛  "
            print(fila_texto)

        print("\n Giro Carta 2")
        f2 = pedir_coordenada("Fila", filas)
        if f2 == "salir":
            print("\n Decidiste terminar el juego. ¡Inténtalo cuando quieras!")
            return

        c2 = pedir_coordenada("Columna", columnas)
        if c2 == "salir":
            print("\n Decidiste terminar el juego. ¡Inténtalo cuando quieras!")
            return

        if descubiertas[f2][c2] or (f1 == f2 and c1 == c2):
            print("\n Coordenada inválida o repetida. Se ocultará la carta que giraste.")
            descubiertas[f1][c1] = False
            time.sleep(1.8)
            continue
        
        descubiertas[f2][c2] = True
        intentos += 1

        limpiar_pantalla()
        print(f"--- NIVEL: {nivel} | INTENTOS: {intentos} ---")
        print(encabezado_columnas)
        print(linea_separadora + bloques_guiones)
        for f in range(filas):
            fila_texto = f"{f} | "
            for c in range(columnas):
                if descubiertas[f][c]:
                    fila_texto += f"{valores[f][c]}  "
                else:
                    fila_texto += "⬛  "
            print(fila_texto)

        if valores[f1][c1] == valores[f2][c2]:
            print("\n ¡Increíble! ¡Encontraste una pareja!")
            parejas_encontradas += 1
            time.sleep(1.5)
        else:
            print("\n Lástima, las cartas no coinciden. ¡Inténtalo de nuevo!")
            time.sleep(2)
            descubiertas[f1][c1] = False
            descubiertas[f2][c2] = False

    limpiar_pantalla()
    print("\n")
    print(" ¡FELICIDADES! ¡Eres el Ganador! ")
    print(f"   Nivel superado: {nivel}")
    print(f"   Total de intentos realizados: {intentos}")
    print("Puedes intentarlo en el siguiente nivel o probar si lo resuelves más rápido.")
    print("\n")
    
    while True:
            continuar = input("¿Deseas jugar nuevamente? (s = sí / n = salir): ").strip().lower()
            if continuar in ["s", "si", "sí"]:
                break  
            elif continuar in ["n", "no", "salir"]:
                print("\n Vuelve cuando quieras, Hasta la proxima.")
                return  
            else:
                print("Opción inválida. Recuerda escribir 's' para jugar otro tablero o 'n' para salir.")

if __name__ == "__main__":
    jugar_concentrese()
