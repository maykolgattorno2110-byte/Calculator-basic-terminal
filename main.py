#dependencias
from logic import *
import time
from os import system
import platform

#COLORES
rojo = "\033[91m"
verde = "\033[92m"
cian = "\033[96m"
amarillo = "\033[93m"
mora = "\033[35m"
negrita = "\033[1m"
reset = "\033[0m"

#LP
PCL = "cls" if platform.system() == "Windows" else "clear"

def Lp():
    system(PCL)

#tuplas
options_3 = (6, 7, 8, 9)
options_1 = (12, 13, 14, 15, 16)
raizes = (12, 13)
salir = ("si", "s", "se", "yes", "yeah", "chi")
quedar = ("no", "n", "nel", "nope")

#dispositivo
sys_p = platform.system()
print(f"dispositivo:{sys_p}")    

#ui principal
print(f"CALCULADORA")
while True:
	print("--")
	print("---ARITMETICA---")
	print("--suma--1")
	print("-")
	print("--resta--2")
	print("-")
	print("--multiplicacion--3")
	print("-")
	print("--division--4")
	print("-")
	print("--potenciacion--5")
	print("-")       
	print("--suma(3)--6")
	print("-")
	print("--resta(3)--7")
	print("-")
	print("--multiplicacion(3)--8")
	print("-")
	print("--division(3)--9")
	print("-")
	print("---AVANZADO---")
	print("--el % de X--10")
	print("-")
	print("--que % es--11")
	print("-")
	print("--raiz cuadrada--12")
	print("-")
	print("--raiz cubica--13")
	print("-")
	print("--area de un circulo--14")
	print("-")
	print("---CONVERSION---")
	print("--C° a F°--15")
	print("-")
	print("--F° a C°--16")
	print("-")
	
	#logica
	try:
		data_1 = int(input(f"--eliga su opcion: "))
			
		if data_1 >= 17 or data_1 <= 0:
			Lp()
			print(f"{rojo}--{reset}")
			print(f"{rojo}--problema:opcion invalida{reset}")
			time.sleep(2)
			continue
			
		data_2 = float(input(f"--eliga el primer numero: "))
		if data_1 not in options_1:
			data_3 = float(input(f"--el segundo: "))
		
		if data_1 in options_3:
		    data_5 = float(input(f"--el tercero: "))		
		
	except ValueError:
		Lp()
		print(f"{rojo}--{reset}")
		print(f"{rojo}--problema:no se permite caracteres{reset}")
		time.sleep(2)
		continue
		
	#logica 2
	try:
		if data_1 == 1:
			print(f"la suma es {cian}{suma(data_2, data_3)}{reset}")
			#suma
		elif data_1 == 2:
			print(f"la resta es {cian}{rest(data_2, data_3)}{reset}")
			#resta
		elif data_1 == 3:
			print(f"la multiplicacion es {cian}{mult(data_2, data_3)}{reset}")
			#multiplicacion
		elif data_1 == 4:
			print(f"la division es {cian}{div(data_2, data_3)}{reset}")
			#division
		elif data_1 == 5:
			print(f"la potenciacion es {cian}{pot(data_2, data_3)}{reset}")
			#potenciacion
		elif data_1 == 6:
			print(f"la suma es {cian}{suma(data_2, data_3, data_5)}{reset}")
			#suma de 3
		elif data_1 == 7:
			print(f"la resta es {cian}{rest(data_2, data_3, data_5)}{reset}")
			#resta de 3
		elif data_1 == 8:
			print(f"la multiplicacion es {cian}{mult(data_2, data_3, data_5)}{reset}")
			#multiplicacion de 3
		elif data_1 == 9:
			print(f"la division es {cian}{div(data_2, data_3, data_5)}{reset}")
			#division de 3
		elif data_1 == 10:
			print(f"el {data_3}% de {data_2} es {cian}{cp(data_2, data_3)}{reset}")
			#el % de X es
		elif data_1 == 11:
			print(f"{data_2} de {data_3} es {cian}{qpe(data_2, data_3)}%{reset}")
			#que % es
		elif data_1 == 12:
			print(f"la raiz cuadrada es {cian}{raiz_1(data_2)}{reset}")
			#raiz cuadrada √
		elif data_1 == 13:
			print(f"la raiz cubica es {cian}{raiz_2(data_2)}{reset}")
			#raiz cubica ³√
		elif data_1 == 14:
			print(f"el area es {cian}{area(data_2)}{reset}")
			#area •
		elif data_1 == 15:
			print(f"la conversion de C° a F° es {cian}{ctf(data_2)}{reset}")
			#C° a F°
		elif data_1 == 16:
			print(f"la conversion de F° a C° es {cian}{ftc(data_2)}{reset}")
			#F° a C°
			
	except ValueError:
		Lp()
		print(f"{rojo}--{reset}")
		print(f"{rojo}--problema:no se permiten negativos en raices{reset}")
		time.sleep(2)
		continue
	except ZeroDivisionError:
	    Lp()
	    print(f"{rojo}--{reset}")
	    print(f"{rojo}--problema:No se puede dividir entre cero{reset}")
	    time.sleep(2)
	    continue
	except OverflowError:
	       Lp()
	       print(f"{rojo}--{reset}")
	       print(f"{rojo}--problema:has superado el limite de memoria{reset}")
	           
	#salida	
	data_4 = input(f"{amarillo}--desea salir? si/no: {reset}").lower()

	if data_4 in salir:
		print("--")
		print("--")
		break
	elif data_4 in quedar:
		print("--")
		print("--")