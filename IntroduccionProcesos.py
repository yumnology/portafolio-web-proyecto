import operator


tareas = {}

def nombre_tarea():
    a = input("")
    return a

def valor_tarea():
    while True:
        try:
            b = int(input())
            return b
        except ValueError:
            print("El valor introducido es de tipo texto, necesita introducir un numero")

def main():
    while input("Desea agregar una tarea: S/N") == "S":
        print("introduzca una tarea: ")
        tarea = nombre_tarea()
        print("introduzca el valor para la tarea: ")
        valor = valor_tarea()
        tareas[tarea] = valor
    sorteddict = sorted(tareas.items(), key=operator.itemgetter(1), reverse=True)
    print("Esta es tu lista de tareas total ordenada:  {} ".format(sorteddict))

    for a in sorteddict:
        print("La primera tarea que tienes que realizar es: {}".format(a))
        while input("Has realizado esta tarea S/N") == "N":
            print("La siguiente tarea ha realizar es {}".format(a))

        print("Felicidades!!, has realizado la tarea!")


if __name__ == "__main__":
    main()

    