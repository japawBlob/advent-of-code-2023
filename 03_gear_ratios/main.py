input_file="input.txt"

def second():
    pass

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

