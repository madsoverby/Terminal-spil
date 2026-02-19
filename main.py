import random

print("gæt et tal fra 1 til 100")
print("lidt lige som tanken brænder jeg siger om det er højere eller laver")

antal_gæt = int(input("skrive hvor mange forså du vil ha -->  "))
gange_tilbgae = antal_gæt

ins = int(input("du skal bare skrive dit tal lige her --> "))

tal = random.randint(1, 100)

while True:
    if ins == tal:
        print(f"du  klarde det du gættede nemelig {tal}")
        break
    if gange_tilbgae == 0:
        print("du havde ikke flere gange tilbage")
        break
    if ins < tal:
        print(f"du gættede {ins} men du skal lige lidt højre")
    if ins > tal:
        print(f"du gættede {ins} men du skal lige lidt lavere")
    gange_tilbgae = gange_tilbgae - 1
    ins = int(input("prøv igen --> "))
