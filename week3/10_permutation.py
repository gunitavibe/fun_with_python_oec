import random

def choose():
    word = [
    "lishen","angel","evil","state","dusty","night","inch","save"
    ,"silent","brave","heart","earth","stone","tones","below",
    "elbow","alert","alter","later","rescue","secure","stare","tears",
    "cheat","teach","thing","light","brain","train","spear","parse",
    "rat","tar","art","loop","pool","top","pot"
    ]
    pick = random.choice(word)
    return pick
def jumble(word):
    jumbled = "".join(random.sample(word,len(word)))
    return jumbled
def play():
    player1 = input("please enter player 1 name")
    player2 = input("please enter player 2 name")
    ppl1 = 0
    ppl2 = 0
    turn = 0

    while(1):
        picked_word = choose()
        qn = jumble(picked_word)
        print ("your word is : ",qn)

        if(turn==0):
            turn = 1
            print(player1,"your turn")
            ans = input("write your guess :")

            if ans == picked_word:
                ppl1=ppl1+1
                print("your score is " ,ppl1)
            else:
                print("oops try again, i thought : " , picked_word)
        else:
            turn = 0
            print(player2,"your turn")
            ans = input("write your guess :")

            if ans == picked_word:
                ppl2=ppl2+1
                print("your score is ",ppl2)
            else:
                print("oops try again, i thought : " , picked_word)     
        c = input("press 1 if you want to continue else press 0")      
        if (c=="0"):
            print(player1,"=",ppl1)
            print(player2,"=",ppl2)
            break        
play()   