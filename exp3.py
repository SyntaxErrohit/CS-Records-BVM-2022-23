def row_max_min(a, m):
    for i in range(m):
        print("Row", i+1, "Maximum:", max(a[i]), "Minimum:", min(a[i]))

def col_max_min(a, m, n):
    for i in range(n):
        maxi = mini = a[0][i]
        for j in range(1, m):
            maxi = max(maxi, a[j][i])
            mini = min(mini, a[j][i])
        print("Column", i+1, "Maximum:", maxi, "Minimum:", mini)

a = ()
m = int(input("Enter the m size of a matrix:"))
n = int(input("Enter the n size of a matrix:"))
print("Enter values for the matrix in the size of", m, "x", n)

for i in range(m):
    t = ()
    for j in range(n):
        t += (int(input()),)
    a += (t,)

print("Matrix is:")
for i in range(m):
    print(a[i])

row_max_min(a,m)
col_max_min(a,m,n)