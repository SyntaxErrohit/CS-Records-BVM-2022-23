def palind(s):                # define a function palind(s)
    if s == s[::-1]:          # check if s == s[::-1]        
        return 1             # if yes, print("true") and return 1
    else:
        return 0             # if no, return 0

def check(s):                       # define a function check(s)
    if s.isalpha():    
        if s[0] in "aeiouAEIOU":
            return 'v'
        else:
            return 'c'


n = int(input("Enter number of strings: "))
p = v = c = 0 # counter
print("Enter", n, "strings:")

for i in range(n):
    a = input() # paaru
    if palind(a) == 1:
        p += 1
    res = check(a)
    if res == 'v':
        v += 1
    else: # else
        c += 1

print("Number of palindrome strings:", p)
print("Number of vowel strings:", v)
print("Number of consonant strings:", c)
