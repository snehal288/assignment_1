from arithmatic import *

#entry point function
def main():
    print("enter first number:")
    value1=int(input())

    print("enter second number:")
    value2=int(input())

    ret1=add(value1,value2)
    ret2=sub(value1,value2)
    ret3=div(value1,value2)
    ret4=mult(value1,value2)

    print("addition is:",ret1)
    print("substraction is:",ret2)
    print("division is:", ret3)
    print("multiplication is:", ret4)

if __name__=="__main__":
 main()

