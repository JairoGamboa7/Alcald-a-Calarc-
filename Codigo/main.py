import os
import platform
from Accidente_de_Transito import main, limpiar_datos

# Función para limpiar consola
def limpiar_consola():
    sistema = platform.system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def menu():
    repetir = True

    while repetir:

        print("Iniciando el análisis de accidentes de tránsito...\n")
        
        print("MENÚ")
        print("1. Accidentes de tránsito")
        print("2. Sectores críticos de mortalidad")
        print("3. Vehículos matriculados")
        print("4. Análisis combinado (los 3 anteriores)\n")
        
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            print("\nSUBMENÚ:")
            print("1) Limpieza")
            print("2) Análisis estadístico")
            print("3) Visualización de datos")
            sub_opcion = input("Seleccione una sub-opción: ")

            # ---------- SUBMENÚ ----------
            if sub_opcion == '1':
                print("\nLimpieza de datos seleccionada.")
                main()

            elif sub_opcion == '2':
                print("\nAnálisis estadístico seleccionado.")

            elif sub_opcion == '3':
                print("\nVisualización de datos seleccionada.")

            else:
                print("\nSub-opción inválida.")
        
        elif opcion == '2':
            print("\nAnálisis de Sectores Críticos de Mortalidad seleccionado.")

        elif opcion == '3':
            print("\nAnálisis de Vehículos Matriculados seleccionado.")

        elif opcion == '4':
            print("\nAnálisis combinado seleccionado.")

        else:
            print("\nOpción no válida. Por favor seleccione 1 a 4.")

        # ---------- PREGUNTA PARA REPETIR ----------
        repetir_opcion = input("\n¿Desea ver otra cosa? (s/n): ").lower()

        if repetir_opcion == 's':
            limpiar_consola()  # Limpiar todo antes de volver a mostrar menú
        else:
            repetir = False
            print("\nPrograma finalizado.")

if __name__ == '__main__':
    menu()
