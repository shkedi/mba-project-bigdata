import src.dataLoader as dl


def remove_extreme_data(path):
    lines = dl.load_all_data(path)
    file_to_write = open(path.replace('.csv', '_reduce_extreme.csv'), 'w')
    isFirst = True
    for line in lines:
        isShouldExclude = False
        if isFirst:
            file_to_write.write(','.join(line) + '\r\n')
            isFirst = False
            continue
        for elem in line:
            if (float(elem) > 100000000) or (float(elem) < -100000000):
                isShouldExclude = True
                break
        if isShouldExclude == False:
           file_to_write.write(','.join(line) + '\r\n')
    file_to_write.close()


def remove_catalog(path):
    lines = dl.load_all_data(path)
    file_to_write = open(path.replace('.csv', '_remove_catalog.csv'), 'w')
    for line in lines:
        index = 0
        for elem in line:
            if (index != 1 and index != (len(line)-1)):
                file_to_write.write(elem + ',')
            elif index == (len(line)-1):
                file_to_write.write(elem + '\r\n')
            index = index + 1
    file_to_write.close()


def adding_avg(path, type):
    lines = dl.load_all_data(path)
    indexes = []
    i = 0
    for elem in lines[0]:
        if elem.startswith(type) or elem.startswith('"' + type):
            indexes.append(i)
        i = i + 1
    file_to_write = open(path.replace('.csv', '_adding_avg_' + type + '.csv'), 'w')
    first_line = lines[0][0:len(lines[0])-1] + [type + '_AVG'] + [lines[0][len(lines[0]) - 1]]
    file_to_write.write(','.join(first_line) + '\r\n')

    for line in lines[1:]:
        index = 0
        sum = 0
        for elem in line:
            if index in indexes:
                sum = sum + float(elem)
            if index != (len(line)-1):
                file_to_write.write(elem + ',')
            else:
                file_to_write.write(str(sum/len(indexes)) + ',' + elem + '\r\n')
            index = index + 1
    file_to_write.close()

#remove_extreme_data('/Users/yairshkedi/tau/bigData/finalProject/ffp_train.csv')
#remove_catalog('/Users/yairshkedi/tau/bigData/finalProject/ffp_train_reduce_extreme.csv')
#adding_avg('/Users/yairshkedi/tau/bigData/finalProject/ffp_train_reduce_extreme.csv', 'FOOD')
#adding_avg('/Users/yairshkedi/tau/bigData/finalProject/ffp_train_reduce_extreme_adding_avg_FOOD.csv', 'HOBBY')