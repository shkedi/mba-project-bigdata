from src import dataLoader as dl

input = dl.load_data('/Users/yairshkedi/tau/bigData/finalProject/ffp_train.csv')
columns = [0]*len(input[0][1])
for line in input[0]:
    i = 0
    for elem in line:
        columns[i] = columns[i] + float(elem)
        i = i + 1

columns = [x/len(input[0]) for x in columns]
print columns;

columns = [0]*len(input[0][1])
for line in input[0]:
    i = 0
    for elem in line:
        if (float(elem) > columns[i]):
            columns[i] = float(elem)
        i = i + 1

print 'max'
print columns;

columns = [0]*len(input[0][1])
for line in input[0]:
    i = 0
    for elem in line:
        if (float(elem) < columns[i]):
            columns[i] = float(elem)
        i = i + 1

print 'min'
print columns;

recent_pur = []
avg_t_pur = []
food_y1 = []
food_y2 = []
food_y3 = []
food_y4 = []
food_y5 = []
hooby_l1 = []
hooby_l2 = []
hooby_l3 = []
hooby_l4 = []
hooby_l5 = []

for line in input[0]:
    recent_pur.append(float(line[5]))
    avg_t_pur.append(float(line[6]))
    food_y1.append(float(line[7]))
    food_y2.append(float(line[8]))
    food_y3.append(float(line[9]))
    food_y4.append(float(line[10]))
    food_y5.append(float(line[11]))
    hooby_l1.append(float(line[12]))
    hooby_l2.append(float(line[13]))
    hooby_l3.append(float(line[14]))
    hooby_l4.append(float(line[15]))
    hooby_l5.append(float(line[16]))

recent_pur.sort()
avg_t_pur.sort()
food_y1.sort()
food_y2.sort()
food_y3.sort()
food_y4.sort()
food_y5.sort()
hooby_l1.sort()
hooby_l2.sort()
hooby_l3.sort()
hooby_l4.sort()
hooby_l5.sort()

print 'mid'
print recent_pur[len(input[0])/2]
print avg_t_pur[len(input[0])/2]
print food_y1[len(input[0])/2]
print food_y2[len(input[0])/2]
print food_y3[len(input[0])/2]
print food_y4[len(input[0])/2]
print food_y5[len(input[0])/2]
print hooby_l1[len(input[0])/2]
print hooby_l2[len(input[0])/2]
print hooby_l3[len(input[0])/2]
print hooby_l4[len(input[0])/2]
print hooby_l5[len(input[0])/2]

print 'small - 1/20'
print recent_pur[1000]
print avg_t_pur[160]
print food_y1[160]
print food_y2[160]
print food_y3[160]
print food_y4[160]
print food_y5[160]
print hooby_l1[160]
print hooby_l2[160]
print hooby_l3[160]
print hooby_l4[160]
print hooby_l5[160]

print 'big - 1/20'
print recent_pur[32000 - 1000]
print avg_t_pur[32000 - 160]
print food_y1[32000 - 160]
print food_y2[32000 - 160]
print food_y3[32000 - 160]
print food_y4[32000 - 160]
print food_y5[32000 - 160]
print hooby_l1[32000 - 160]
print hooby_l2[32000 - 160]
print hooby_l3[32000 - 160]
print hooby_l4[32000 - 160]
print hooby_l5[32000 - 160]

#food l2 remove -9999 and + 100000
#food l4 remove 100000
#hooby_l1 remove 100000
#hooby_l5 remove -100000

