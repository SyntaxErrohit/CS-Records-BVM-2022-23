def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

def insertionSort(a):
    for i in range(len(a)):
        t = a[i]
        while i >= 1 and a[i-1] > t:
            a[i] = a[i-1]
            i -= 1
        a[i] = t

def binarySearch(a, x):
    l = 0
    h = len(a)-1
    while l <= h:
        m = (l+h)//2
        if a[m] < x:
            l = m+1
        elif a[m] > x:
            h = m-1
        else:
            print("Element found at", m+1)
            break
    else:
        print("Element not found")

print("1.Bubble sort and binary search")
print("2.Insertion sort and binary search")
print("3.Exit")
ch = int(input("Enter choice number: "))

while ch != 3:
    if ch == 1:
        l = []
        n = int(input("Enter number of integers: "))
        print("Enter", n, "integers")
        for i in range(n):
            l.append(int(input()))
        bubbleSort(l)
        print("Sorted array:", l)
        s = int(input("Enter element to search: "))
        binarySearch(l, s)

    elif ch == 2:
        l = []
        n = int(input("Enter number of strings: "))
        print("Enter", n, "strings")
        for i in range(n):
            l.append(input())
        insertionSort(l)
        print("Sorted array:", l)
        s = input("Enter element to search: ")
        binarySearch(l, s)

    else:
        print("Enter a number between 1-3")

    print("1.Bubble sort and binary search")
    print("2.Insertion sort and binary search")
    print("3.Exit")
    ch = int(input("Enter choice number: "))