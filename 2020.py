# coding=utf-8
import re
import sys
import unittest


def dec1_1():
    data = []
    floor = 0
    index = 1
    with open('dec1-1.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())
    for char in data[0]:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        else:
            print('ERROR')
        if floor < 0:
            print('part 2', index)
            return
        index += 1
    print('part 1', floor)


def dec2_1():
    data = []
    total = 0
    with open('dec2-2.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    for present in data:
        l, w, h = present.split('x')
        l = int(l)
        w = int(w)
        h = int(h)
        print(l, w, h, present)
        size = 2*l*w + 2*l*h + 2*w*h
        size += min(l*w, l*h, w*h)
        total += size
    print(total)




def dec2_2():
    # format 6-11 c: dccxcccccchrcfdckcsc
    valid = 0
    regex = r"(\d+).(\d+) (\w): (\w+)"
    with open('dec19-2.txt', 'r') as f:
        for cnt, line in enumerate(f):
            match = re.search(regex, line)
            first = int(match.group(1))
            second = int(match.group(2))
            c = (match.group(3))
            my_str = (match.group(4))
            matches = 0
            if my_str[first-1] == c:
                matches += 1
            if my_str[second - 1] == c:
                matches += 1

            if matches == 1:
                valid += 1
    print(valid)


def dec3_1():
    # format 6-11 c: dccxcccccchrcfdckcsc
    hits = 0
    current_spot = 0
    slope = 3
    hill = []
    with open('dec3_1.txt', 'r') as f:
        for cnt, line in enumerate(f):
            hill.append(line.strip())

    for line in hill:
        if line[current_spot] == '#':
            hits += 1
        print(line[:current_spot], line[current_spot], line[current_spot+1:], current_spot, hits)
        current_spot += slope
        current_spot = current_spot % len(line)


def calculate_slope(hill, slope, skip):
    current_spot = 0
    hits = 0
    for index, line in enumerate(hill):
        if index % 2 == 1 and skip:
            continue
        if line[current_spot] == '#':
            hits += 1
        # print (line[:current_spot], line[current_spot], line[current_spot+1:], current_spot, hits)
        current_spot += slope
        current_spot = current_spot % len(line)
    return hits


def dec3_2():
    # format 6-11 c: dccxcccccchrcfdckcsc
    hill = []
    with open('dec3_1.txt', 'r') as f:
        for cnt, line in enumerate(f):
            hill.append(line.strip())

    total = calculate_slope(hill, 1, False)
    total *= calculate_slope(hill, 3, False)
    total *= calculate_slope(hill, 5, False)
    total *= calculate_slope(hill, 7, False)
    total *= calculate_slope(hill, 1, True)

    print(total)


def is_valid_passport_1(passport):
    if 'byr' not in passport \
            or 'iyr' not in passport \
            or 'eyr' not in passport \
            or 'hgt' not in passport \
            or 'hcl' not in passport \
            or 'ecl' not in passport \
            or 'pid' not in passport:
        return 0
    return 1


def is_valid_passport_2(passport):
    if 'byr' not in passport \
            or 'iyr' not in passport \
            or 'eyr' not in passport \
            or 'hgt' not in passport \
            or 'hcl' not in passport \
            or 'ecl' not in passport \
            or 'pid' not in passport:
        return 0
    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        return 0
    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        return 0
    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        return 0
    height = passport['hgt']
    result = re.match('(\d+)(.*)', height)
    if result.group(2) == 'cm':
        if int(result.group(1)) < 150 or int(result.group(1)) > 193:
            return 0
    elif result.group(2) == 'in':
        if int(result.group(1)) < 59 or int(result.group(1)) > 76:
            return 0
    else:
        return 0

    hair_color = passport['hcl']
    result = re.match('^#[0-9a-f]{6}$', hair_color)
    if not result:
        return 0

    eye_color = passport['ecl']
    if eye_color not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return 0

    if len(passport['pid']) != 9:
        return 0
    return 1


def dec4_1():
    data = []
    valid = 0
    with open('dec4.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)

    passports = []
    passport = {}
    for line in data:
        if line == "":
            passports.append(passport)
            passport = {}
            continue
        data = line.split()
        for value in data:
            pair = value.split(":")
            passport[pair[0]] = pair[1]
    passports.append(passport)

    for passport in passports:
        valid += is_valid_passport_2(passport)
        print(valid)


def get_id(b_pass):
    val = 1
    my_id = 0
    for c in reversed(b_pass):
        if c in ('R', 'B'):
            my_id += val
        val *= 2
    return my_id


def dec5_1():
    # FBFBBFFRLR - B = 1 and R = 1 convert to binary number
    data = []
    highest_id = 0

    with open('dec5.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)

    for b_pass in data:
        my_id = get_id(b_pass)
        if my_id > highest_id:
            highest_id = my_id

    print(highest_id)


def dec5_2():
    # FBFBBFFRLR - B = 1 and R = 1 convert to binary number
    data = []
    ids = [0]*900
    lowest_id = 10000
    with open('dec5.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)

    for b_pass in data:
        my_id = get_id(b_pass)
        ids[my_id] = 1
        if my_id < lowest_id:
            lowest_id = my_id

    print(ids)
    for value, my_id in enumerate(ids):
        if my_id == 0 and value > lowest_id:
            print(value)
            return


def process_group(group):
    print(group)
    print(len(group))
    return len(group)


def dec6_1():
    data = []
    total = 0
    with open('dec6.txt', 'r') as f:
        for cnt, line in enumerate(f):
            line = line.strip()
            data.append(line)

    group = {}
    new_group = True
    for line in data:
        if line == "":
            total += process_group(group)
            group = {}
            new_group = True
            continue
        if new_group:
            new_group = False
            for value in line:
                group[value] = 1
        else:
            for key, value in group.items():
                if key not in line:
                    del group[key]
    total += process_group(group)
    print(total)


def dec7_1():
    data = {}
    regex_non = r"(.*) bags contain no other bags"
    regex = r"(.*?) bags contain(.*)."
    bag_regex = r"\d+ (.*) bags?"
    with open('dec7_test.txt', 'r') as f:
        for cnt, line in enumerate(f):
            bag = line.strip()

            if re.search(regex_non, bag):
                data[match.group(1)] = {}
                print("No match", bag)
                continue

            match = re.search(regex, bag)
            # print(match.group(0))
            outside = match.group(1)
            bags = match.group(2).split(', ')

            for bag in bags:
                match = re.search(bag_regex, bag)
                if match.group(1) in data:
                    data[match.group(1)].append(outside)
                else:
                    data[match.group(1)] = [outside]

    print('data', data)
    exists_in = []
    bags = ['shiny gold']
    while bags:
        bag = bags.pop()
        if bag in exists_in:
            continue
        print('now', bag)
        exists_in.append(bag)
        if bag in data:
            bags.extend(data[bag])
    print(exists_in)
    print(len(exists_in) - 1)


def solve(color, data):
    root = data[color]

    if root is None:
        return 0
    else:
        print('X', root)
        return sum([root[key]*solve(key, data) + root[key] for key in root])


def dec7_2():
    data = {}
    regex_non = r"(.*) bags contain no other bags."
    regex = r"(.*?) bags contain(.*)."
    bag_regex = r"(\d+) (.*) bags?"
    with open('dec7.txt', 'r') as f:
        for cnt, line in enumerate(f):
            bag = line.strip()

            match = re.search(regex_non, bag)
            if match:
                data[match.group(1)] = None
                continue

            match = re.search(regex, bag)
            outside = match.group(1)
            bags = match.group(2).split(', ')

            for bag in bags:

                match = re.search(bag_regex, bag)
                bag_data = {match.group(2): int(match.group(1))}
                if outside in data:
                    data[outside][match.group(2)] = int(match.group(1))
                else:
                    data[outside] = bag_data

    print(data)
    print(solve('shiny gold', data))


def dec8_1():
    data = []
    acc = 0
    index = 0
    with open('dec8.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    while data[index]:
        line = data[index]
        if not line:
            break
        operation = line[0:3]
        print(operation, line)
        if operation == 'nop':
            data[index] = None
            index += 1
        elif operation == 'jmp':
            data[index] = None
            index += int(line[4:])
        elif operation == 'acc':
            data[index] = None
            acc += int(line[4:])
            index += 1
        else:
            print('ERROR')

    print(acc)


def run(line, index, acc):
    operation = line[:3]
    if operation == 'nop':
        index += 1
    elif operation == 'jmp':
        index += int(line[4:])
    elif operation == 'acc':
        acc += int(line[4:])
        index += 1
    else:
        print('ERROR')
    return index, acc


def dec8_2():
    data = []
    with open('dec8.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    stored_data = data[:]
    swap_line = 0
    while swap_line < len(data):
        acc = 0
        index = 0
        data = stored_data[:]
        if data[swap_line][:3] == 'nop':
            data[swap_line] = 'jmp' + data[swap_line][4:]
        elif data[swap_line][:3] == 'jmp':
            data[swap_line] = 'nop' + data[swap_line][4:]
        else:
            swap_line += 1
            continue
        swap_line += 1
        while data[index]:
            line = data[index]
            data[index] = None
            (index, acc) = run(line, index, acc)

            if index == len(data):
                print('Success!!!', acc)
                return
            if index > len(data):
                break

    print(acc)


def dec9_1_and_2():
    data = []
    with open('dec9.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(int(line.strip()))

    print(data)
    index = 0
    last_25 = {}
    fail = 0
    while len(last_25) < 25:
        element = data[index]
        if element not in last_25:
            last_25[element] = 1
        else:
            last_25[element] += 1
        index += 1

    while index < len(data):
        element = data[index]
        works = False
        for item in last_25:
            if element - item in last_25:
                works = True
                break
        if not works:
            fail = element
            print(f"item {element} is the answer to part 1")
            break
        element = data[index]
        last_25[element] = last_25.get(element, 0) + 1

        element = data[index - 25]
        if last_25[element] > 1:
            last_25[element] -= 1
        else:
            del last_25[element]

        index += 1

    # Part 2
    for i in range(len(data)):
        total = data[i]
        smallest = data[i]
        largest = data[i]
        start = data[i]
        while total < fail:
            i += 1
            total += data[i]
            if data[i] < smallest:
                smallest = data[i]
            if data[i] > largest:
                largest = data[i]

        if total == fail and data[i] != start:
            print(f"start is {start} end is {data[i]}")
            print(f"{smallest+largest} is the answer to part 2")
            return


def dec10_1():
    data = []
    ones = 0
    threes = 0
    current = 0
    with open('dec10.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(int(line.strip()))

    data.sort()
    for x in data:
        if current + 1 == x:
            ones += 1
        if current + 3 == x:
            threes += 1
        current = x
    threes += 1
    print(ones * threes)


def figure_ways(data):
    if len(data) == 0:
        return 0
    if len(data) < 3:
        return 1
    ways = 0
    ways += figure_ways(data[1:])
    ways += figure_ways(data[2:])
    ways += figure_ways(data[3:])
    return ways


def dec10_2():
    adapters = []
    with open('dec10.txt', 'r') as f:
        for cnt, line in enumerate(f):
            adapters.append(int(line.strip()))
        adapters.append(0)

    adapters.sort()
    adapters.append(adapters[-1]+3)

    start = 0
    prev = 0
    paths = 1
    for i in range(len(adapters)):
        x = adapters[i]
        if prev + 3 == x:
            my_paths = figure_ways(adapters[start:i])
            print(my_paths, adapters[start:i])
            paths *= my_paths
            start = i
        prev = adapters[i]

    print(paths)


def dec16_1():
    data = []
    total = 0
    with open('dec16.txt', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip())

    valid_nums = [False]*1000
    line = data.pop(0)
    possibilities = []
    regex = re.compile('(.*): (\d+)-(\d+) or (\d+)-(\d+)')
    while line:  # rules
        my_obj = {}
        match = re.search(regex, line)
        name = match.group(1)
        start1 = int(match.group(2))
        end1 = int(match.group(3))
        start2 = int(match.group(4))
        end2 = int(match.group(5))
        my_obj['name'] = name
        my_obj['s1'] = start1
        my_obj['e1'] = end1
        my_obj['s2'] = start2
        my_obj['e2'] = end2
        my_obj['rows'] = [True]*20
        possibilities.append(my_obj)
        for i in range(start1, end1):
            valid_nums[i] = True
        for i in range(start2, end2):
            valid_nums[i] = True
        print(f'{start1} {end1}    {start2} {end2}')
        line = data.pop(0)
    print(possibilities)


    data.pop(0)
    my_ticket = data.pop(0)
    my_ticket = my_ticket.split(',')
    for i in range(len(my_ticket)):
        my_ticket[i] = int(my_ticket[i])
    data.pop(0)
    data.pop(0)

    err_sum = 0

    valid_tickets = [my_ticket]
    for ticket in data:
        invalid = False
        vals = ticket.split(',')
        for val in vals:
            if valid_nums[int(val)]:
                continue
            err_sum += int(val)
            invalid = True
        for i in range(len(vals)):
            vals[i] = int(vals[i])
        if not invalid:
            valid_tickets.append(vals)
    print(err_sum, len(valid_tickets), valid_tickets)

    print(valid_tickets[0][0], valid_tickets[1][1])
    for pos in possibilities:
        print(pos)
        for i in range(len(pos['rows'])):
            if not pos['rows'][i]:
                continue
            for ticket in valid_tickets:
                if ticket[i] < pos['s1']:
                    pos['rows'][i] = False
                if ticket[i] > pos['e2']:
                    pos['rows'][i] = False
                if ticket[i] > pos['e1'] and ticket[i] < pos['s2']:
                    pos['rows'][i] = False
    print('RESULT')
    print(possibilities)
    for pos in possibilities:
        print(pos)

    print('Now solve manually, first one row has only one truth, then after one column will have one truth')
    print(my_ticket[14] * my_ticket[12] * my_ticket[15] * my_ticket[3] * my_ticket[17] * my_ticket[4])



# class TestAll(unittest.TestCase):
#     def test_dec5_ids(self):
#         self.assertEqual(get_id('FBFBBFFRLR'), 357)
#         self.assertEqual(get_id('BFFFBBFRRR'), 567)
#         self.assertEqual(get_id('FFFBBBFRRR'), 119)
#         self.assertEqual(get_id('BBFFBBFRLL'), 820)


if __name__ == '__main__':
    # unittest.main()
    dec16_1()
