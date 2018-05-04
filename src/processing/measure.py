def recall(tp, fn):
    return float(tp)/(tp+fn)


def accuracy(tp, tn, fp, fn):
    return float(tp + tn)/(tp + tn + fp + fn)


def precision(tp, fp):
    if (tp + fp == 0):
        return 1;
    return float(tp)/(tp + fp)


def matrix_confuzion(actual, excpted):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for x in range(len(actual)):
        if (actual[x] == excpted[x]) and (actual[x] == 1):
            tp = tp + 1
        elif (actual[x] == excpted[x]) and (actual[x] == 0):
            tn = tn + 1
        elif actual[x] == 0:
            fp = fp + 1
        else :
            fn = fn + 1
    return tp, tn, fp, fn

def threshold(predict, threshold):
    result = []
    for x in predict:
        if x > threshold:
            result.append(1)
        else:
            result.append(0)
    return result

