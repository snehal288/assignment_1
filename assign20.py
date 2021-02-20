def display(n):
    i=0
    while n>0:
        f=n%10
        i=i+f
        n=n//10
    return i
def main():
    num=int(input("enter number:"))
    ret=display(num)
    print("addition is:",ret)
if __name__=="__main__":
    main()