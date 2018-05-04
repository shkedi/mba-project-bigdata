def create_predict_dic(path, predict):
    precdict_dic = {}
    file_to_read = open(path, 'r')
    file_to_read.readline();
    i = 0
    for line in file_to_read:
        values = line.split(',')
        precdict_dic[values[0]] = predict[i]
        i = i + 1
    file_to_read.close()
    return precdict_dic

def adding_feedback(path, feedback, threshold):
    file_to_read = open(path, 'r')
    file_to_write = open(path.replace('.csv', '_adding_feedback.csv'), 'w')
    line = file_to_read.readline().split(',');
    for i in range(len(line)-1):
        file_to_write.write(line[i] + ',')
    file_to_write.write('feedback' + ',')
    file_to_write.write(line[len(line)-1])

    for line in file_to_read:
        current_line = line.split(',')
        feedback_line = feedback.get(current_line[0], str(threshold))
        for i in range(len(current_line)-1):
            file_to_write.write(current_line[i] + ',')
        file_to_write.write(str(feedback_line) + ',')
        file_to_write.write(current_line[len(current_line)-1])

    file_to_read.close()
    file_to_write.close()


def feedback_manipulation(feedback_dic, threshold):
    for key in feedback_dic:
        feedback_dic[key] = (10 * (feedback_dic[key]-threshold))
    return feedback_dic

