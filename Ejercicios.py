#password="ceballos"
#user=123

#password=input("ingrese su contraseña")
#user=int(input("ingrese su usuario"))

#if password=="ceballos" and user==123:
    #print("Has ingresado")
#else:
    #print("Vuelve a intentar")
#EJERCICIO 1: # Precio y cantidad, calcular el subtotal, si el subtotal es mayor de 1 millon
# calcular descuento del 25% de lo contrario el descuento es de 0%.
# Calcular el IVA y el neto a pagar.

#precio=int(input("ingrese el precio del articulo"))
#cantidad=int(input("ingrese la cantidad de articulos"))
#subtotal=precio*cantidad
#iva= float(subtotal*0.19)
#neto_pagar= float(subtotal+iva)
#pagar= float (neto_pagar-(neto_pagar*0.25))
#if subtotal>1000000:
    #print(f"El descuento es de 25% {subtotal*0.25}, el valor del IVA es de ${iva} y el valor a pagar es de ${pagar}")
#else:
    #print(f"el descuento es del 0%, el IVA es de ${iva} por lo tanto debe pagar ${neto_pagar}")

#Realizar un programa que me pida el producto, precio, cantidad y a que categoría pertenece para que imprima
# el subtotal su descuento, iva y precio neto.
#De ser categoría1 y que el producto tenga una cantidad mayor a 10 aplicaría un descuento del 15%
#De ser categoría2 y que el producto tenga una cantidad mayor a 20 aplicaría un descuento del 20%
#De ser categoría3 y que el producto tenga una cantidad mayor a 21 aplicaría un descuento del 30%
#Si no entonces todos los productos independientes de la cantidad y su categoría tendrán el 5% de descuento.

#categoria_1=0.15
#categoria_2=0.20
#categoria_3=0.30

#producto=input("ingrese el nombre del producto elegido")
#precio=int(input("ingrese el valor del producto"))
#cantidad=int(input("ingrese la cantidad de productos a llevar"))
#categoria=input("ingrese la clase de categoria: categoria1,categoria2,categoria3")
#subtotal=precio*cantidad
#iva= float(subtotal*0.19)
#neto_pagar= float(subtotal+iva)

#if cantidad>10 and categoria=="categoria1":
    #print(f"Para este caso aplica la categoria 1 con un descuento del 15% {subtotal*categoria_1}, por lo tanto el subtotal es "
          #f"{subtotal} el iva es de {iva} y el precio neto a pagar es de {((subtotal+iva)-(subtotal*categoria_1))}")
#elif cantidad>20 and categoria=="categoria2":
    #print(f"Para este caso aplica la categoria 2 con un descuento del 20%{subtotal*categoria_2}, por lo tanto el subtotal es "
          #f"{subtotal} el iva es de {iva} y el precio neto a pagar es de {((subtotal+iva)-(subtotal*categoria_2))}")
#elif cantidad>21 and categoria=="categoria3":
    #print(f"Para este caso aplica la categoria 3 con un descuento del 30% {subtotal*categoria_3}, por lo tanto el subtotal es "
          #f"{subtotal} el iva es de {iva} y el precio neto a pagar es de {((subtotal+iva)-(subtotal*categoria_3))}")
#else:
    #print(f"Para este caso todos los productos independientes de la cantidad y su categoría tendrán el 5% de descuento ,"
          #f" por lo tanto el subtotal es {subtotal} el iva es de {iva} y el precio neto a pagar es de {neto_pagar}")

#import random


#vidas=5
#puntos=0

#Si sale cero pierde una vida
#Si se genera cualquier otro numero dentro un rango rdtsblrcido, gana puntos.




#while vidas !=0:
   #num=random.randint(0,9)
   #if num !=0:
       #puntos+=1
       #print("Tienes ",{puntos},"puntos")
   #else:
       #vidas-=1
       #print("Te quedan", {vidas},"vidas")

#Reciban por consola el valor de una compre
#que puedan ingresar el numero de cuotas
#calcular el valor de la cuota
#usando while queremos que imprima el plan de pago y le muestre el cupo liberado con cada pago


