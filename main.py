import random


def main(gange_tilbgae=5):
    print("gæt et tal fra 1 til 100")
    print("lidt lige som tanken brænder jeg siger om det er højere eller laver")


    ins = int(input("du skal bare skrive dit tal lige her --> "))

    tal = random.randint(1, 100)

    while True:
        if ins == tal:
            print(f"du  klarde det du gættede nemelig {tal}")
            break
        if gange_tilbgae == 0:
            print(f"du havde ikke flere gange tilbage tallet var {tal}")
            break
        if ins < tal:
            print(f"du gættede {ins} men du skal lige lidt højre")
        if ins > tal:
            print(f"du gættede {ins} men du skal lige lidt lavere")
        gange_tilbgae = gange_tilbgae - 1
        ins = int(input("prøv igen --> "))

print("hvis du ikke skriver noget gård den til spil automatisk")
print("Indstillinger")
print("Spil")

ins = input("Skriv her --> ")

if ins == "Indstillinger":
    main(int(input("hvormaneg gange skal du have -->")))
else:
    main()