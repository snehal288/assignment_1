def display(n):
    for i in range(n):
        for j in range(n):
            print(j+1,end=" ")
        print()

def main():
    value=int(input())
    ret=display(value)
    print(ret)
if __name__=="__main__":
  main()