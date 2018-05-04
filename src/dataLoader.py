def load_data(path):
    file_to_read = open(path, 'r')
    file_to_read.readline()
    x = []
    y = []
    for line in file_to_read:
        elements = line.split(',')
        tmp_x = []
        for i in range(1, len(elements) - 1):
            tmp_x.append(float(elements[i]))
        y.append(float(elements[len(elements) - 1].rstrip('\r\n')))
        x.append(tmp_x)
    file_to_read.close()
    return x, y


def load_data_no_predict(path, is_predict_exist_in_file):
    is_predict_exist = 0
    if is_predict_exist_in_file:
        is_predict_exist = 1
    file_to_read = open(path, 'r')
    file_to_read.readline()
    x = []
    for line in file_to_read:
        elements = line.split(',')
        tmp_x = []
        for i in range(1, len(elements) - is_predict_exist):
            tmp_x.append(float(elements[i]))
        x.append(tmp_x)
    file_to_read.close()
    return x


def load_all_data(path):
    file_to_read = open(path, 'r')
    x = []
    for line in file_to_read:
        elements = line.split(',')
        tmp_x = []
        for i in range(len(elements) - 1):
            tmp_x.append(elements[i])
        tmp_x.append(elements[len(elements) - 1].rstrip('\r\n'))
        x.append(tmp_x)
    file_to_read.close()
    return x