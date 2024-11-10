# TODO решите задачу

def task() -> float:
    file = open("input.json", "r")
    string = file.readlines()
    sum = 0
    ch_1 = 0
    ch_2 = 0

    for i in range(len(string)):
        if string[i].find("score") != -1:
            score_i = string[i].find("score") + 8
            ch_1 = float(string[i][score_i : len(string[i]) - 2])
        elif (string[i].find("weight")) != -1:
            weight_i = string[i].find("weight") + 9
            ch_2 = float(string[i][weight_i : len(string[i]) - 1])
        if (ch_1 != 0) and (ch_2 != 0):
            sum += ch_1 * ch_2
            ch_1 = 0
            ch_2 = 0
    file.close()
    return round(sum, 3)
print(task())
