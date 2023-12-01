
def part_one():
    with open("input.txt") as f:
        sum=0
        for l in f:
            first=-1
            last=-1
            for c in l:
                if c.isdigit():
                    if first == -1:
                        first=int(c)
                    last=int(c)
            sum+=first*10+last
    print(sum)

numbers3={'one':1, 'two':2, 'six':6}
numbers4={'four':4, 'five':5, 'nine':9}
numbers5={'three':3, 'seven':7, 'eight':8}

def part_two():
    with open("input.txt") as f:
        sum=0
        for l in f:
            first=-1
            last=-1
            for c in range(len(l)):
                if l[c].isdigit():
                    if first == -1:
                        first=int(l[c])
                    last=int(l[c])
                else:
                    str_num=-1
                    if l[c:c+5] in numbers5:
                        str_num=numbers5[l[c:c+5]]
                    if l[c:c+4] in numbers4:
                        str_num=numbers4[l[c:c+4]]
                    if l[c:c+3] in numbers3:
                        str_num=numbers3[l[c:c+3]]
                    if str_num != -1:
                        if first == -1:
                            first=str_num
                        last=str_num
            sum+=first*10+last
    print(sum)

if __name__ == "__main__":
    part_one()
    part_two()

