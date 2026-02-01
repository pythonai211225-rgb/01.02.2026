
for i in range(5):  # range(0, 4, 1)
    print(i, end = ' ')

print()

for i in range(2, 10 + 2, 2):  # jump by 2
    print(i, end = ' ')

print()

for i in range(15, 10 - 1, -1):  # jump by -1
    print(i, end = ' ')

print()

# range(5) ==> [0, 1, 2, 3, 4]

for i in [1, -2, 5, 0, 10]:
    print(i, end = ' ')

# run on all numbers from 1 to 50 jump by 3 , print all zugi numbers -- use for loop
# input 2 numbers lower, higher -- print all numbers from Higher to Lower (descending) -- use for loop
# *bonus: input 2 numbers 1 divider 2 number 3 , 12.
#         use only for loop and find out how many times 3 is in 12 == 4
#         use only for loop and + operation
#         i.e. 5 and 18 ==> result: 3

higher = 10
lower = 5
for i in range(higher, lower - 1, -1):
    print(i)

