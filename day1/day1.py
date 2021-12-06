# day 1 - sonar sweep
# -------------------------------------------------------------------- #

# part 1
# objective : How many measurements are larger than the previous measurement?
with open('input.txt') as f:
    data = [int(i) for i in f.readlines()]
    f.close()

result_1 = 0

for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        result_1 += 1

print(result_1)

# -------------------------------------------------------------------- #

# part 2
# objective : How many sums are larger than the previous sum?
result_2 = 0

for i in range(3, len(data)):
    curr_window_sum = data[i - 2] + data[i - 1] + data[i - 0]
    prev_window_sum = data[i - 3] + data[i - 2]+ data[i - 1]

    if curr_window_sum > prev_window_sum:
        result_2 += 1

print(result_2)

# -------------------------------------------------------------------- #

