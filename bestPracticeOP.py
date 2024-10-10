class Alumno:
    # Crea la función constructor con atributos vacíos
    def __init__(self):
        self.__nombre = None
        self.__apellido_paterno = None
        self.__apellido_materno = None
        self.__no_control = None
        self.__semestre = None

    # Métodos para establecer valores (setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos para obtener valores (getters)
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre

    def get_Nombre_Completo(self):
        return self.__nombre + " " + self.__apellido_paterno + " " + self.__apellido_materno


# Diccionario para almacenar alumnos
registro_alumnos = {}

# Capturar 3 registros
for i in range(3):
    alumno = Alumno()  # Crear una nueva instancia en cada iteración
    alumno.set_nombre(input("Introduce el nombre: "))
    alumno.set_apellido_paterno(input("Introduce el apellido paterno: "))
    alumno.set_apellido_materno(input("Introduce el apellido materno: "))
    alumno.set_no_control(input("Introduce el número de control: "))
    alumno.set_semestre(int(input("Introduce el semestre: ")))

    registro_alumnos[i] = alumno

# Mostrar los nombres de los registros
for i in range(3):
    print(f"Nombre: {registro_alumnos[i].get_nombre()}")

alumno.set_nombre("Victor")

# Asignar valores a los atributos
# alumno.set_nombre("Carlos")
# alumno.set_apellido_paterno("González")
# alumno.set_apellido_materno("Pérez")
# alumno.set_no_control("2023101234")
# alumno.set_semestre(3)

# registro_alumnos[0] = alumno

# Obtener los valores
# print("Nombre: ", alumno.get_nombre())  # Carlos
# print("Apellido Paterno: ", alumno.get_apellido_paterno())  # González
# print("Apellido Materno: ", alumno.get_apellido_materno())  # Pérez
# print("Numero de Control: ", alumno.get_no_control())  # 2023101234
# print("Semestre: ", alumno.get_semestre())  # 3

# print("Nombre completo: ", alumno.get_Nombre_Completo())

# print("Nombre completo: ", alumno.get_nombre(), alumno.get_apellido_paterno(), alumno.get_apellido_materno())