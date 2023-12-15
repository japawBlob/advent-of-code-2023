input_file="input.txt"

def arr_to_int(arr):
    summ=0
    for i, number in enumerate(arr[::-1]):
        summ+=number*(10**i) 
    return summ

def search_left_and_right(x, line):
    ret1=search_left(x,line)
    ret2=search_right(x,line)
    return ret1+ret2[1:]

def search_right(x, line):
    ret=[]
    while line[x].isdigit() and x < len(line):
        ret.append(int(line[x]))
        x+=1
    return ret

def search_left (x, line):
    ret=[]
    while line[x].isdigit() and x >= 0:
        ret.append(int(line[x]))
        x-=1
    return ret[::-1]

def search_line(x_left, x_right, line):
    numbers=[]
    digit_location=[]
    for i in range(x_left, x_right+1):
        if (line[i].isdigit()):
            digit_location.append(True)
        else:
            digit_location.append(False)
    if len(digit_location)>2:
        if digit_location[0] and digit_location[2] and not digit_location[1]:
            left = search_left(x_left, line)
            right = search_right(x_right, line)
            return[arr_to_int(left),arr_to_int(right)]
    for i, present in enumerate(digit_location):
        if present:
            digits = search_left_and_right(x_left+i, line)
            numbers.append(arr_to_int(digits))
            break
    return numbers

def resolve_star(x, prev_line, curr_line, next_line):
    # check of digit around star
    x_left = max(0, x-1)
    x_right = min(x+1, len(curr_line)-1)
    numbers=[]
    # prev
    numbers+=search_line(x_left, x_right, prev_line)
    # curr
    numbers+=search_line(x_left, x_right, curr_line)
    # next
    numbers+=search_line(x_left, x_right, next_line)
    if len(numbers) == 2:
        return numbers[0]*numbers[1]
    return 0

def second():
    final_result=[]
    with open(input_file) as file:
        lines = file.readlines()
        for y, line in enumerate(lines):
            line=line.rstrip()
            prev_line=lines[y-1] if y-1 >= 0 else '.'*len(line)
            curr_line=line
            next_line=lines[y+1] if y+1 < len(lines) else '.'*len(line)

            for x, char in enumerate(curr_line):
                if char == '*':
                    result = resolve_star(x, prev_line, curr_line, next_line) 
                    if result != 0:
                        final_result.append(result)
    return sum(final_result)

def resolve_position(x1, x2, prev_line, curr_line, next_line):
    #print('index1: ', x1, '->' ,curr_line[x1], '|', 'index2: ',x2, '->' ,curr_line[x2],curr_line, end='\n')
    new_x1 = max(x1-1, 0)
    new_x2 = min(x2+2, len(curr_line))
    for x in range(new_x1, new_x2):
        if prev_line[x] != '.':
            #print("prev_line catch:", prev_line[x], "On index", x)
            return True
        if next_line[x] != '.':
            #print("next_line catch:", next_line[x], "On index", x)
            return True
    if x1 > 0 and curr_line[x1-1] != '.':
        #print("curr_line catch:", curr_line[x1-1], "On index", x1-1)
        return True
    if x2+1 < len(curr_line) and curr_line[x2+1] != '.':
        #print("curr_line catch:", curr_line[x2+1], "On index", x2+1)
        return True
    return False
        

def first():
    final_result=[]
    with open(input_file) as file:
        lines = file.readlines()
        for y, line in enumerate(lines):
            line=line.rstrip()
            prev_line=lines[y-1] if y-1 >= 0 else '.'*len(line)
            curr_line=line
            next_line=lines[y+1] if y+1 < len(lines)-1 else '.'*len(line)

            current_digit=[];
            for x, char in enumerate(curr_line):
                if char.isdigit():
                    current_digit.append((char, x))
                else:
                    if current_digit:
                        value=0      
                        for iteration,digit in enumerate(reversed(current_digit)):
                            value+=int(digit[0])*(10**iteration)
                        if resolve_position(current_digit[0][1], current_digit[-1][1], prev_line, curr_line, next_line):
                            final_result.append(value)
                    current_digit=[]
            if current_digit:
                value=0      
                for iteration,digit in enumerate(reversed(current_digit)):
                    value+=int(digit[0])*(10**iteration)
                if resolve_position(current_digit[0][1], current_digit[-1][1], prev_line, curr_line, next_line):
                    final_result.append(value)
    return sum(final_result)

if __name__ == '__main__':
    #print("            0123456789")
    print(first())
    print(second())

