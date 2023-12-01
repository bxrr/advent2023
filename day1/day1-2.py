# this file reformats the input file so it can be used with part 1's code

f1 = open("input", "r")
f2 = open("input_new", "w")

data = [
    ["one", "on1ne"],
    ["two", "tw2wo"], 
    ["three", "th3ree"],
    ["four", "fo4ur"], 
    ["five", "fi5ve"],
    ["six", "si6ix"],
    ["seven", "se7ven"],
    ["eight", "ei8ght"],
    ["nine", "ni9ne"],
    ["zero", "ze0ro"]
]

for line in f1:
    for item in data:
        line = line.replace(item[0], str(item[1]))
    f2.write(line)