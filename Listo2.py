"""Mision Operacion Strix Final"""
print("Central intelligence Agency")
print("****************************")
print("")
print("Welcome Agent Twilight")

def wordfill(word,size):
    if len(word) % 2 == 0:
        result = ' ' * int((size - len(word))/2) + word + ' ' * int((size - len(word))/2)
    else:
        result = ' ' * int((size - len(word))/2) + word + ' ' * int((size - len(word))/2) + ' '

    return result 

#Cifrado de Cesar 

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def normalize_text(text):
    result = ""
    text = text.replace(" ", "").upper()
    for c in text:
        if c in alphabet:
             result+=c
    return result

def get_desp(char):
    return (ord(char.upper())-65)

def caesar_cipher(text,desp):
    cipher = ""
    for i in range(len(text)):   #Para cada letra del texto
        char = text[i]
        if (char.islower()):
            cipher += chr((ord(char) + desp - 97) % 26 + 97) #97 primera letra minuscula (a)
        else:
            cipher += chr((ord(char) + desp-65) % 26 + 65)  # Prima letra mayuscula (A) -> EJ caesar 3: (A(65) + 3-65) -> 3 % 26 = 3+65 = 68(D)   
    return cipher

def caesar_decipher(text,desp):
    plain = ""
    for i in range(len(text)):
        char = text[i]
        if (char.islower()):
            plain += chr((ord(char) -97-desp) % 26 + 97)
        else:
            plain += chr((ord(char) -65-desp) % 26 + 65)
    return plain

def vigenere_cipher(plain,clave):
    result = ""
    for i in range(0,len(plain)): #Para todo el texto
        desp = get_desp(clave[i % len(clave)]) #Obtenemos el desplazamiento asociado a la clave
        result +=(caesar_cipher(plain[i],desp)) #Ciframos la letra con caesar y la añadimos al string
    return result

def vigenere_decipher(text,clave):
    result = ""
    for i in range(0,len(text)): #Para todo el texto
        desp = get_desp(clave[i % len(clave)]) #Obtenemos el desplazamiento asociado a la clave
        result +=(caesar_decipher(text[i],desp)) #desciframos la letra con caesar para el desplazamiento dado 
    return result

def add_cipher_material(material, codigo):
    with open('ciainventary.txt', 'a') as f:
        f.write( '|' + vigenere_cipher(material,'HLA') + '|'+codigo+ '|\n')

def read_descipher_material():
    with open('ciainventary.txt', 'r') as f:
        for line in f.readlines():
            if not ('_' in line):
                print(vigenere_decipher(line.split('|')[1], 'HLA'), '')
                print(line.split('|')[2])
    
stock_list = []
opcion =""

while opcion!=6:
    print()
    print("\t.:MENU:.")
    print("******************")
    print("1. Add a material in the stock database: ")
    print("2. Remove material in the stock database: ")
    print("3. Edit a material in the stock database:  ")
    print("4. View the stock database materials: ")
    print("5. Want to view inventory database materials in Json file, .txt file: ")
    print("6. Exit")
    opcion = int(input("Select an option: "))
    print()

    if opcion==1:
        follow = True 
        stock_list =[]
        k=1
        while follow:
            name_of_the_material = input("Enter the name of the material: ")
            code = input("Enter the code of the material: ")
            

            if k ==1:
              maxi=len(name_of_the_material)
              valor=name_of_the_material
              codigo=code
            else: 
              cadena=len(name_of_the_material)
              if (cadena > maxi):
                  maxi=len(name_of_the_material)
                  for i in stock_list:
                         new_name= i["name"].ljust(cadena)
                         i["name"]=new_name

            stock_list.append({"name": name_of_the_material, "code": code})
            follow_text = input("Want to enter other material into the stock? (yes/no)")
            k=k+1

            if follow_text == "no":
                 follow = False
                 for i in stock_list:
                  name = i['name']
                  code = i['code']
                  add_cipher_material(name, code)
           
     
    elif opcion==2:
        for i in stock_list:
            print("\t name:", i["name"])
            print("\tcode:", i["code"])
            
        cont = 0 
        search = input("Introduce the material: ")
        for i in stock_list:
            if search in i.values():
                pos=cont
                bool = input("Want to remove the material(yes/no): ")
                if(bool == "yes"):
                    stock_list.pop(pos)
                else:
                    print("Cancel...")
            cont=cont +1    
            
        else:
            print("Doesn't exit")
        print(stock_list)
    
    elif opcion==3:
        for i in stock_list:
            print("\t name:", i["name"])
            print("\tcode:", i["code"])
            
         
        search = input("Introduce the material: ")
        for i in stock_list:
            if search in i.values():
                
                bool = input("Want to edit the material(yes/no): ")
                if(bool == "yes"):
                    new_name = input("Enter the new name of the material: ")
                    i["name"]=new_name
                    
                else:
                    print("Cancel...")
                    
                bool = input("Want to edit the code(yes/no): ")
                if(bool == "yes"):
                    new_code = input("Enter the new code of the material: ")
                    i["code"]=new_code
                else:
                    print("Cancel...")
                
        print(stock_list)        
        
    elif opcion==4:
        for i in stock_list:
            name = wordfill(i["name"],20)
            code = wordfill(i["code"],20)
            print('|{}|\t{}|\n'.format(name,code))
            print('_'*50 + '\n')
        read_descipher_material()
        

    elif opcion ==5:
        import json
        fileName = "CIA-inventary.json"
        file = open(fileName, "w")
        for i in stock_list:
            name = i['name']
            code = i['code']
            jsonString = i
            jsonString = '{ "name":' + f'"{name}"' + ', ' + '"code":' + f'"{code}"' + '}'
            print(jsonString)
            jsonString = json.loads(jsonString)


            json.dump(jsonString, file)
        file.close()           


    elif opcion==6:
        print("See you later Agent Twilight")
        
    else:
        print("Error, wrong choice of menu") 
    
 
