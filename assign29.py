def display(n):
    i=0
    while(n>0):
        i=i+1
        n=n//10
    return i
def main():
    num=int(input("enter num"))
    ret=display(num)
    print("digits in numbers",ret)
if __name__=="__main__":
    main()
