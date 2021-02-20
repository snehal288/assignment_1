def add(no1,no2):
    sum=no1+no2
    return sum
def main():
    print("enter number")
    value1=int(input())
    value2=int(input())
    ret=add(value1,value2)
    print("addition is",ret)
if __name__=="__main__":
    main()