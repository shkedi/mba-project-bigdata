from sklearn.utils import resample
import src.dataLoader as dl
from random import shuffle

#should check if needed
def upSample(path):
    input = dl.load_all_data(path)
    df_majority = []
    df_minority = []
    is_first = True
    first_line = []
    line1 = []
    for line in input:
        if is_first:
            is_first = False
            first_line = line
            continue
        if line[len(line)-1] == '0':
            df_majority.append(line)
        else:
            df_minority.append(line)
        line1.append(line)

    df_minority_upsampled = resample(df_minority, replace=True, n_samples=34576, random_state=123)

    mixDataList = df_minority_upsampled + df_majority;
    shuffle(mixDataList)

    file_to_write = open(path.replace('.csv', '_up_sample.csv'), 'w')
    file_to_write.write(','.join(first_line) + '\r\n')

    for line in mixDataList:
        file_to_write.write(','.join(line) + '\r\n')
    file_to_write.close()


