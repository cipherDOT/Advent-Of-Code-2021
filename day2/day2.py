

# day 2 - Dive!
# -------------------------------------------------------------------- #
# part 1
# objective : What do you get if you multiply your final horizontal position by your final depth?
with open('input.txt') as f:
    data = [i.strip() for i in f.readlines()]
    f.close()


x_coords = []
y_coords = []

for cmd in data:
    [word, num] = cmd.split()
    if word == 'forward':
        x_coords.append(int(num))
    elif word == 'up':
        y_coords.append(-int(num))
    elif word == 'down':
        y_coords.append(int(num))

x_coord = sum(x_coords)
y_coord = sum(y_coords)
result_1 = x_coord * y_coord
print(result_1)

# -------------------------------------------------------------------- #
# part 2
# objective : What do you get if you multiply your final horizontal position by your final depth?
x_coords = []
y_coords = []
aim = 0

for cmd in data:
    [word, num] = cmd.split()
    if word == 'forward':
        x_coords.append(int(num))
        y_coords.append(aim * int(num))

    elif word == 'up':
        aim -= int(num)

    elif word == 'down':
        aim += int(num)

x_coord = sum(x_coords)
y_coord = sum(y_coords)
result_2 = x_coord * y_coord
print(result_2)

# -------------------------------------------------------------------- #
