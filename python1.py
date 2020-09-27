import random


tries = 0
correct1 = 0

print("Time to count up")
#loop tests ascending count
while correct1 < 3:#if they get 3 answers correct, they can move on to the next level
    #x,y,z, and a are random #s going in ascending order
    x = random.randint(1,100)
    y = x+1
    z = y+1
    a = z+1
    answer = ""
    nextNumber = str(a)
    print(str(x)+","+str(y)+","+str(z)+",?")#prompt of sequence
    print("What comes next?")
    while answer!=nextNumber:
        if tries < 3:#if they don't get it in 3 tries, display solution and make a new problem
            answer = input()#user input
            if answer!=nextNumber:
                print("Try again")
                tries += 1
            else:
                print("Correct")
                correct1+=1
                break

        else:
            print("The correct answer is " + nextNumber)
            break  

tries2 = 0
correct2 = 0
#loop tests descending count
print()
print("Time to count down")
while correct2 < 3:#if they get 3 answers correct, they are done with level 1
    #x,y,z, and a are random #s going in ascending order
    x = random.randint(3,100)
    y = x-1
    z = y-1
    a = z-1
    answer = ""
    nextNumber = str(a)
    tries2 = 0
    print(str(x)+","+str(y)+","+str(z)+",?")#prompt of sequence
    print("What comes next?")
    while answer!=nextNumber:
        if tries2 < 3:#if they don't get it in 3 tries, display solution and make a new problem
            answer = input()#user input
            if answer!=nextNumber:
                print("Try again")
                tries2 += 1
            else:
                print("Correct")
                correct2+=1
                break

        else:
            print("The correct answer is " + nextNumber)
            break        
    
