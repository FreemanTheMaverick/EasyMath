import random as rd

operators=['+','-','*','/']

def evaluate(string):
    result=0
    condition=0
    try:
        result=eval(string)
    except ZeroDivisionError:
        condition=1
    else:
        condition=(result<0 or result%1!=0)
    return result,condition

def bracket(bracketlength,operator):
    tokens=[]
    condition=True
    while condition:
        tokens=[]
        for i in range(bracketlength):
            if i!=0:
                tokens.append(rd.choice(operators))
            tokens.append(str(rd.choice([rd.randint(2,9),rd.randint(1,99),rd.randint(1,999)]))+'.')
        string=''.join(tokens)
        result,condition=evaluate(string)
        condition=condition or operator not in string
    return '('+string+')'

def printformula(string,answer):
    question=string.replace('.','').replace('+',' + ').replace('-',' - ').replace('*',' * ').replace('/',' ÷ ')
    result=eval(string)
    if answer:
        print(question+' = '+str(round(result)))
    else:
        print(question)

def randomlist(num):
    ls=[]
    residual=num
    while residual>0:
        a=rd.randint(1,num-1 if residual==num else residual)
        ls.append(a)
        residual=residual-a
    return ls

from sys import argv
if __name__=='__main__':
    length=int(argv[1])
    total=int(argv[2])
    strings=[]
    for n in range(total):
        ls=randomlist(length)
        condition=1
        string=''
        while condition:
            bigtokens=[]
            for i in ls:
                if i==1:
                    bigtokens.append(str(rd.choice([rd.randint(2,9),rd.randint(1,99),rd.randint(1,999)]))+'.')
                else:
                    bigtokens.append(bracket(i,rd.choice(operators)))
                bigtokens.append(rd.choice(operators))
            bigtokens.pop()
            string=''.join(bigtokens)
            result,condition=evaluate(string)
        strings.append(string)

    print('Questions:')
    for n in range(total):
        print(str(n+1)+'. ',end='')
        printformula(strings[n],0)

    print('Answers:')
    for n in range(total):
        print(str(n+1)+'. ',end='')
        printformula(strings[n],1)
