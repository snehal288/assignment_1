def prime(n):
    for i in range (2,n):
        if n%i==0:
            print("not prime number")
            return
    else:
       print("prime number")
def main():
    x=int(input())
    ret=prime(x)
    print(ret)
if __name__=="__main__":
    main()