f = open("input", "r")
f2 = open("outputs", "w")

total = 0
for line in f:
    line = line[line.find(":")+2:].replace("  ", " ").replace("\n", "")
    split = line.split(" | ")
    winning_nums = split[0].split(" ")
    nums = split[1].split(" ")
    
    s = 0
    i = 0
    for n in nums:
        if n in winning_nums:
            s = 1 if s == 0 else s * 2
            i += 1
        f2.write(str(i) + "\n")
    total += s

print(total)