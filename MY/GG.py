try:
    with open("MY/users,txt", "r", encoding="utf-8")as file:
        content = file.read()
        a = content.split()
        b = content.split()
        print(a)
        print(int() + int())
except FileNotFoundError:
    print("File not Found")

try:
    with open("MY/users,txt", "r", encoding="utf-8")as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not Found")




try:
    with open("MY/users,txt", "r", encoding="utf-8")as file:
        content = file.read()
        print(content)
  #      #file.write(content::-1.strip(''))
except FileNotFoundError:
    print("File not Found")