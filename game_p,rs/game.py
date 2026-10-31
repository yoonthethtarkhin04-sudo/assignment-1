print("              Welcome to the game             ")
print("              ...................             ")
print(" ")
print(""" 
Rock = R
Paper = P
Scissor = S
      """)
print(" ")

print("Two Player = 2")
print("Three Player = 3")


print(" ")
print(" ")
again = "Y"
while again == "Y":
    player_number = int(input("Enter number of player (2 or 3) : "))
    print(" ")
    choose = [] #ilst
    for i in range(player_number):
        play = input(f"for player {i+1} : Rock or Paper or Scissor? : ").upper()
        choose.append(play)
    

    if player_number == 2:
        p1 = choose[0]
        p2 = choose[1]
        if p1 == p2:
            print("They are Tie!")
            
        elif ((p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P")):
            print("Player 1 Win!")
        else : print ("Player 2 Win!")
        
    #2player

    #3player

    if player_number == 3:
        p1 = choose[0]
        p2 = choose[1]
        p3 = choose[2]
        if p1 == p2 and p2 == p3:
            print("They are Tie!")
          #p1 & p2  
        elif ((p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P")):
    #p1 win 
            
            if p1 == p3:
                print("Player 1 and Player 3 are Tie.")
            elif ((p1 == "R" and p3 == "S") or (p1 == "P" and p3 == "R") or (p1 == "S" and p3 == "P")):
                #p1 & p3 
                print("Player 1 Win!")
            else : print("Player 3 Win!")
            
        #p2 win
        else :
            if p2 == p3:
                print("Player 2 and Player 3 are Tie.")
            elif ((p2 == "R" and p3 == "S") or (p2 == "P" and p3 == "R") or (p2 == "S" and p3 == "P")):
                #p2 & p3 
                print("Player 2 Win!")
            else : print("Player 3 Win!")
    print(" ")
    again = input("Want to play again?(Y/N) : ").upper()
print("Awesome to have you on board! Thanks for playing.")

