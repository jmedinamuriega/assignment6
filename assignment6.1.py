# 1. The Calculator App
num1=input("please put the first number: ")
num2=input("please put the second number: ")
operation=input("now the type of operation (D)ivision, (M)ultiplication, (S)um, (Su)bstraction")


def sum(num1,num2):
    return int(num1)+int(num2)

def divison(num1,num2):
    return int(num1)/int(num2)
     
def multiplication(num1, num2):
    return int(num1)*int(num2)
      
def substraction(num1, num2):        
    return int(num1)-int(num2)
while True:
    try:             
        if operation.lower()=="s":
            sum(num1,num2)
            print(f"the result of that operation is {sum(num1,num2)}")
            break
        if operation.lower()=="d":
            try:
                divison(num1,num2)
                print(f"the result of that operation is {divison(num1,num2)}")
            except ZeroDivisionError:
                print("Can't divide by Zero")
                break
        if operation.lower()=="m":
            multiplication(num1,num2)
            print(f"the result of that operation is {multiplication(num1,num2)}")
            break
        if operation.lower()=="su":
            substraction(num1,num2)
            print(f"the result of that operation is {substraction(num1,num2)}")
            break
    except ValueError:
        print("Hey put numbers not strings :D")
        break

    
    
    