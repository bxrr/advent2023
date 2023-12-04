
    line = line[line.find(":")+2:].replace("  ", " ").replace("\n", "")
    split = line.split(" | ")
    winning_nums = split[0].split(" ")