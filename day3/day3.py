
# day 3 - binary diagnostic

# -------------------------------------------------------------------- #

# part 1
# objective : What is the power consumption of the submarine?
# note : power = gamma * epsilon
with open('input.txt') as f:
    data = [i.strip() for i in f.readlines()]
    f.close()

bit_length = len(data[0])
gamma = ''
epsilon = ''

for i in range(bit_length):
    bits = []
    common = None
    rare = None
    for bit in data:
        bits.append(int(bit[i]))

    s = sum(bits)
    if s > len(data) // 2:
        common = 1
        rare = 0
    else:
        common = 0
        rare = 1

    gamma = gamma + str(common)
    epsilon = epsilon + str(rare)

print(f'binary gamma: {gamma}')
print(f'binary epsilon: {epsilon}')
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(f'decimal gamma: {gamma}')
print(f'decimal epsilon: {epsilon}')
print(f'result 1: {gamma * epsilon}')

print('\n#------------------------------------#\n')

# -------------------------------------------------------------------- #

# part 2
# objective : What is the life support rating of the submarine?
# note : life support = oxygen genrator{var : oxygen} * CO2 scrubbber{var : carbon}
def most(arr):
    elems = ['0', '1']
    high = -1
    elem = None
    for i in elems:
        if arr.count(i) > high:
            elem = i
            high = arr.count(i)
        elif arr.count(i) == high:
            return '1'
        
    return elem

def least(arr):
    elems = ['0', '1']
    low = 9999
    elem = None
    for i in elems:
        if arr.count(i) < low:
            elem = i
            low = arr.count(i)
        elif arr.count(i) == low:
            return '0'
        
    return elem

def func(arr, common):
    res = arr
    for count in range(bit_length):
        if len(res) == 1:
            return res
        bits = []
        for i in res:
            bits.append(i[count])

        if common:
            c = most(bits)
        else:
            c = least(bits)

        res = list(filter(lambda k:k[count] == c, res))
    
    return res

oxygen = func(data, True)
carbon = func(data, False)
print(f'binary oxygen: {oxygen[0]}')
print(f'binary carbon: {carbon[0]}')
oxygen = int(oxygen[0], 2)
carbon = int(carbon[0], 2)
print(f'decimal oxygen: {oxygen}')
print(f'decimal carbon: {carbon}')
print(f'result 2: {oxygen * carbon}')

# -------------------------------------------------------------------- #
