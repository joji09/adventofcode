import re

def mul(x,y):
    return x*y

with open("3.txt", "r") as f:
    content = f.read()

    result = 0
    regrex = '(mul\([0-9]{1,3}\,[0-9]{1,3}\))' #part 1
    regrex2 = '(mul\([0-9]{1,3}\,[0-9]{1,3}\))|(do\(\))|(don\'t\(\))' #part 2
    process = re.findall(regrex2, content)
    flag_enable = True
    for p in process:
        # result += eval(p) - PART 1
        process2 = ",".join(s for s in p if (len(s) > 0))
        if(flag_enable and "mul" in process2):
            result += eval(process2)
        elif "don't" in process2:
            flag_enable = False
        elif "do()" in process2:
            flag_enable = True

print(result)