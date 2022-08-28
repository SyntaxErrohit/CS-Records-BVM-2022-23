import csv

def create():
    heading = ["Name", "Age", "Sex"]
    rows = [["rat", 43, 'M'], ["anu", 45, 'F'],
            ["raja", 50, 'M'], ["rani", 52, 'F']]
    with open("data.csv", "w", newline="") as f:
        obj = csv.writer(f)
        obj.writerow(heading)
        obj.writerows(rows)
        print("Records are written in data.csv file")

def display():
    with open("data.csv", "r", newline="") as f:
        obj = csv.reader(f)
        for x in obj:
            print(x)

def search():
    found = 0
    with open("data.csv", "r", newline="") as f:
        obj = csv.reader(f)
        n = input("Enter name to search: ")
        for row in obj:
            if row[0] == n:
                print("Name =", row[0])
                print("Age =", row[1])
                print("Sex =", row[2])
                found = 1
        if found == 0:
            print("Sorry, record not found")

create()
display()
search()
