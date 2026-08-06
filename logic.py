from math import pi, sqrt, cbrt


#--- SUMA + ---

def suma(*numbers):
	return sum(numbers)
	
#--- RESTA - ---

def rest(*numbers):
	total = numbers[0]
	for n in numbers[1:]:
	    total -= n
	return total
	    

#--- MULTIPLICACION * ---

def mult(*numbers):
	total = 1
	for n in numbers:
	    total *= n
	return total
	
#--- DIVISION / ---

def div(*numbers):
	total = numbers[0]
	try:
	    for n in numbers[1:]:
	        total /= n
	    return total
	except ZeroDivisionError:
	        return "\033[91m--problema:no se permiten 0 en division genio\033[0m"
	        
#--- POTENCIACION ** ---

def pot(data_2, data_3):
	return data_2 ** data_3

#--- PORCENTAJE % ---

def cp(data_2, data_3):
    return data_2 * data_3 / 100

def qpe(data_2, data_3):
    return data_2 / data_3 * 100

#--- RAICES √ ---

def raiz_1(data_2):
    return sqrt(data_2)

def raiz_2(data_2):
   return cbrt(data_2)

#--- AREA • ---

def area(data_2):
    area = pi * (data_2 ** 2)
    return area

#--- GRADOS ° ---

def ctf(data_2):
    return (data_2 * 9/5) + 32

def ftc(data_2):
    return (data_2 - 32) * 5/9
