try:
    file = open ("hello.txt",'r')
    try:
        temp = file.read()
        print(temp)
        file.close()
    except:
        print("The file doesn't exist")
except:
    print("File doesn't exist")
finally:
    print("We are done with the code")