f = open("input", "r")

data = []
temp = []
for i in range(142):
    temp.append(".")
data.append(temp)

for line in f:
    temp_list = ["."]
    temp_num = ""
    for char in line:
        if(char.isdigit()):
            temp_num += char
            temp_list.append("0")
        elif char != "\n":
            if(temp_num != ""):
                temp_list[-1] = (temp_num)
                temp_num = ""
            temp_list.append(char)
    if(temp_num != ""):
        temp_list[-1] = (temp_num)
        temp_num = ""
    temp_list.append(".")
    data.append(temp_list)

temp = []
for i in range(142):
    temp.append(".")
data.append(temp)
s = 0

for i in range(len(data)):
    for u in range(len(data[i])-1):
        if not(data[i][u] in "012345679.") and not(data[i][u].isnumeric()):
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if data[i+x][u+y].isnumeric():
                        retrieve = ""
                        tp_ct = 0
                        if(data[i+x][u+y] == "0"):
                            while(data[i+x][u+y+tp_ct] == "0"):
                                data[i+x][u+y+tp_ct] = "."
                                tp_ct += 1
                
                        retrieve = data[i+x][u+y+tp_ct]
                        if(retrieve.isdigit()): s += int(retrieve)
                        data[i+x][u+y+tp_ct] = "."
print(s)
