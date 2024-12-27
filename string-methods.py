texto = "hola muNdo"
texto_con_espacios = "       texto con espacios        "
texto_separado = "Python,JavaScript,Django,React"
lista = ["Hola","Juan","Carlos"]
numeros = "123456"
letras = "ABC"
espacio = "   "
repetición = "Manzana,Naranja,Manzana,Limon"


print("capitalize:", texto.capitalize()) # Convierte la primera letra en mayúscula el resto en minúscula
print("upper:", texto.upper()) # Convierte le texto entero en mayúsculas
print("lower:",texto.lower()) # Convierte todo el texto en Minúsculas
print("Strip:", texto_con_espacios.strip()) # Elimina los espacios al comienzo  y al final
print("replace:", texto_con_espacios.replace("espacios","gracia")) # reemplaza una palabra por otra
print("split:", texto_separado.split(",")) # Separar texto en items de una lista
print("join:", ",".join(lista)) # Junta los items de una lista en una string 
print("find:",repetición.find("Manzana")) # Muestra la posición donde arranca el texto ingresado
print("rfind:",repetición.rfind("Manzana")) # Muestra la  ultima posición donde arranca el texto ingresado
print("index:",texto.index("muNdo")) # Muestra la posición donde arranca el texto ingresado
print("startwith:",texto.startswith("Adiós")) #Indica si comienza o no con la palabra ingresada 
print("endswith:",texto.endswith("muNdo")) #Indica si finaliza o no con la palabra ingresada
print("isdigit:", numeros.isdigit()) # Indica si todos los caracteres son números o no (espacios NO SON NÚMEROS)
print("isalpha:",texto.isalpha()) # Indica si todos los caracteres son letras o no (Espacios no son letras) 
print("isalphnum:", letras.isalnum()) #Indica si todos los caracteres son alfanuméricos o no (espacios no son letras ni numeros)
print("isspace:",espacio.isspace()) # Indica si el string solo esta hecho de espacios
print("count:",repetición.count("Manzana")) #Indica cuantas veces se repite la palabra ingresada

