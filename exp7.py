import pickle

def create():
    f = open("student.dat", "wb")
    while True:
        rno = int(input("Enter roll no: "))
        name = input("Enter name: ")
        gender = input("Enter gender: ")
        std = int(input("Enter standard: "))
        sec = input("Enter section: ")
        data = [rno, name, gender, std, sec]
        pickle.dump(data, f)
        ch = input("Do you want to continue (y/n): ")
        if ch == 'n':
            break
    f.close()

def append():
    f = open("student.dat", "ab")
    while True:
        rno = int(input("Enter roll no: "))
        name = input("Enter name: ")
        gender = input("Enter gender: ")
        std = int(input("Enter standard: "))
        sec = input("Enter section: ")
        data = [rno, name, gender, std, sec]
        pickle.dump(data, f)
        ch = input("Do you want to continue (y/n): ")
        if ch == 'n':
            break
    f.close()

def display():
    f = open("student.dat", "rb")
    try:
        while True:
            k = pickle.load(f)
            print(k)
    except EOFError:
        f.close()

def search():
    f = open("student.dat", "rb")
    rno = int(input("Enter roll no to find: "))
    flag = 0
    try:
        while True:
            k = pickle.load(f)
            if k[0] == rno:
                print(k)
                flag = 1
    except EOFError:
        f.close()
    if flag == 0:
        print("Sorry, record not found!")

create()
while True:
    print("Main menu\n1. Append\n2. Display\n3. Search\n4. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        append()
    elif ch == 2:
        display()
    elif ch == 3:
        search()
    elif ch == 4:
        break
