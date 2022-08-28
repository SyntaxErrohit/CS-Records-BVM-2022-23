def print_diagonal(a,n):
    for i in range(n):
        for j in range(n):
            if i == j or i == n-1-j:
                print(a[i][j], end=" ")
            else:
                print(" ", end=" ")
        print()

def swap_diagonal(a,n):
    for i in range(n):
        a[i][i], a[i][n-i-1] = a[i][n-i-1], a[i][i]

a = []
n = int(input("Enter the size of square matrix: "))
print("Enter values for the square matrix in the size of", n,"x",n)

for i in range(n):
    t = []
    for j in range(n):
        t.append(int(input()))
    a.append(t)

print("\nDiagonal before swaping:")
print_diagonal(a,n)
swap_diagonal(a,n)
print("\nDiagonal after swaping:")
print_diagonal(a,n)