#valor=int(input(f"ingrese el valor total de la compra"))
#cuotas=int(input(f"Ingrese cantidad de cuotas a diferir"))
#interes=valor*0.18
#valor_cuota=(valor+interes)/cuotas
#numcuotas=1

#while cuotas !=0:
    #print(f"El valor de la cuota , {numcuotas} es {valor_cuota}")
    #numcuotas+=1
    #cuotas-=1


#print("1. Registro\n 2.Login\n 3.Salir)"

#opc=0

#if opc==1:
    #print("Registro")
#elif opc==2:
    #print("Login")
#elif opc==3:
    #print("Salir")
#else:
    #print(("Seleccione una opción valida")

#Generar un programa que permita hacer el registro e iniciar sesion dentro de While, debe imprimir el menu usando la
#implementación de if,elif,else (selector multiple).Cuando inicie sesion que implemente la solución del calculo de cuotas
#creada en el reto anterior.




#opc=int(input("1. Registro\n 2.Login\n 3.Salir\n"))


#if opc==1:
    #print("Registro")
#elif opc==2:
    #print("Login")
#elif opc==3:
    #print("Salir")
#else:
    #print("Seleccione una opción valida")

#user="duvacean"
#password=12345

#usuario=input(f"ingrese el usuario")
#contraseña=int(input(f"Ingrese su contraseña"))

"""def valor():
    valor=int(input(f"ingrese el valor total de la compra"))

    cuotas=int(input(f"Ingrese cantidad de cuotas a diferir"))

    interes=valor*0.18
    valor_cuota=(valor+interes)/cuotas
    numcuotas=1

    while cuotas !=0:
        print(f"El valor de la cuota , {numcuotas} es {valor_cuota}")
        numcuotas+=1
        cuotas-=1


if usuario==user and password==contraseña:
     print("Bienvenido");
     valor()
else:
     print("Intente de nuevo porfavor");"""

"""saldo=0

acumIngresos=0
acumEgresos=0

isOn= int(input("ingrese 1 para inicializar el servicio\n"))


while isOn !=0:
    opc= int(input("1.Ingreso:\n 2.Egreso:\n 3.Salir"))

    if opc==1:
        ingreso=int(input("Registre el ingreso:"))

        saldo= saldo+ingreso

        print(f"Su saldo es ${saldo}")

        acumIngresos+=1
        print(acumIngresos)
    elif opc==2:
        egreso=int(input("Registre el monto a retirar"))

        saldo=saldo-egreso

        if saldo<=0:
            print("Saldo insuficiente")
            saldo=saldo+egreso
            print(saldo)

        else:
            print(f"Su saldo es $:{saldo}")
        acumEgresos += 1
        print(acumEgresos)

    elif opc==3:
        print("Salir")
        isOn=0
    else:
        print("Ingrese una opción válida")"""

#---------------------------------------------------------------------


"""Las listas son estructuras de datos lineales se crean usando un brackes,ejemplo: my_list=[]
Las listas son ordenadas (Orden de insersion),es decir que el último dato ingresado ocupara la última posición
Emplea metodos para manipular los items de la misma.
Cómo los arrays la primera posición inicia en 0
Permite item duplicados y los trata como independientes, ejemplo:maria,maria.
Las listas son mutables, es decir podemos agregar,actualizar o remover items.
Pueden contener distintos tipos de datos."""


"""nombres=["Juan","Pepito","Maria","Luis"]
#Metodo len valida el tamaño de la lista
print(len(nombres))
print(type(nombres))

listaDatos=["Pepito","Perez",1000000,1.80,True]

print(f"La estatura es de {listaDatos[3]}")

#Slicing de datos
print(listaDatos[0:2])

print(listaDatos[1:4])

print(listaDatos[:4])

print(listaDatos[2:])

print(listaDatos[:-1])

print(listaDatos[:-2])

print(listaDatos[-4:-1])

print(listaDatos[1:4])"""

# sumando 2 numeros
""" valor1 = 7
valor2 = 4

resultado = valor1 + valor2
print(resultado) """

#comentario en linea y extracion de una palabra
new_word = "No pares de aprender"

