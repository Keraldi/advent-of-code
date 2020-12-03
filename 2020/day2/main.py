# input file pattern: <int1>-<int2> <char>: <string>
# wheras int1 and int2 are start and end slice, <char> the char it must be in <string>

file = open('patterns', mode="r")
inp = file.read().splitlines()


def policy1(_input):
    valid = 0

    for line in _input:
        pattern, password = line.split(':')
        password = password[1::]
        intrange, char = pattern.split(' ')
        _min, _max = [int(element) for element in intrange.split('-')]

        count = 0
        for character in password:
            if character == char:
                count += 1

        if _min <= count <= _max:
            valid += 1

    return valid


def policy2(_input):
    valid = 0

    for line in _input:
        pattern, password = line.split(':')
        intrange, char = pattern.split(' ')
        pos1, pos2 = [int(element) for element in intrange.split('-')]

        if (password[pos1] == char) ^ (password[pos2] == char):
            valid += 1

    return valid


print(policy2(inp))
