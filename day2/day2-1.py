f = open("input", "r")

def replace_check(og, color, num):
    if og.find(color) != -1:
        og = og.replace(color, "").replace(" ", "").replace("\\n", "")
        if(int(og) <= num):
            return num
        else: return int(og)
    return num


s = 0

for line in f:
    temp = str(line)
    temp = temp.replace("Game ", "").replace(";", ",")
    num = temp[0:temp.find(":")]
    num = int(num)
    temp = temp[temp.find(":")+1:]
    new_temp = temp.split(",")

    mb=0
    mr=0
    mg=0

    for item in new_temp:
        mr = replace_check(item, "red", mr)
        mg = replace_check(item, "green", mg)
        mb = replace_check(item, "blue", mb)
            
    s += mr * mg * mb

print(s)