short_word = new_word[3:8]

print("¡Nunca " + short_word + " de aprender!")

categoria = int (input("ingrese la categoria del producto 1, 2, 3"))
precio = int(input("ingrese el precio del producto"))
cantidad = int(input("ingrese la cantidad de cuantos productos compro"))
subtotal = precio*cantidad
if categoria == 1 and cantidad>20:
    total = subtotal-(subtotal*0.15)+(subtotal*0.19)
    print (f"total de la compra es {subtotal} compro mas de 20 articulos aplica el descuento de {subtotal*0.15} y un iva de {subtotal*0.19} para un total a pagar es de {total}")
elif categoria == 2 and cantidad>20:
    total = subtotal-(subtotal*0.20)+(subtotal*0.19)
    print (f"total de la compra es {subtotal} compro mas de 20 articulos aplica el descuento de {subtotal*0.20} y un iva de {subtotal*0.19} para un total a pagar es de {total}")
elif categoria == 3 and cantidad>21:
    total = subtotal-(subtotal*0.30)+(subtotal*0.19)
    print (f"total de la compra es {subtotal} compro mas de 20 articulos aplica el descuento de {subtotal*0.30} y un iva de {subtotal*0.19} para un total a pagar es de {total}")
else:
    total = subtotal-(subtotal*0.05)+(subtotal*0.19)
    print (f"total de la compra es {subtotal} de las 3 categorias no selecciono ninguna entonces no tiene descuento {subtotal*0.05} y un iva de {subtotal*0.19} para un total a pagar es de {total}")

import random
vidas = 5
puntos = 0

#si sale cero pierde una vida, si se genera cualquier otro numrto dentro de un rango establecido, gana puntos 

while vidas !=0:
    num = random.randint(0,9)

    if num != 0 :
        puntos += 1
        print ("tienes ", puntos, "puntos")
    else:
        vidas -= 1
        print ("te quedan ", vidas, "vidas")

""" Reciban por consola el valor de una compra que puedan ingresar el numero de coutas
calcular el valor de la cuota
usando while queremos que imprima el plan de pago y le muestre el cupo liberado con cada pago """


# tuplas -------------------------------------------

"""son inmutables no se pueden modificar
contiene distintos tipos de datos
si se requiere añadir un dato se debe de convertir a una lista
se puede acceder la tupla indicando el indice de la misma
para recorrer la tupla usamos la funcion
las duplas permiten duplicar valores
"""

week_days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
print(type(week_days)) 
print(dir(week_days)) #dir es para ver los metodos que tiene el objeto
print(len(week_days)) #len es para saber el tamaño de la tupla
print(week_days[0]) #para impirmir solo la posicion deseada
print(week_days[1])
print(week_days[2])
print(week_days[3])
print(week_days[4])
print(week_days[5])
print(week_days[6])

print(week_days[:6]) #esto es un slicing para imprimir hasta el indice que le ponga
print(week_days[:0])
print(week_days[:-1])

for i in range (len(week_days)): #ciclo for para recorrer la tupla
    print(week_days[i])

week_days_list = list(week_days) #convertimos la tupla a una lista para poderla modificar
print(type(week_days_list))
week_days_list.append("Holyday")
print( week_days_list[:8])
week_days_list.pop()
print(week_days_list[:8])
week_days = tuple(week_days_list)
print(type(week_days))

# Conjuntos----------------------------

"""son inmutables
son desordenados
no son indexados
no permite duplicar"""

vowels = {"a", "e", "i", "o", "u"}
print(len(vowels))
print(type(vowels))
for i in vowels: #para recorrer un conjunto
    print(vowels)
vowels.add("@") #añadiendo una nueva vocal al conjunto
for i in vowels:
    print(vowels)
vowels.remove("@") #removiendo una vocal existente
for i in vowels:
    print(vowels)
vowels.pop() #elimina cualquier dato ya que no tienen indice
for i in vowels:
    print(vowels)

# Diccionario --------------------------

