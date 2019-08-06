from random import randint,randrange
def lose(l):
    if isfull(l) and isfull(sleft(l)) and isfull(sright(l)) and isfull(sup(l)) and isfull(sdown(l)):
        return 1
    return 0
def isfull(l):
    for i in l:
        for j in i:
            if j==0:
                return 0
    return 1
def genelem(l):
    i=randint(0,len(l)-1)
    j=randint(0,len(l)-1)
    if isfull(l):
        if not isfull(sleft(l)) or not isfull(sright(l)) or not isfull(sup(l)) or not isfull(sdown(l)):
            return 'special'
    else:
        if l[i][j]==0:
            l[i][j]=randrange(2,5,2)
            return l
        else:
            genelem(l)
def sleft1(l1):
    l=l1
    i=0
    j=0
    for i1 in l:
        j2=0
        j=0
        j3=0
        count=0
        #CHECKS FOR ELEMENTS WHICH ARE NON ZERO AND EQUAL
        for j1 in range(0,len(i1)):
            if l[i][j2]!=0:
                for o in range(j2+1,len(i1)):
                    if l[i][o]!=l[i][j2] and l[i][o]!=0:
                        #IF THERE IS AN ELEMENT WHICH BLOCKS THE ELEMENT WHICH IS NON ZERO,THE GIVEN ELEMENT CANNOT
                        #BE COMBINED WITH ANY OTHER ELEMENT IN THE SAME ROW.HENCE BREAK
                        break
                    if l[i][o]==l[i][j2]:
                        #COMBINES THE TWO EQUAL ELEMENTS AND MAKES THE RIGHT EQUAL ELEMENT ZERO
                        l[i][j2]=2*l[i][j2]
                        l[i][o]=0
                        o-=1
                        break
            j2+=1
        #SHIFTS ELEMENTS TO THE LEFT
        for j1 in i1:
            if l[i][j]!=0:
                #NEED TO SHIFT ONLY IF THE ELEMENT IS NON ZERO
                for k in range(j+1):
                    if l[i][j-k]==0:
                    #SHIFTS THE NON ZERO NUMBERS TO THE LEFT OF THE FOUND NUMBER
                    #(BY NUMBER OF ZEROES TO THE LEFT PLACES) TO THE LEFT 
                        temp=l[i][j-k]
                        l[i][j-k]=l[i][j-k+1]
                        l[i][j-k+1]=temp
            j+=1
        i+=1
    return l
def rotate(l):
    m=zip(*l[::-1])
    m=map(list,m)
    return m
def sleft(l):
    return rotate(rotate(rotate(rotate(sleft1(l)))))
def sright(l):
    return rotate(rotate(sleft(rotate(rotate(l)))))
def sup(l):
    return rotate(rotate(rotate(sright(rotate(l)))))    
def sdown(l):
    return rotate(rotate(rotate(sleft(rotate(l)))))
def printl(l):
    for i in l:
        print i
    print '\n'
print '\n'
def play2048():
    n=int(raw_input('enter NxN grid:'))
    l=[]
    for i in range(n):
        count=[]
        for j in range(n):
            count.append(0)
        l.append(count)
    genelem(l)
    printl(l)
    while not lose(l):
        ch=raw_input('up=w down=s right=d left=a')
        if ch=='w':
            if l==sup(l):
                printl(l)
                continue
            else:
                l=sup(l)
                genelem(l)
                printl(l)
        if ch=='a':   
            l1=map(list,l)
            #printl(l1)
            #printl(sleft(l1))
            if sleft(l)==l1:
                printl(l)
                l=l
                continue
            else:
                genelem(l)
                printl(l)
        if ch=='s':
            if l==sdown(l):
                printl(l)
                l=l
                continue
            else:
                l=sdown(l)
                genelem(l)
                printl(l)
        if ch=='d':
            if l==sright(l):
                printl(l)
                continue
            else:
                l=sright(l)
                genelem(l)
                printl(l)
        if ch=='bored':
            print 'play this in you free time'
            break
        if lose(l):
            print 'You lose!!!!!!!!'
play2048()
def algo():
    n=int(raw_input('enter grid'))
    l=[]
    for i in range(n):
        m=[]
        for j in range(n):
            m.append(0)
        l.append(m)
    while not lose(l):
        genelem(l)
        print'jaa'
        printl(l)
        l=sright(l)
        l=sdown(l)
        l=sleft(l)
        l=sup(l)
        printl(l)
    return l
#algo()
"""printl(l)
n=[]
for i in l:
    n.append(i)
n=map(list,l)
print n
printl (sleft(l))
if n==sleft(l):
    print l
    print (n)
printl(n)"""
