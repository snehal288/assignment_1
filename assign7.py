def chknum(no):
    if no%5==0:
        return True
    else:
        return False

def main():
    num=int(input("enter value"))
    ret=chknum(num)
    if ret==True:
        print("TRUE")
    else:
        print("FALSE")
if __name__=="__main__":
    main()