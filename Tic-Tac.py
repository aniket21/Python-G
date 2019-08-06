list=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
listx=[[0,0],[0,0],[0,0],[0,0],[0,0]]
listo=[[0,0],[0,0],[0,0],[0,0],[0,0]]
def printlist(l):
    print '%s | %s | %s' %(l[0][0],l[0][1],l[0][2])
    print '-----------'
    print '%s | %s | %s' %(l[1][0],l[1][1],l[1][2])
    print '-----------'
    print '%s | %s | %s' %(l[2][0],l[2][1],l[2][2])
def wincheck(O,list1):
    if list1[0][0]==O and list1[0][1]==O and list1[0][2]==O or list1[1][0]==O and list1[1][1]==O and list1[1][2]==O or list1[2][0]==O and list1[2][1]==O and list1[2][2]==O or list1[0][0]==O and list1[1][1]==O and list1[2][2]==O or list1[0][2]==O and list1[1][1]==O and list1[2][0]==O  or list1[0][0]==O and list1[1][0]==O and list1[2][0]==O or list1[0][1]==O and list1[1][1]==O and list1[2][1]==O or list1[0][2]==O and list1[1][2]==O and list1[2][2]==O:
        return 1        
flag=0
e=0
j=0
p=0
ch=' '
printlist(list)
ch=raw_input('do you want to play against another player? press y ;to exit press n')
if ch=='y':
    for m in range(0,5):
        x=raw_input('player X enter your x coordinate')
        y=raw_input('player X enter your y coordinate')
        x=int(x)
        y=int(y)
        listx[e]=(x,y)
        for i in range(0,e+1):
            if listx[e]==listo[j] or listx[e]==listx[j] and e!=j:
                flag=1
            j=j+1
        j=0
        if flag==1:
            print('Overwriting not allowed!!!!!')
            break
        list[x][y]='X'
        printlist(list)
        wincheck('X',list)
        if wincheck('X',list)==1:
            print('player X wins')
            break
        if e==4:
            print 'thanks'
            break
        m=raw_input('player O enter your x coordinate')
        n=raw_input('player O enter your y coordinate')
        m=int(m)
        n=int(n)
        listo[e]=(m,n)
        for k in range(0,e+1):
            if listo[e]==listx[p] or listo[e]==listo[p] and e!=p:
                flag=1
            p=p+1
        if flag==1:
            print 'Overwriting not allowed!!!!!!'
            break
        p=0
        list[m][n]='O'
        printlist(list)
        wincheck('O',list)
        if wincheck('O',list)==1:
            print(' player O wins')
            break
        e=e+1
else:
    print ('exit')
