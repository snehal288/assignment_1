def chknum(no):
    if no%2==0:
        return True
    else:
        return False
def main():
    print("enter number")
    value=int(input())
    bret=chknum(value)
    if bret==True:
        print("even number")
    else:
        print("odd number")
if __name__=="__main__":
    main()