"""los diccionarios permiten tener clave valor
son cambiables
no permite claves duplicadas 
son ordenados
permiten agregar, remover items
son iterables
poseen distintos metodos para manipular los datos
admiten distintos tipos de datos"""

Users = {
    "Name":"Pepito",
    "Last_name":"Perez",
    "Age": 25
}
print(Users) #para imprimir clave y valor
print(Users.keys()) #para impirmir las claves
print(Users.values()) #para imprimir los valores
print(type(Users))
print(Users.get("Name")) #buscando 
print(Users["Name"])

Users ["Mail"] = "pepito@mail.com" #agregando una nueva clave y valor al diccionario
print(Users.keys())
print(Users.get("Mail"))

Users.update({"Mail":"pperez@mail.com"}) #actualizando el valor de una clave
print(Users.keys())
print(Users.get("Mail"))

Users.pop("Name") #para remover una clave
print(Users.keys())
Users.popitem()
print(Users.keys())

for x,y in Users.items():
    print(x,y)

Users1 = {  #forma 1 de hacer un diccionario de diccionario
    "User1":{
        "name":"juan",
        "age":12
    },
    "User2":{
        "name":"Maria",
        "edad":15
    },
    "User3":{
        "name":"julia",
        "edad":18
    }
}

Student1 = {"nota1":4.2, "nota2":4.3} #forma 2 de hacer un diccionario de diccionario
Student2 = {"nota1":4.4, "nota2":4.3}
Student3 = {"nota1":4.5, "nota2":4.1}

Students = {
    "student1":Student1,
    "student2":Student2,
    "student3":Student3
}

print(Students)

# Funciones --------------------------------------------------

saludo = "hola python"

def printsomething (saludo):
    print (saludo)

printsomething (saludo)

# calcular la masa corporal

def calculeImc (peso, altura):
    imc = peso / (altura*altura)
    print (imc)

calculeImc (100,1.90)

salario = 1200000

def calculeHealth (salario):
    eps = salario*0.04
    return eps

def calculePension (salario):
    pension = salario*0.04
    return pension

def calculeSalaryNeto (salario, eps,pension):
    salarioNeto = salario-eps-pension
    print (salarioNeto)

eps = calculeHealth (salario)
pension = calculePension (salario)
calculeSalaryNeto (salario, eps, pension)

def calculeSalaryNeto2(Salario):
    eps = calculeHealth (salario)
    pension = calculePension (Salario)
    Salario_neto = salario-eps-pension
    print (Salario_neto)

calculeSalaryNeto2(salario)

def register (*items):
    print (f"los datos son:  {items [:4]}")

register("pepito","perez",25,"pepito@mail.com")

def calculePayNomine (salario):
    pagoEps = lambda sal : salario * 0.04
    pagoPension = lambda sal : salario * 0.04
    salarioNeto = salario - pagoEps(salario) - pagoPension(salario)
    return salarioNeto

print(calculePayNomine(1000000))

"""Bancolombia requiere calcular los salarios de su nueva starup Pagui
-registrar id,nombre,apellido.cargo,area,salario
-requiere listar a los empleados
-calcular el salario neto de cada uno, teniendo en cuenta que si gana <2 SMLV se le paga aux transporte
-imprimir colilla de pago
-un empleado podra ingresar al sistema y buscar su colilla de pago e imprimirla
-un analista de recursos humanos podra visualizar todos los empleados y todas las colillas, ademas buscar por empleado
-pago total nomina"""

#ejemplo 1

class Empleado:
    def __init__(self, id, nombre, apellido, cargo, area, salario):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cargo = cargo
        self.area = area
        self.salario = salario

