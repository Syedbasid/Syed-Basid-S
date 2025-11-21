a= int(input("Enter a: "))
if a%2==1:
    count =a
else:
    count=a-1
if count<=0:
    count=1
for i in range(count):
    print(2*i+1,end=" ")


