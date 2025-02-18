import numeros


def preguntar():

    print("Bienvenido a Farmacia CEDOLINI")

    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmética")
        mi_rubro = input("Elija su rubro: ").upper()

        if mi_rubro in ["P", "F", "C"]:
            break
        else:
            print("Esa no es una opción válida")

    numeros.decorador(mi_rubro)


def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)  # Acá valido con index()
        except ValueError:
            print("Esa noes una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break


inicio()