class Nomina:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def listar_empleados(self):
        for empleado in self.empleados:
            print(f"ID: {empleado.id}, Nombre: {empleado.nombre} {empleado.apellido}, Cargo: {empleado.cargo}, Área: {empleado.area}, Salario: {empleado.salario}")

    def calcular_salario_neto(self, empleado):
        smlv = 908526  # Valor del salario mínimo legal vigente (SMLV) en Colombia
        if empleado.salario < 2 * smlv:
            salario_neto = empleado.salario + 106454  # Sumar auxilio de transporte
        else:
            salario_neto = empleado.salario
        return salario_neto

    def imprimir_colilla_pago(self, empleado):
        salario_neto = self.calcular_salario_neto(empleado)
        print(f"Colilla de Pago para {empleado.nombre} {empleado.apellido}:")
        print(f"ID: {empleado.id}")
        print(f"Cargo: {empleado.cargo}")
        print(f"Área: {empleado.area}")
        print(f"Salario Bruto: {empleado.salario}")
        print(f"Salario Neto: {salario_neto}")

    def buscar_empleado_por_id(self, id):
        for empleado in self.empleados:
            if empleado.id == id:
                return empleado
        return None

    def visualizar_todos_los_empleados(self):
        for empleado in self.empleados:
            self.imprimir_colilla_pago(empleado)

# Ejemplo de uso
nomina = Nomina()
empleado1 = Empleado(1, "Juan", "Perez", "Analista", "Recursos Humanos", 1500000)
empleado2 = Empleado(2, "Maria", "Lopez", "Desarrollador", "Tecnología", 1800000)

nomina.agregar_empleado(empleado1)
nomina.agregar_empleado(empleado2)

print("Lista de Empleados:")
nomina.listar_empleados()

empleado_a_buscar = nomina.buscar_empleado_por_id(1)
if empleado_a_buscar:
    nomina.imprimir_colilla_pago(empleado_a_buscar)
else:
    print("Empleado no encontrado.")

print("Visualizar todos los empleados y colillas:")
nomina.visualizar_todos_los_empleados()

#Ejemplo 2

empleados = []
smlv = 908526  # Valor del salario mínimo legal vigente (SMLV) en Colombia

def registrar_empleado():
    id = int(input("Ingrese el ID del empleado: "))
    nombre = input("Ingrese el nombre del empleado: ")
    apellido = input("Ingrese el apellido del empleado: ")
    cargo = input("Ingrese el cargo del empleado: ")
    area = input("Ingrese el área del empleado: ")
    salario = float(input("Ingrese el salario del empleado: "))
    empleados.append({"id": id, "nombre": nombre, "apellido": apellido, "cargo": cargo, "area": area, "salario": salario})

def listar_empleados():
    print("Lista de Empleados:")
    for empleado in empleados:
        print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']} {empleado['apellido']}, Cargo: {empleado['cargo']}, Área: {empleado['area']}, Salario: {empleado['salario']}")

def calcular_salario_neto(salario):
    if salario < 2 * smlv:
        salario_neto = salario + 106454  # Sumar auxilio de transporte
    else:
        salario_neto = salario
    return salario_neto

def imprimir_colilla_pago(empleado):
    salario_neto = calcular_salario_neto(empleado["salario"])
    print(f"Colilla de Pago para {empleado['nombre']} {empleado['apellido']}:")
    print(f"ID: {empleado['id']}")
    print(f"Cargo: {empleado['cargo']}")
    print(f"Área: {empleado['area']}")
    print(f"Salario Bruto: {empleado['salario']}")
    print(f"Salario Neto: {salario_neto}")

def buscar_empleado_por_id(id):
    for empleado in empleados:
        if empleado["id"] == id:
            return empleado
    return None

def visualizar_todos_los_empleados():
    for empleado in empleados:
        imprimir_colilla_pago(empleado)

def pago_total_nomina():
    total_nomina = sum(empleado["salario"] for empleado in empleados)
    return total_nomina

while True:
    print("\nMenú de Opciones:")
    print("1. Registrar Empleado")
    print("2. Listar Empleados")
    print("3. Calcular Salario y Imprimir Colilla")
    print("4. Visualizar Todos los Empleados y Colillas")
    print("5. Pago Total de Nómina")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registrar_empleado()
    elif opcion == "2":
        listar_empleados()
    elif opcion == "3":
        id = int(input("Ingrese el ID del empleado: "))
        empleado = buscar_empleado_por_id(id)
        if empleado:
            imprimir_colilla_pago(empleado)
        else:
            print("Empleado no encontrado.")
    elif opcion == "4":
        visualizar_todos_los_empleados()
    elif opcion == "5":
        total_nomina = pago_total_nomina()
        print(f"Total de Nómina: {total_nomina}")
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

