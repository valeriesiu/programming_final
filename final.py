#VS, XR , MA,               ab

#Variables for the game (All of us)
fragment1 = False
fragment2 = False
fragment3 = False

win = False
key_fragments=3
key_pieces=0

#introduction VS
left = "village"
right = "woods"
investigate = ("You ended up further investigating. You go further into the forest and stumble upon this yellow ball. He says ""Hey its me its verity!"" your a little off put cause he broke out into song.. After the song ended he said ""im kinda hungry.."" he ended up eating you for lunch. YOU DIED.")
village_choice1=("You go towards the village, its empty. Your kind of confuse, knock on doors and call out. Theres no answer. While your on your way to leave you stumble upon this door thats slightly opened. You go inside.")

print("You slipped at the arcade! You hit you head pretty hard.. now that youve woken up your in minecraft! ")
choice1=input(f"""You should explore, go left or go right
     GO left TOWARDS THE VILLAGE   OR   GO right TOWARDS THE WOODS --> """).strip().lower()

if choice1 == "left":
    print("You make your way to the village, while your walking to the village you hear something rustling in the bushes. You ignore it and continue your journey to the village...")
    print(village_choice1)



elif choice1 == "right":
    print("You decide to go to the woods...")

choice2=input(f"""You make your way towards the woods, you hear some giggling from the bushes beyond.
                                          PICK
                FURTHER investigate?       OR       RUN AWAY TO THE village
""").strip().lower()
    
else:
    print("thats not what i asked for")


    if choice2 == "village":
      print(village_choice1)

    if choice2 == "investigate":
     print(investigate)

    else:
     print("thats not what i asked for ")
# Room one r(XR)

room1 = ("You made it to the village safely!")
room1choice = input(f"You see a house and the door is open so you go in and investigate. You see a chest and you have to guess a minecraft monster to open it. Guess a minecraft monster (Type the monsters name all lowercase)")

if room1choice == "ender dragon":
    print("you found fragment of a key to unlock something!")
    fragment1 = True
elif room1choice == "zombie":
    print("you found a fragment of a key to unlock something!")
    fragment1 = True
elif room1choice == "spider":
    print("you found fragment of a key to unlock something!")
    fragment1 = True
else:
    print("Thats no an option")
    
        
        




# Room 2 and functions(MA)
room2 = print("From the village you run to the woods and in the woods you find a chest with a four diget code lock. Next to the lock is  a peice of paper with that looks like this '_74_' and you have to guess two diffrent numbers. And both numbers are 10-67. You need to hurry or verity will catch you")
print("Now guess the first number")
gss = 5
guess = 0

while guess != 67:
    guess = int(input("Guess a number from 10 to 67: "))

    if guess < 10 or guess > 67:
        print("Pick a number between 1 and 67!")
    elif guess < 67:
        print("Too low. Try again.")
        (gss - 1)
    if guess > 67:
        print("Too high. Try again.")
        (gss - 1)
    if gss == 0:
        print("Verity caught up to you. You died")
    if guess == 67:
        print("Correct. Your first number is 67.")
print("It's time to guess the second number now")
guess = 0

while guess != 41:
    guess = int(input("Guess a number from 10 to 67: "))

    if guess < 10 or guess > 67:
        print("Pick a number between 1 and 67!")
    if guess < 41:
        print("Too low. Try again.")
        (gss - 1)
        if gss == 0:
            print("Verity caught up to you. You died")
    if guess > 41:
        print("Too high. Try again.")
        (gss - 1)
        if gss == 0:
            print("Verity caught up to you. You died")
    if guess == 41:
        print("Correct. Your second number is 41.")

code = "67" + "41"

print("you have the two pieces of code. Use them to unlock the chest")

chest_guess = input("Enter the four-digit chest code: ")

while chest_guess != code:
    print("Wrong. Try again.")
chest_guess = input("Enter the four-digit chest code: ")
if chest_guess == code:
    print("The chest opens. inside a key fragment is found")
    fragment2 = True

# Room 3 and functions (AB) it will be a thing where you have to find the key to get out

room3A=True
room3=("you have 2 of the three fragments. tramatized and stunned you sway slightly as you think about how you need to keep moving. you take a step looking for the last building that will have the next fragment you stumble, almost collapsing, you just have to keep on pushing. step after step, all you can think about is home, as you take another, you wonder if you will be able to survive what happened here, if its a dream, reality, or something beyond that, you see the final house. it got this radiant hum coming from it as you walk closer your hear the demon scream out. it sounds like a sonic boom as you fall to your knees, clasping your ears, wincing. You run to the next house as you hear it walking behind you. you open up the door and slam it as you see the final fragment, locked behind a glass case locked with a key lock on the front. you hear it banging on the door. you only have limited time before it comes inside ")
print (f"{room3}")
input(f"you look around the room. There are only a couple places you can check for a key. You're going to have to be fast, as the thing is at the door. There is a bed, a chest, a rug, and a deskdrawer. You can check which one first.  ")
bed= (f"you check under the bed. you find nothing there. He bangs on the door. what next?  ")
chest= (f"you open the chest, to find nothing, this house was clearly abondoned, and it bangs on the door and yells, try again"  )
deskdrawer= (f"you open the drawer, and there is nothing there, as you hear a bang and a screech from it, try again"  )
rug= (f"you look under the rug. you found the key, as it bangs on the door"  )
key = True

if "chest" == input:
    print (f"{chest}")

if "bed" == input:
    print (f"{bed}")

if "deskdrawer" == input:
    print (f"{deskdrawer}")

if "rug" == input:
    print (f"{rug}")
    key=True

if key == True: 
    key_fragments == 3


# ending scene(depends on choices) VS
    if key_fragments==3 is True:
        print("""you managed to find the final key fragment! you run over to the portal with your key. After unlocking a chest you find the portal activator! you use it and succsessfully make it to the real world!
   
                                                                                              GOOD ENDING    """)

    if key_fragments <3 is True:
      print("""unfortunateley you did not find the final key fragment. due to this you were struggling to run away from verity. he turned evil and started chasng after you. sadly for you running cant last forever
                                                                                                 BAD ENDING    """)