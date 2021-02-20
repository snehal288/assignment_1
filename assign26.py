def display(n):
    for i in range(5,0,-1):
        for j in range(1,i+1):
            print("* ",end=" ")
        print("\n")
def main():
    value=5
    ret=display(value)
    print(ret)
if __name__=="__main__":
  main()