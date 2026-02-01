
# START

lower = None
higher = None

while True:
    lower = int(input('lower?'))
    higher = int(input('higher?'))
    if higher > lower:
        break
    print("===== higher must be bigger than lower")

for i in range(lower, higher + 1):
    print (i, end=" ")

# STOP