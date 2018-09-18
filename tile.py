#Start from tile 1,1
#Instructions pop up and shows you which directions you can choose
#You input the direction you want to go which will be defined as:
#'N' As in North
#'S' As in South
#'E' As in East
#'W' as in west
# Once you input your direction the instructions will pop up to show you the directions.
#Once the final tile of 3,1 has been reached you will have won the game




x = 1
y = 1



while not (x==3 and y==1):
    if (x,y) == (1,1):
        print("You can travel: (N)orth")
        Direction = str(input("Direction: "))
        valid_direction = 'n'
        if (Direction==valid_direction):
            y = y+1
        else:
            print("Not a valid direction!")

    elif (x,y) == (1,2):
        print("You can travel: (N)orth or (S)outh or (E)ast")
        Direction = str(input("Direction: "))
        valid_direction = 'n' 's' 'e'
        if (Direction=='s'):
            y = y-1
        elif(Direction=='n'):
            y= y+1 
        elif(Direction=='e'):
            x= x+1 
        else:
            print("Not a valid direction!")

    elif (x,y) == (1,3):
        print("You can travel: (S)outh or (E)ast")
        Direction = str(input("Direction: "))
        valid_direction = 'n' 's' 'e'
        if (Direction=='s'):
            y = y-1
        elif(Direction=='e'):
            x= x+1 
        else:
            print("Not a valid direction!")

    elif (x,y) == (2,1):
        print("You can travel: (N)orth ")
        Direction = str(input("Direction: "))
        valid_direction = 'n'
        if(Direction=='n'):
            y= y+1 
        else:
            print("Not a valid direction!")

    elif (x,y) == (2,2):
        print("You can travel: (S)outh or (W)est")
        Direction = str(input("Direction: "))
        valid_direction = 'w' 's'
        if (Direction=='s'):
            y = y-1
        
        elif(Direction=='w'):
            x= x-1
        else:
            print("Not a valid direction!")

    elif (x,y) == (2,3):
        print("You can travel: (W)est or (E)ast")
        Direction = str(input("Direction: "))
        valid_direction = 'w' 'e'
        if (Direction=='w'):
            x = x-1
        elif(Direction=='e'):
            x= x+1 
        else:
            print("Not a valid direction!")

    elif (x,y) == (3,1):
        print("You can travel: (N)orth")
        Direction = str(input("Direction: "))
        valid_direction = 'n'
        if (Direction=='n'):
            y = y+1
        else:
            print("Not a valid direction!")

    elif (x,y) == (3,2):
        print("You can travel: (N)orth or (S)outh")
        Direction = str(input("Direction: "))
        valid_direction = 'n' 's'
        if (Direction=='s'):
            y = y-1
        elif(Direction=='n'):
            y= y+1 
        else:
            print("Not a valid direction!")

    elif (x,y) == (3,3):
        print("You can travel: (W)est or (S)outh")
        Direction = str(input("Direction: "))
        valid_direction = 'w' 's'
        if (Direction=='s'):
            y = y-1
        
        elif(Direction=='w'):
            x= x-1
        else:
            print("Not a valid direction!")
    
    
if (x==3 and y==1):
    print("Victory")
