num=[int(x) for x in input("Enter numbers: ").replace(","," ").split()]
result={}
for i in range(1,10):
    count=0
    for n in num:
        if n%i==0:
            count+=1
        result[i]=count
print(result)
    