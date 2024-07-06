from FUNCIONES_ADRIAN_LIZANA_005 import menu, registrar_cliente, listar_clientes, registrar_compra, enviar_resumen_puntos
menu()
BD = []

print("¡Bienvenido A TODO AHORRO!")

while True:
    
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        registrar_cliente(BD)

    elif opcion == "2":
        listar_clientes(BD)

    elif opcion == "3":
        registrar_compra(BD)

    elif opcion == "4":
        enviar_resumen_puntos(BD)

    elif opcion == "5":
        print("Gracias vuelve pronto!")
        break

    else:
        print("Opción inválida. Intenta otra vez.")
