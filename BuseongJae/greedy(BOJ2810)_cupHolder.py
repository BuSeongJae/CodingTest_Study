#9
#SLLLLSSLL
# N = int(input())
info = 'SLLLLSSLL'
info = list(info)
result = 0 #가능한 사람수
i=0
pre = 's'
isRight= False
while i < len(info):
    if(isRight == False):
        if(info[i] =='S'):
            result += 1
            pre = 's'
            i += 1
        elif(info[i] =='L' and pre =='s'):
            result += 2
            pre = 'l'
            i += 2
            isRight =True
    elif (isRight == True):
        if (info[i] == 'S'):
            result += 1
            pre = 's'
            i += 1
        elif (info[i] == 'L'):
            result += 1
            pre = 'l'
            i += 2






print(result)
