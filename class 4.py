'''name=str(input('enter ur name:'))
length=len(name)
for i in range(length):
    for j in range(length):
        if i+j==1 or i==name or i+j==length-1:
            print(name[i],end=' ')
        else: 
            print(" ",end=" ")
    print()'''

'''apple=[10,5,20]
print(apple)
print(apple[1])
print(apple[-1])
print(apple[-3])'''

'''banana=[10,'banana',250000.75,'Z']
print(banana)

for i in banana:
    print(i,end=" ")'''2

'''college=[10,20,30,40,50]
print(college[1])
print(college[-2])
print(college[1:3])
print(college[1:7])'''

shetty=[]
n=int(input('enter the list size'))
for i in range(0,n):
    ele=input('enter the elements')
    shetty.append(ele)
print(shetty)

