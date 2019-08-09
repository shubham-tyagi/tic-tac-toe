import random

board={'1':' ','2':' ','3':' ',
        '4':' ','5':' ','6':' ',
        '7':' ','8':' ','9':' '}

list=[1,2,3,4,5,6,7,8,9]

def printBoard(board):
    print("\n")
    print(board['1']+" | "+board['2']+" | "+board['3'])
    print("---------")
    print(board['4']+" | "+board['5']+" | "+board['6'])
    print("---------")
    print(board['7']+" | "+board['8']+" | "+board['9'])

#board['1']='X'

while(True):
    print("\nwhat do you want to be 'X' or 'O' ")
    player=input()
    player=player.upper()
    if(player=='X' or player=='O'):
        break

if(player=='X'):
    computer='O'
else:
    computer='X'

list1=[['1','2','3'],['1','4','7'],['1','5','9'],['3','6','9'],['3','5','7'],['4','5','6'],['2','5','8'],['7','8','9']]
list2=['1','3','5','9']
list3=['9','5','3','1']

for i in range(5):
    flag=0
    while(True):
        if(5 in list):
            position=5
            break
        
        for k in range(len(list1)) :
            if( (board[str(list1[k][0])]==board[str(list1[k][1])]== computer) and (int(list1[k][2]) in list) ):
                position=list1[k][2]
                flag=1
                break

            if(board[str(list1[k][1])]==board[str(list1[k][2])]==computer and (int(list1[k][0]) in list)):
                position=list1[k][0]
                flag=1
                break

            if(board[str(list1[k][0])]==board[str(list1[k][2])]== computer and (int(list1[k][1]) in list)):
                position=list1[k][1]
                flag=1
                break    

        if flag==1:
            break

        for k in range(len(list1)) :
            
            if(board[str(list1[k][0])]==board[str(list1[k][1])]== player and (int(list1[k][2]) in list)):
                position=list1[k][2]
                flag=1
                break

            if(board[str(list1[k][1])]==board[str(list1[k][2])]==player and (int(list1[k][0]) in list)):
                position=list1[k][0]
                flag=1
                break

            if(board[str(list1[k][0])]==board[str(list1[k][2])]== player and (int(list1[k][1]) in list)):
                position=list1[k][1]
                flag=1
                break  
        
        if flag==1:
            break

        for k in range(len(list2)):
            if(int(list2[k]) in list and int(list3[k]) in list  ):
                position=list2[k]
                flag=1
                break
        
        if flag==1:
            break
        while(True):
            position = list[random.randint(0,len(list)-1)]
            if(position in list):
                break
        break
    
    board[str(position)]=computer
    printBoard(board)
    list.remove(int(position))

    

    if(board['1']==board['2']==board['3']==computer or board['4']==board['5']==board['6'] == computer or
       board['1']==board['4']==board['7'] == computer or board['1']==board['5']==board['9'] == computer or
       board['3']==board['6']==board['9'] == computer or board['3']==board['5']==board['7'] == computer or
       board['2']==board['5']==board['8'] == computer or board['7']==board['8']==board['9'] == computer ):
       
       print("\n----------- the computer has won ! you lose ------------- ")
       break
    
    if(i==4):
        print("\n--------------------draw------------------------")
        break
    # turn=player
    while(True):
        position=input("\n enter the position you want to mark ")
        if(int(position)in list):
            break
        else:
            printBoard(board)

    board[str(position)]=player
    list.remove(int(position))

    if(board['1']==board['2']==board['3']==computer or board['4']==board['5']==board['6'] == computer or
       board['1']==board['4']==board['7'] == computer or board['1']==board['5']==board['9'] == computer or
       board['3']==board['6']==board['9'] == computer or board['3']==board['5']==board['7'] == computer or
       board['2']==board['5']==board['8'] == computer or board['7']==board['8']==board['9'] == computer ):
       
       print("\n---------- the player has won ! computer lose . -------------")
       break





        
        



