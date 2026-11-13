cantidad_camarotes_disponibles = 90
capacidad_maxima_cancelacion = 90
historial_total_reservas = 0

print("¡Bienvenido al sistema de gestión de camarotes del Crucero Atlántico!\n")

ejecutando_sistema = True

while ejecutando_sistema:
    print("=== MENÚ PRINCIPAL ===")
    print("1.- Camarotes disponibles.")
    print("2.- Reservar camarote.")
    print("3.- Cancelar camarote.")
    print("4.- Historial de reservas.")
    print("5.- Salir.")
    
    opcion_seleccionada_usuario = input("Selecciona una opción (1-5): ")
    
    if opcion_seleccionada_usuario == "1":
        
        print(f"\nCantidad actual de camarotes disponibles: {cantidad_camarotes_disponibles}\n")
        
    elif opcion_seleccionada_usuario == "2":
        
        while True:
            entrada_reservas = input("\nIngresa la cantidad de camarotes a reservar: ")
            if entrada_reservas.isdigit():
                cantidad_camarotes_a_reservar = int(entrada_reservas)
                if cantidad_camarotes_a_reservar <= 0:
                    print("La cantidad a reservar debe ser mayor a 0.")
                elif cantidad_camarotes_a_reservar > cantidad_camarotes_disponibles:
                    print(f"No hay suficientes camarotes disponibles. Disponibles actualmente: {cantidad_camarotes_disponibles}")
                else:
                    cantidad_camarotes_disponibles -= cantidad_camarotes_a_reservar
                    historial_total_reservas += cantidad_camarotes_a_reservar
                    print(f"¡Reserva exitosa! Has reservado {cantidad_camarotes_a_reservar} camarote(s).\n")
                    break
            else:
                print("Por favor, ingresa un número entero válido.")
                
    elif opcion_seleccionada_usuario == "3":
       
        while True:
            entrada_cancelaciones = input("\nIngresa la cantidad de camarotes a cancelar: ")
            if entrada_cancelaciones.isdigit():
                cantidad_camarotes_a_cancelar = int(entrada_cancelaciones)
                if cantidad_camarotes_a_cancelar <= 0:
                    print("La cantidad a cancelar debe ser mayor a 0.")
                elif cantidad_camarotes_a_cancelar > capacidad_maxima_cancelacion:
                    print(f"No se puede cancelar esa cantidad. Supera el límite de {capacidad_maxima_cancelacion} camarotes por operación.")
                else:
                    cantidad_camarotes_disponibles += cantidad_camarotes_a_cancelar
                    historial_total_reservas -= cantidad_camarotes_a_cancelar
                    print(f"¡Cancelación exitosa! Se han liberado {cantidad_camarotes_a_cancelar} camarote(s).\n")
                    break
            else:
                print("Por favor, ingresa un número entero válido.")
                
    elif opcion_seleccionada_usuario == "4":
       
        print(f"\nHistorial de reservas activas en esta sesión: {historial_total_reservas}\n")
        
    elif opcion_seleccionada_usuario == "5":
       
        print("\nGracias por utilizar nuestro software, hasta la próxima.")
        ejecutando_sistema = False
        
    else:
        print("\nOpción no válida. Por favor, selecciona una opción entre 1 y 5.\n")