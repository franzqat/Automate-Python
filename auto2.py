# auto2.py

while True:
    print("Hello user. Who are you?")
    name = input()
    if name != 'Joe':
        continue
    print("Hello Joe, what is the password?")
    pw = input()
    if pw == 'swordfish':
        break
print("Access Granted.")
