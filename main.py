import random
try:
    with open("overby-spil-pref.txt", "r+") as con:
        defult = con.read()
        

except FileNotFoundError:
    with open("overby-spil-pref.txt", "w") as con:
        con.write("7")
        defult = 7

defult = int(defult)


def main(gange_tilbage=defult):
    print("gæt et tal fra 1 til 100")
    print("lidt lige som tanken brænder jeg siger om det er højere eller laver")

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
            print(f"du gættede {ins} men du skal lige lidt højre")
        else:
            print(f"du gættede {ins} men du skal lige lidt lavere")

        gange_tilbage -= 1

print("hvis du ikke skriver noget går den til spil automatisk med 7 førsøg vis du vil ændre så gå ind i indstillinger")
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
       