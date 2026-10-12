#VS, XR , MA,               ab

#Variables for the game (All of us)
fragment1 = False
fragment2 = False
fragment3 = False
fragment4 =False
win = False


#introduction VS
left = "village"
right = "woods"
investigate = ("You ended up further investigating. You go further into the forest and stumble upon this yellow ball. He says ""Hey its me its verity!"" your a little off put cause he broke out into song.. After the song ended he said ""im kinda hungry.."" he ended up eating you for lunch. YOU DIED.")
village_choice1=("You go towards the village, its empty. Your kind of confuse, knock on doors and call out. Theres no answer. While your on your way to leave you stumble upon this door thats slightly opened. You go inside.")

print("You slipped at the arcade! You hit you head pretty hard.. now that youve woken up your in minecraft!!! ")
choice1=input(f"""You should explore, go left or go right
     GO left TOWARDS THE VILLAGE   OR   GO right TOWARDS THE WOODS --> """).strip().lower()

if choice1 == "left":
    print("You make your way to the village, while your walking to the village you hear something rustling in the bushes. You ignore it and continue your journey to the village...")
    print(village_choice1)

else:
    print("thats not what i asked for, try again. check for any spelling mistakes.")



if choice1 == "right":
    print("You decide to go to the woods...")

    choice2=input(f"""You make your way towards the woods, you hear some giggling from the bushes beyond.
                                          PICK
                FURTHER investigate?     OR       RUN AWAY TO THE village
""").strip().lower()
if choice2 == "village":
    print(village_choice1)

if choice2 == "investigate":
    print(investigate)

else
    print("thats not what i asked fpr ")
# Room one r(XR)

room1 = ("You made it to the village safely!")
room1choice = input(f"You see a house and the door is open so you go in and investigate. You see a chest, would you like to open it or would you like to leave")

if room1choice == "open":
    print("you found fragment of a key to unlock something!")
    fragment1 = True
elif room1choice == "leave":
    print("You decided to")
    fragment1 = False
else:
    print("Thats no an option")
    




# Room 3 and functions(MA)
guess = 0

while guess != 67:
    guess = int(input("Guess a number from 1 to 67: "))

    if guess < 1 or guess > 67:
        print("Pick a number between 1 and 67!")
    elif guess < 67:
        print("Too low! Try again.")
    elif guess > 67:
        print("Too high! Try again.")
    else:
        break

print("Correct! Your first number is 67.")


guess = 0

while guess != 41:
    guess = int(input("Guess a number from 1 to 67: "))

    if guess < 1 or guess > 67:
        print("Pick a number between 1 and 67!")
    elif guess < 41:
        print("Too low! Try again.")
    elif guess > 41:
        print("Too high! Try again.")

print("Correct! Your second number is 41.")

code = "67" + "41"

print("you have the two pieces of code. Use then to unlock the chest")

chest_guess = input("Enter the four-digit chest code: ")

while chest_guess != code:
    print("Wrong code! Try again.")
chest_guess = input("Enter the four-digit chest code: ")

print("The chest opens. inside a key fragment is found")


# Room 4 and functions (AB) it will be a three number guessing game with a 2 minute timer if timer runs out of time you get death screened.
room4=("you have 3 of the four fragments. tramatized and stunned you sway slightly as you think about how you need to keep moving. you take a step looking for the last building that will have the next fragment you stumble, almost collapsing, you just have to keep on pushing. step after step, all you can think about is home, as you take another, you wonder if you willl be able to survive what happended here, if its a dream, reality, or somthing beyond that, you see the final house. it got this radient humm coming from it as you walk closer your hear the verity scream out. ")





# ending scene(depends on choices) VS

