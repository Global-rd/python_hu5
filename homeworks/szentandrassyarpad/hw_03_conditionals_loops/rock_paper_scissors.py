while True:
    rounds=int(input('Fordulók száma: '))
    if rounds%2==1 and rounds>0:
        break
    else:
        print('Legyen olyan kedves, pozitív páratlan egész számot megadni! Előre is köszönjük!')

valid_answers=('rock', 'paper', 'scissors')
score=[0,0]

for i in range(rounds):
    print(f'{i+1}. kör:')    
    while True:
        answers=list()
        for j in range(2):            
            while True:
                answers.append( input(str(j+1)+'. játékos válasza: '))              
                if answers[j] in valid_answers:
                    break
                else:
                    answers.pop()
                    print(f"A lehetséges válaszok: {valid_answers}!")

        if answers[0]==answers[1]:
            print('Döntetlen, válasszatok újra!')
        else:           
            if answers[0]=='rock':
                if answers[1]=='scissors':
                    score[0]+=1
                else:
                    score[1]+=1
            elif answers[0]=='paper':
                if answers[1]=='rock':
                    score[0]+=1
                else:
                    score[1]+=1
            elif answers[0]=='scissors':
                if answers[1]=='paper':
                    score[0]+=1
                else:
                    score[1]+=1            

            break
else:
    print(f'{rounds} kör után győzött { "1. játékos" if score[0]>score[1] else "2. játékos"} {abs(score[0]-score[1])} ponttal.')
