def order (a):
    return sorted([a[i].split() for i in range(len(a))])

def manual_order (a,b,c):
    if a > b:
        a,b = b,a
    if b > c:
        b,c = c,b
    if a > b:
        a,b = b,a
    return (a,b,c)

w = input("digite 3 numeros:")[:3]
x,y,z = input("digite 3 numeros:").split()
ordened = order(w)

print(ordened)
print(manual_order(x,y,z))
