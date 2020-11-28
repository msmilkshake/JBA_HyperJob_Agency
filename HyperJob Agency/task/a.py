a = input()
try:
    if a.split()[0] == 'int':
        a = int(a.split()[1])
    print(a / 2)
except EOFError:
    print("Error")
finally:
    print("I'm okay.")
print("The end")