#Adventure game: VS, XR, MA, AB

# Variables for the game
fragment1 = False
fragment2 = False
fragment3 = False
key_fragments = 0

# Introduction VS
left = "village"
right = "woods"
investigate = ("You ended up further investigating. You go further into the forest and stumble upon this yellow ball. "
"He says: Hey, it's me, it's Verity! You are a little off put because he breaks out into song. "
"After the song ends he says: I'm kinda hungry... and ends up eating you for lunch. YOU DIED.")

village_choice1 = ("You go towards the village and it's empty. You are confused and knock on doors and call out. "
"There is no answer. While you are leaving, you stumble upon a door that is slightly opened. "
"You go inside.")

while True:
    fragment1 = False
    fragment2 = False
    fragment3 = False
    key_fragments = 0

    print("You slipped at the arcade! You hit your head pretty hard... now that you've woken up, you're in Minecraft!")
    choice1 = input(
        """You should explore. Go left or go right.
     GO left TOWARDS THE VILLAGE   OR   GO right TOWARDS THE WOODS --> """).strip().lower()

    if choice1 == "left":
        print("You make your way to the village, while walking you hear something rustling in the bushes. You ignore it and continue your journey.")
        print(village_choice1)

# Room 1 and functions (XR)
        print("You end up walking into a small house. There you see that there is a chest "
              "and you decide to go up to it and see what it has inside to see if you will find "
              "anything that will get you out of this nightmare. You go up to the chest and see that "
              "it's locked. You then see a note that says that you have to enter the right minecraft "
              "monster so that you could open the chest. You have 3 tries to guess the right monster.")
        correct_monster = "enderman"
        attempts = 0

        while attempts < 3 and not fragment1:
            room1choice = input("Guess a minecraft monster to open the chest: ").strip().lower()

            if room1choice == correct_monster:
                print("Good job! You guessed the right monster and the chest opened. You found a key fragment inside.")
                fragment1 = True
                key_fragments += 1
            else:
                attempts += 1
                print("wrong guess the chest is still locked. Try guessing again.")

        if not fragment1:
            print("You run out of tries and now you must leave the house. Your now back at the beginning.")
# VS
    elif choice1 == "right":
        print("You decide to go to the woods...")
        choice2 = input(
            """You make your way towards the woods, you hear some giggling from the bushes beyond.
                                          PICK
                FURTHER investigate?       OR       RUN AWAY TO THE village""").strip().lower()

        if choice2 == "village":
            print(village_choice1)
        elif choice2 == "investigate":
            print(investigate)
            print("You died. Start over.")
            play_again = input("Do you want to play again? (y/n): ").strip().lower()
            if play_again == "y":
                print("Restarting the game...")
                continue
            else:
                print("Thanks for playing!")
                break

    # Room 2 and functions (MA)
    print("From the village you run to the woods and in the woods you find a chest with a four digit code lock. "
          "Next to the lock is a piece of paper that looks like this '_74_' and you have to guess two different numbers. "
          "Both numbers are between 10 and 67. You need to hurry or Verity will catch you.")

    print("Now guess the first number.")
    first_guess = 0
    while first_guess != 67:
        first_guess = int(input("Guess a number from 10 to 67: "))

        if first_guess < 10 or first_guess > 67:
            print("Pick a number between 10 and 67!")
        elif first_guess < 67:
            print("Too low")
        elif first_guess > 67:
            print("Too high")
        else:
            print("you got it! Your first number is 67")

    print("time to guess the second number")
    second_guess = 0
    while second_guess != 41:
        second_guess = int(input("Guess a number from 10 to 67: "))

        if second_guess < 10 or second_guess > 67:
            print("Pick a number between 10 and 67!")
        elif second_guess < 41:
            print("Too low")
        elif second_guess > 41:
            print("Too high")
        else:
            print("You got it! Your second number is 41")

    code = "6741"
    print("You have the two pieces of code. Use them to unlock the chest.")

    chest_guess = input("Enter the four digit chest code: ").strip()
    while chest_guess != code:
        print("Wrong. Try again.")
        chest_guess = input("Enter the four-digit chest code: ").strip()

    if chest_guess == code:
        print("The chest opens and you find a key fragment inside. You take it and continue your journey.")
        fragment2 = True
        key_fragments += 1

    # Room 3 and functions (AB)
    room3 = (
        "You have 2 of the 3 fragments. Traumatized and stunned, you sway slightly as you think about how "
        "you need to keep moving. You take a step looking for the last building that will have the next fragment. "
        "You stumble, almost collapsing, but keep pushing. Step after step, all you can think about is home. "
        "As you take another, you wonder if you will be able to survive what happened here. "
        "You see the final house. It has a radiant hum coming from it. As you walk closer, you hear the demon scream. "
        "It sounds like a sonic boom as you fall to your knees, clasping your ears, wincing. "
        "You run to the house as you hear it walking behind you. You open the door and slam it shut, "
        "and you see the final fragment locked behind a glass case with a key lock on the front. "
        "You hear it banging on the door. You only have limited time before it breaks in."
    )
    print(room3)

    bed = "You check under the bed. You find nothing there. He bangs on the door. What next?"
    chest = "You open the chest and find nothing. This house was clearly abandoned. It bangs on the door and yells, try again."
    deskdrawer = "You open the drawer and there is nothing there. You hear a bang and a screech from it. Try again."
    rug = "You look under the rug. You found the key!"
    key_found = False

    room3_choice = input(
        "You look around the room. There are only a couple of places you can check for a key. "
        "There is a bed, a chest, a rug, and a desk drawer. Which do you check? "
    ).strip().lower()

    if room3_choice == "bed":
        print(bed)
    elif room3_choice == "chest":
        print(chest)
    elif room3_choice == "deskdrawer":
        print(deskdrawer)
    elif room3_choice == "rug":
        print(rug)
        key_found = True
    else:
        print("That's not a valid place to search.")

    if key_found:
        fragment3 = True
        key_fragments += 1

    # Ending scene (VS)
    if key_fragments >= 3:
        print(
            """You managed to find the final key fragment! You run over to the portal with your key.
        After unlocking the chest, you find the portal activator. You use it and successfully make it to the real world!

                                                         GOOD ENDING"""
        )
    else:
        print(
            """Unfortunately, you did not find the final key fragment. Due to this, you are struggling to run away from Verity.
                            He turns evil and starts chasing you. Sadly, your running cannot last forever.
                                                               BAD ENDING"""
        )

    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again != "y":
        print("Thanks for playing!")
        break
