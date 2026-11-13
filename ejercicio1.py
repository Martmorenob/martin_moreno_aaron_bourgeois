cantidad_chefs_maestros = 0
cantidad_chefs_aprendices = 0

entrada_cantidad_chefs = input("Ingresa la cantidad de chefs a registrar: ")
while not (entrada_cantidad_chefs.isdigit() and int(entrada_cantidad_chefs) > 0):
    print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")
    entrada_cantidad_chefs = input("Ingresa la cantidad de chefs a registrar: ")
cantidad_total_chefs = int(entrada_cantidad_chefs)


for indice_chef in range(1, cantidad_total_chefs + 1):
    print(f"\n--- Registro del Chef {indice_chef} de {cantidad_total_chefs} ---")
    

   
codigo_culinario_chef = input("Ingresa el código culinario del chef: ")
while not (len(codigo_culinario_chef) >= 6 and " " not in codigo_culinario_chef):
        print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")
        codigo_culinario_chef = input("Ingresa el código culinario del chef: ")
        entrada_experiencia = int("Ingresa la experiencia culinaria (en años): ")

while not (entrada_experiencia.isdigit() and int(entrada_experiencia) > 0):
    print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")
    entrada_experiencia = input("Ingresa la experiencia culinaria (en años): ")
    experiencia_culinaria_anos = int(entrada_experiencia)

            

    if experiencia_culinaria_anos > 8:
        cantidad_chefs_maestros += 1
        print(f"El chef con código {codigo_culinario_chef} ha sido clasificado como: Chef Maestro.")
    else:
        cantidad_chefs_aprendices += 1
        print(f"El chef con código {codigo_culinario_chef} ha sido clasificado como: Chef Aprendiz.")


print("\n=== RESUMEN FINAL DE REGISTRO ===")
print(f"¡La escuela cuenta con {cantidad_chefs_maestros} Chefs Maestros y {cantidad_chefs_aprendices} Chefs Aprendices! ¡A cocinar!")