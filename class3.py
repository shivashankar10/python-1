'''print(chr(3256)+chr(3302)+chr(3228)+chr(3247)+chr(3277))'''

'''print(chr(3254)+chr(3263)+chr(3253)+chr(3254)+chr(3202)+chr(3221)+chr(3248))'''

'''print(ord('s'))
print(ord('a'))
print(ord('n'))
print(ord('j'))
print(ord('a'))
print(ord('y'))'''

'''for i in range(ord('A'),ord('Z')):
    print(ord(chr(i)),end=' ')'''

'''for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=' ')

print()'''

'''for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()'''


'''for i in range(97,123):
    for j in range(97,i+1):
        print(chr(j),end=' ')
    print()'''

'''for i in range(0,11):
    print(i/10,end=' ')'''
    
'''#print i in range(1,11):
 #print(i/10,end=' ')'''

'''a=-5
print(abs(a))
print(-(a))
print(pow(2,3))
print(pow(2,1))
print(pow(2,0))'''
'''import math
print(math.ceil(5.01))
print(math.ceil(-4.02))'''

def isleapyear(year):
    if(year % 4 == 0 and year % 100!=0):
        return True
    else:
        return False
year=int(input("enter a year:"))
if isleapyear (year):
    print(year,"is a leap year")
else:
    print(year,"is not leap year")
