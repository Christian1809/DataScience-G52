import os
from time import sleep

dic_empresas = {
    '20454545': {
        'razon_social': 'EMPRESA SAC',
        'direccion': 'CALLE EL SOL 123'
    },
    '1234': {
        'razon_social': 'DULCERIA SA',
        'direccion'   :  'av Dueñas',
    }
}


ANCHO = 50

while True:
    os.system("clear")  # usar "cls" en windows si no funciona
    print("=" * ANCHO)
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("=" * ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
    """)
    print("=" * ANCHO)
    opcion = input("INGRESE OPCION : ")

    os.system("clear")

    if opcion == "1":
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese RUC: ")
        if ruc in dic_empresas:
            print("La empresa ya existe.")
        else:
            razon = input("Ingrese razón social: ")
            direccion = input("Ingrese dirección: ")
            dic_empresas[ruc] = {
                'razon_social': razon,
                'direccion': direccion
            }
            print("Empresa registrada correctamente.")
        input("Presione ENTER para continuar...")

    elif opcion == "2":
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESAS")
        print("=" * ANCHO)
        if len(dic_empresas) == 0:
            print("No hay empresas registradas.")
        else:
            for ruc, datos in dic_empresas.items():
                print(f"RUC: {ruc}")
                print(f"Razón Social: {datos['razon_social']}")
                print(f"Dirección: {datos['direccion']}")
                print("-" * ANCHO)
        input("Presione ENTER para continuar...")

    elif opcion == "3":
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese el RUC de la empresa a actualizar: ")
        if ruc in dic_empresas:
            razon = input("Nueva razón social: ")
            direccion = input("Nueva dirección: ")
            dic_empresas[ruc]['razon_social'] = razon
            dic_empresas[ruc]['direccion'] = direccion
            print("Datos actualizados correctamente.")
        else:
            print("No existe empresa con ese RUC.")
        input("Presione ENTER para continuar...")

    elif opcion == "4":
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese el RUC de la empresa a eliminar: ")
        if ruc in dic_empresas:
            del dic_empresas[ruc]
            print("Empresa eliminada correctamente.")
        else:
            print("No existe empresa con ese RUC.")
        input("Presione ENTER para continuar...")

    elif opcion == "5":
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL SISTEMA...")
        print("=" * ANCHO)
        sleep(2)
        break

    else:
        print("Opción no válida.")
        sleep(2)