#Clases en py

class Vehiculo:
    def _init_(self,marca,modelo,color,ruedas,ref):
        self.marca=marca
        self.modelo=modelo
        self.color=color
        self.ruedas=ruedas
        self.ref=ref
        
    def ver_vehiculo(self):
        print(f"Marca: {self.marca} \n Modelo: {self.modelo} \n Color: {self.color}")
    
moto=Vehiculo("Yamaha",2023,"Negro",2,"N-Max 150")

carro=Vehiculo("Mazda",2024,"Blanco",4,"CX-5")

def ver_vehiculo(self):
    print(f"Marca: {self.marca} \n Modelo{self.modelo} \n Color{self.color}")

print(carro.marca)
print(moto.marca)

#También se puede sobreescribir el atributo
carro.marca="Renault"
print(carro.marca)

# Ahora vamos a crear un metodo para ver el vehiculo y sus atributos

carro.ver_vehiculo()
moto.ver_vehiculo()

class Persona:
    def __init__(self, id, nombre,apellido, correo, password):
        self._id = id
        self._Nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._password = password

        @id.setter
        def id(self, id):
            self._id = id

        @property
        def id(self):
            return self._id
        
        @nombre.setter
        def nombre (self, nombre):
            self._mombre = nombre
        
        @property
        def nombre(self):
            return nombre
        
        @apellido.setter
        def apellido (self, apellido):
            self._apellido = apellido

        @property
        def apellido (self):
            return apellido
        
        @correo.setter
        def correo (self, correo):
            self._correo = correo

        @property
        def correo (self):
            return correo

        @password.setter
        def password (self, password):
            self._password = password

        @property
        def password (self):
            return password

#vamos a generar los metodos, ppara registrar los usuarios e impirmir el registro

    def registrar_usuario(self):
        id = input(f"Ingrese el id del usuario")
        nombre = input(f"Ingrese el nombre del usuario")
        apellido = input(f"Ingrese el apellido del usuario")
        correo = input(f"Ingrese el correo del usuario")
        password = input(f"Ingrese la contraseña del usuario")

    def imprimir_registro (self):
        print (f"Id: {self._id} nombre {self._nombre} apellido {self._apellido} correo {self._correo} contraseña {self._password}")


#esto se debe de llevar a otra hoja para poder heredar
from Persona import Persona 
class Empleado (Persona): 
    def __init__(self, id, nombre, apellido, correo, password, cargo, salario, tipo_contrato):
        super().__init__(id, nombre, apellido, correo, password)
        self._cargo = cargo
        self._salario = salario
        self._tipo_contrato

        @property
        def cargo(self):
            return self._cargo
        @cargo.setter
        def cargo (self, cargo):
            self._cargo = cargo
            
        @property
        def salario(self):
            return self._salario
        @salario.setter
        def cargo (self, salario):
            self._salario = salario

        @property
        def tipo_contrato(self):
            return self._tipo_contrato
        @tipo_contrato.setter
        def tipo (self, tipo_contrato):
            self._tipo_contrato = tipo_contrato

#vamos a sobrescribir los metodos

def registrar_usuario(self):
    id = input(f"Ingrese el id del usuario")
    nombre = input(f"ingrese el nombre del usuario")
    apellido = input(f"ingrese el apellido del usuario")
    correo = input(f"ingrese el correo del usuario")
    password = input(f"ingrese el password del usuario")
    cargo = input(f"ingrese el cargo del usuario")
    salario = input(f"ingrese el salario del usuario")
    tipo_contrato = input(f"ingrese el tipo de contrato del usuario")

def imprimir_registro (self):
    super().imprimir_registro() #me saca error por que se tiene que hacer en otra hoja
    print(f"cargo: {self._cargo} salario {self._salario} tipo contrato {self.tipo_contrato}")


#se crea otra hoja y se hace el siguiente codigo

from Empleado import Empleado

from persona import persona

persona1 = persona

id = 1

persona1._id(id)

persona1.imprimir_persona
