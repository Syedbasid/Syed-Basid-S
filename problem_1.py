class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
a=float(input("Enter a: "))
b=float(input("Enter b: "))
op=input("Enter operation type (+,-,*,/): ")
calc=calculator()
if op=="+":
    print(calc.add(a,b))
elif op=="-":
    print(calc.sub(a,b))
elif op=="*":
    print(calc.mul(a,b))
elif op=="/":
    if b==0:
          print("Cannot Divide By zero")
    else:
        print(calc.div(a,b))
else:
    print("invalid operation")


