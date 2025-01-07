questions= [
    [
        "Which Language was used to create 4?", "Python","French","JavaScript","php","none",4
     ],
    [
        "Which Language was used to create fb?", "Python","French","JavaScript","php","none",3
     ],
    [
        "Which Language was used to create fb?", "Python","French","JavaScript","php","none",4
     ],
    [
        "Which Language was used to create fb?", "Python","French","JavaScript","php","none",4
     ],
    [
        "Which Language was used to create fb?", "Python","French","JavaScript","php","none",4
     ],     
    [
        "Which Language was used to create fb?", "Python","French","JavaScript","php","none",4
     ],     
    [
        "Which Language was used to create fb?", "Python","French","JavaScript","php","none",4
     ],
     [
        "Which Language was used to create fb?", "Python","French","JavaScript","php","none",4
     ],
    [
        "Which Language was used to create fb?", "Python","French","JavaScript","php","none",4
     ],     
    [
        "Which Language was used to create fb?", "Python","French","JavaScript","php","none",4
     ],
    [
        "Which Language was used to create fb?", "Python","French","JavaScript","php","none",4
     ],
    [
        "Which Language was used to create fb?", "Python","French","JavaScript","php","none",4
     ], 
    [
        "Which Language was used to create fb?", "Python","French","JavaScript","php","none",4
     ],
    [
        "Which Language was used to create fb?", "Python","French","JavaScript","php","none",4
     ],              
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,100000000,750000000]
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs.{levels[i]}")
    print(f"a. {question[1]}          b. {question[2]} ")
    print(f"c. {question[3]}          d. {question[4]} ")
    reply = int(input("enter your answer (1-4) or 0 to quit:\n "))
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs.{levels[i]}")
        if(i == 4):
            money = 10000
        elif (i == 7):
            money = 25000
        elif (i == 9):
            money = 50000            
        elif (i == 14):
            money = 320000 
        elif (i == 17):
            money = 10000000
        elif (i == 19):
            money = 750000000                            
    else:
        print("Wrong answer!")
        break

print(f"YOUR TAKE HOME MONEY IS {money}")
print(type(questions),questions)