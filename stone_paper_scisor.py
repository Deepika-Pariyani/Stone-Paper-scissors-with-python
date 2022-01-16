import random
while True:
    inp = input("Enter R for rock\nEnter P for Paper\nEnter S for Scissors :- ")
    inp = inp.upper()
    a = ["Rock","Paper","Scissors"]
    c = random.choice(a)
    if inp == "R" :
       if c == "Paper":
          print(f"{c}\nYou lost ")
       elif c == "Scissors":
          print(f"{c}\nYou won ")
    elif inp == "P":
       if c == "Scissors":
          print(f"{c}\nYou lost ")
       elif c == "Rock":
          print(f"{c}\nYou won ")
    elif inp == "S":
       if c == "Rock":
          print(f"{c}\nYou lost ")
       elif c == "Paper":
          print(f"{c}\nYou won ")
    else: 
        print("Enter valid choice between rock paper and scissors")
    cont = input("Continue y/n? - ").upper()
    while cont != "Y" and cont != "N":
           print("Enter valid choice")
           cont = input("Continue y/n? - ").upper()
           if cont == "N":
              break