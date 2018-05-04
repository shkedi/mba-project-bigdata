def prepare_buyer_dic(path):
    buyerDic = {}
    f = open(path, 'r')
    f.readline()
    for line in f:
        line_arr = line.split(',')
        buyerDic[line_arr[0]]=line_arr[len(line_arr)-1].rstrip("\r\n")
    f.close()
    return buyerDic

def adding_factor_to_review(path, buyerDic):
    file_to_read = open(path, 'r')
    file_to_write = open(path.replace('.csv','_edit.csv'), 'w')
    file_to_write.write(file_to_read.readline().rstrip("\r\n") + ',"factor"\r\n')
    for line in file_to_read:
        file_to_write.write(line.rstrip("\r\n") + ',' + buyerDic[line.split(',')[0]] + "\r\n")
    file_to_write.close()
    file_to_read.close()

def feature_occurence(path, factor):
    file_to_read = open(path, 'r')
    sum_of_indexes = [0] * len(file_to_read.readline().split(','))
    for line in file_to_read:
        elements = line.split(',')
        for i in range(0,len(elements)):
            if factor == elements[len(elements)-1].rstrip('\r\n'):
                if (i == 0 or i == len(elements)-1):
                    sum_of_indexes[i] = 0
                else:
                    sum_of_indexes[i] = sum_of_indexes[i] + int(elements[i])
    file_to_read.close()
    return sum_of_indexes

def minimize_file(path, sum_of_negative, sum_of_positive):
    file_to_read = open(path, 'r')
    file_to_write = open(path.replace('.csv', '_remove_unimpact_feature.csv'), 'w')
    for line in file_to_read:
        elements = line.split(',')
        for i in range(0,len(elements)-1):
            if (sum_of_negative[i] + sum_of_positive[i]> 15 and abs(sum_of_negative[i] - sum_of_positive[i]) > 10) or (sum_of_negative[i] < 10 and sum_of_positive[i] < 10):
                file_to_write.write(elements[i] + ',')
        file_to_write.write(elements[len(elements)-1])
    file_to_read.close()
    file_to_write.close()

#sum_of_negative = feature_occurence('/Users/yairshkedi/tau/bigData/finalProject/reviews_training_edit.csv','0')
#sum_of_positive = feature_occurence('/Users/yairshkedi/tau/bigData/finalProject/reviews_training_edit.csv','1')
#minimize_file('/Users/yairshkedi/tau/bigData/finalProject/reviews_training_edit.csv', sum_of_negative, sum_of_positive)



