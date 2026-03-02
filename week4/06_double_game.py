import string
import random

m = random.randint(0,4)
n = random.randint(0,4)

symbols = []
symbols = list(string.ascii_letters)
same_symbol = random.choice(symbols)
symbols.remove(same_symbol)

card1=[0]*5
card2=[0]*5

for i in range(0,5):
    if(i == m):
        if(i == n):
            card1[i]=same_symbol
            card2[i]=same_symbol
        else:
            card1[i]=same_symbol
            card2[i]=random.choice(symbols)   
            symbols.remove(card2[i])
    else:
        if(i == n):
            card1[i]=random.choice(symbols)   
            symbols.remove(card1[i])
            card2[i]=same_symbol
        else:
            card1[i]=random.choice(symbols)   
            symbols.remove(card1[i])   
            card2[i]=random.choice(symbols)   
            symbols.remove(card2[i])

print("Card 1:", card1)
print("Card 2:", card2)

ch = input("spot the same symbol : ")
if(ch == same_symbol):
    print("right")
else:
    print("try again")    
            