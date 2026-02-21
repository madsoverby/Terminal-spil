import random
try:
    with open("overby-spil-pref.txt", "r+") as con:
        defult = con.read()
        

except FileNotFoundError:
    with open("overby-spil-pref.txt", "w") as con:
        con.write("7")
        defult = 7

defult = int(defult)


#Det her er main funtionen af spillet

def main(gange_tilbage=defult):
    print("Gæt et tal fra 1 til 100")
    print("Lidt lige som tampen brænder jeg siger om det er højere eller lavere")

    tal = random.randint(1, 100)

    while True:
        try:
            ins = int(input("du skal bare skrive dit tal lige her --> "))    
        except ValueError:
            print("Du må kun skrive tal")
            continue
        if ins == tal:
            print(f"du  klarde det du gættede nemelig {tal}")
            break
        elif gange_tilbage == 1:
            print(f"du havde ikke flere gange tilbage tallet var {tal}")
            break
        elif ins < tal:
            print(f"du gættede {ins} men du skal lige lidt højere")
        else:
            print(f"du gættede {ins} men du skal lige lidt lavere")

        gange_tilbage -= 1

#hovedmenuen

print("Hvis du ikke skriver noget går den til spil automatisk med 7 førsøg hvis du vil ændre så gå ind i Indstillinger")
print("Indstillinger")
print("Spil")

ins = input("Skriv her --> ")

if ins == "Indstillinger":
    inputs = input("hvor mange gange skal du have hver gang --> ") 
    with open("overby-spil-pref.txt", "w") as con:
        con.write(inputs)
    main(int(inputs))
        

else:
     main()
       