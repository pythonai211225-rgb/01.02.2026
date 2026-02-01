
# START

# range(10)        = 0 1 2 3 4 5 6 7 8 9
# range(0, 10)     = 0 1 2 3 4 5 6 7 8 9
# range(1, 10 + 1) = 1 2 3 4 5 6 7 8 9 10

# _min = None
# { 9, 8, 0, 1 } ==> 0
# { }  ==> 0
# { 3 , 1, 0  }  _min = 0
# { } _min = None

players_total = 0
player_above_16 = 0

for _ in range(1, 10 + 1):
    player_age = int(input('age?'))
    if player_age < 12:
        continue
    if player_age > 18:
        break

    players_total += 1
    if player_age > 16:
        player_above_16 += 1

print('players total:', players_total)
print('player above 16:', player_above_16)

# STOP