import random
try:
    with open("game-pref.txt", "r+") as con:
        defult = con.read()
        

except FileNotFoundError:
    with open("game-pref.txt", "w") as con:
        con.write("7")
        defult = 7

defult = int(defult)




def main(times_left=defult):
    print("Guess a number from 1 to 100")

    tal = random.randint(1, 100)

    while True:
        try:
            ins = int(input("Type Your answer here --> "))    
        except ValueError:
            print("Your only allowed to type numbers")
            continue
        if ins == tal:
            print(f"Nice you guessed the right number {tal} with {times_left} trys left")
            break
        elif times_left == 1:
            print(f"Sorry you don't have any more guesses, heres the number {tal}")
            break
        elif ins < tal:
            print(f"you guessed {ins} but you need to go a little higher")
        else:
            print(f"you guessed {ins} but you have to go a little lower")

        times_left -= 1



print("If you don't enter anything, the game will start automatically with 7 attempts. If you want to change this, go to Settings.")
print("Settings")
print("Game")

ins = input("Type here --> ")

if ins == "Settings":
    inputs = input("how many guesses do you want --> ") 
    with open("game-pref.txt", "w") as con:
        con.write(inputs)
    main(int(inputs))
        

else:
     main()
       
