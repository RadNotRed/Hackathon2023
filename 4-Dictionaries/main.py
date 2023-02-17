#I cant help with the slang, I dont even know it mtyself - Kevin the antisocial one who doesnt have social medio and therefor this is rigged!
#Apollo 14

print("Welcome to translator bot 001, I will convert certain words into computer tongue and espanol for you.... Actually Ill refrain from computer tongue because 01100010 01101001 01101110 01100001 01110010 01111001 00100000 01101001 01110011 00100000 01110111 01100001 01111001 00100000 01110100 01101111 00100000 01101100 01101111 01101110 01100111 00100000 01110011 01101111 00100000 01001001 00100000 01100001 01100011 01110100 01110101 01100001 01101100 01101100 01111001 00100000 01110111 01101111 01101110 01110100 00100000 01100001 01100100 01100100 00100000 01101001 01110100 00100000 01100001 01110011 00100000 01101001 01110100 00100000 01110111 01101001 01101100 01101100 00100000 01110100 01100001 01101011 01100101 00100000 01110100 01101111 01101111 00100000 01101101 01110101 01100011 01101000 00100000 01110011 01110000 01100001 01100011 01100101 (binary is way to long so I actually wont add it as it will take too much space)")

Spanish = ["colores", "programa", "usar", "facil", "programadora", "numeres", "codificar", "ayudar", "nueve", "si", "calor", "necesitar", "secuencia", "iteracion", "seleccion", "condicion", "mirar", "derecho", "binario", "idioma", "metodo", "entrada", "crear", "factores", "funcionar"]
English = ["colors", "program", "use", "easy", "programer", "numbers", "code", "help", "nine", "if", "hot", "need", "sequence", "iteration", "seclection", "condition", "look", "right", "binary", "language", "method", "input", "create", "factors", "funcion"]

keyword = input("Please enter one of the words that follow to translate: " + str(English) + ":")

counter = 0
while (counter < len(English)):
  if(English[counter] == keyword):
    print("The Spanish translation is: " + str(Spanish[counter]))
  counter += 1