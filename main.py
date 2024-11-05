def main():
    a= int(input("whats the number on your mind:"))    
    b= int(input("whats the number on your mind:"))
    c= input("what do you wanna do with your number?\n add,sub,divide,multiply:")
    c= c.lower()
    if c == "add":
        print(a+b)
    elif c == "sub":
        print(a-b)
    elif c == "divide":
        print(a/b)
    elif c == "multiply":
        print(a*b)
    else:
        print("invalid input")
        main()
    retry()
def retry():
    d= (input("do you wanna continue: (yes or no)"))
    if d=="yes" or "y" or "Y":
        main()
    elif d=="no" or "n" or "N":
        exit()
    else:
        print("invalid input")
        retry()

if __name__ == "__main__":
    main()

