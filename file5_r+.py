with open("hello.text","r+") as f:
    content = f.read()
    print(content)
    text = input("Enter the data you want to write/append: ")
    f.write(text)
    updated_content = f.read()
    print(updated_content)