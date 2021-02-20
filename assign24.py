def fact(n):
    f=0
    for i in range(1,n):
        if n%i==0:
            print(i)
            f=f+i
    return f

def main():
    x=int(input("value is:"))
    ret=fact(x)
    print("addition of factors:",ret)

if __name__=="__main__":
   main()