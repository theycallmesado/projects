while True:
    try:
        x = abs(int(input("Give me a number: ")))
    except ValueError:
        print("Try again. ", end="")
        continue
    break


while True:
    x = (x * 3 + 1)
    z = 0
    while x > 0:
        k = x % 10
        z = z + k
        x = int(x/10)
    if z >= 10:
        x = z
        continue
    else:
        break
print(z)
