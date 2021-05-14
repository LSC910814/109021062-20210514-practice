n, a1, a2, a3 = map(int,input().split())

t=a1 * 15 + a2 * 20 + a3 * 30
x = (n-t) 
x1 = (n-t) // 50
x2 = (x - (x1 * 50)) // 5
x3 = (x - ((x1 * 50) + (x2 *5))) // 1

if n< t:
    print(0)
else:
    print(x3, x2, x1)