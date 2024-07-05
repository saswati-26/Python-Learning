import os

where = input("Enter the filename you want to work with: ")
mode = input("Enter the mode (r=read, w=write, a=append, r+=read and write): ")

if not os.path.exists(where):
    create_file = input("File doesn't exist. Do you want to create a new file? (y/n): ")
    if create_file.lower() != 'y':
        print("Exiting program.")
        exit()

try:
    with open(where, mode) as f:
        want_to_continue = 'y'
        while want_to_continue.lower() == 'y':
            if 'r' in mode:
                content = f.read()
                print(content)
            elif 'w' in mode or 'a' in mode:
                text = input("Enter the data you want to write/append: ")
                f.write(text + '\n')
                print("Text successfully written/appended to the file.")
            elif 'r+' in mode:
                content = f.read()
                print(content)
                text = input("Enter the data you want to write/append: ")
                f.seek(0) #move pointer to the beginning
                f.write(text)
                new_line = input("Do you want to add a new line? (y/n): ")
                if new_line.lower() == 'y':
                    f.write('\n')
                f.seek(0)
                updated_content = f.read()
                print(updated_content)
            else:
                print("Enter a valid mode (r=read, w=write, a=append, r+=read and write): ")

            want_to_continue = input("Do you want to continue? (y/n): ")
except Exception as e:
    print("Exception arised is:", e)

print("File operation is successful!!")