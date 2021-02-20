def chknum(no):
    if no>0:
        return no
    elif no==0:
        return no
    else:
        return no

def main():
    num=int(input("enter value"))
    ret=chknum(num)
    if ret>0:
        print("number is positive")
    elif ret==0:
        print("zero")
    else:
        print("number is negative")
if __name__=="__main__":
    main()