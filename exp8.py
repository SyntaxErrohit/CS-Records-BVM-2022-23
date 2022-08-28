import pickle, os

def append():
    f = open("std.dat", "ab")
    while True:
        rno = int(input("Enter roll no: "))
        name = input("Enter name: ")
        mark = int(input("Enter mark: "))
        data = {"rollno": rno, "name": name, "mark": mark}
        pickle.dump(data, f)
        ch = input("Do you want to continue (y/n): ")
        if ch == 'n':
            break
    f.close()

def display():
    f = open("std.dat", "rb")
    try:
        while True:
            k = pickle.load(f)
            print("Roll no:", k["rollno"])
            print("Name:", k["name"])
            print("Mark:", k["mark"])
    except EOFError:
        f.close()

def modify():
    f = open("std.dat", "rb")
    t = open("temp.dat", "wb")
    rno = int(input("Enter roll no to modify: "))
    flag = 0
    try:
        while True:
            k = pickle.load(f)
            if k["rollno"] == rno:
                mark = int(input("Enter mark: "))
                data = {"rollno": rno, "name": k["name"], "mark": mark}
                pickle.dump(data, t)
                flag = 1
            else:
                pickle.dump(k, t)
    except EOFError:
        f.close()
        t.close()
    if flag == 0:
        print("Sorry, record not found!")
    os.remove("std.dat")
    os.rename("temp.dat", "std.dat")

while True:
    print("Main menu\n1. Append\n2. Display\n3. Modify\n4. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        append()
    elif ch == 2:
        display()
    elif ch == 3:
        modify()
    elif ch == 4:
        break
