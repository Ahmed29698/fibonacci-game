#fibonnaci game
#Name : Ahmed gamal
#ID:20170358
#The game works as the players choose tha number of coins and a starting point which make range of their choice 2*the starting point
#Date : 14/2/2018


coins=int(input("what is the number of coins ?"))
player = 1
start=int(input("choose starting point :"))
cond=True
while cond :
    while True :
        print("player",player,"enter number that is at most twice starting point or smaller than number of coins :") 
        move = int(input())
        b=2*move 
        while move >= coins or move > start*2 or move ==0 :
            move =int(input("enter number that is at most twice starting point or smaller than number of coins :"))
        coins=coins - move
        print("coins",coins)
        if coins == 1 :
            print("player",player,"wins")
            break
        elif player == 1:
            player =2
        else :
            player = 1
            
