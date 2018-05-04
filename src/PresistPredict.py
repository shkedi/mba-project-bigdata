from src import dataLoader as dl


def presist(path, predict):
    input = dl.load_all_data(path)
    file_to_write = open(path.replace('.csv', '_predict.csv'), 'w')
    is_first = True
    i = 0
    for line in input:
        if is_first:
            file_to_write.write((','.join(line)).rstrip('\r\n') + ",predict\r\n")
            is_first = False
            continue
        file_to_write.write((','.join(line)).rstrip('\r\n') + "," + str(predict[i]) + "\r\n")
        i = i + 1
    file_to_write.close()

def presist_recomdention(path, index, predict):
    file_to_write = open(path, 'w')
    file_to_write.write('"ID","BUYER_FLAG"\r\n')
    for flag in predict:
        file_to_write.write(str(index) + ',' + str(flag) + '\r\n')
        index = index + 1
    file_to_write.close()

