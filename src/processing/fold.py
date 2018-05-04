import numpy as np
from sklearn.model_selection import KFold
import measure as measure


def kfold(x,y, algorithm):
    x_array = np.array(x)
    y_array = np.array(y)
    predict_y = []
    split = 10
    forumola = []
    kf = KFold(n_splits=split)
    sum_precision = 0
    sum_acc = 0
    sum_recall = 0
    for train_index, test_index in kf.split(x_array):
        current_algorithm = algorithm(x_array[train_index], y_array[train_index])
        forumola.append(current_algorithm)
        current_predict = current_algorithm.predict(x_array[test_index])
        predict_y.append(current_predict)
        current_experiment = measure.matrix_confuzion(y_array[test_index], measure.threshold(current_predict, 0.5))

        recall = measure.recall(current_experiment[0], current_experiment[3])
        acc = measure.accuracy(current_experiment[0], current_experiment[1], current_experiment[2], current_experiment[3])
        presion = measure.precision(current_experiment[0], current_experiment[2])

        sum_precision = sum_precision + presion
        sum_acc = sum_acc + acc
        sum_recall = sum_recall + recall
    sum_acc = float(sum_acc)/split
    sum_precision = float(sum_precision) / split
    sum_recall = float(sum_recall) / split
    print 'avg presicion: ' + str(sum_precision)
    print 'avg acc: ' + str(sum_acc)
    print 'avg recall: ' + str(sum_recall)
    return forumola, predict_y


def kfold_predict(x, formula):
    x_array = np.array(x)
    predict_y = []
    alg_result = []
    split = 10
    kf = KFold(n_splits=split)
    i = 0
    positive = 0
    for train_index, test_index in kf.split(x_array):
        for x in formula[i].predict(x_array[test_index]):
            if x > 0.5:
                predict_y.append(1)
                positive = positive + 1
            else:
                predict_y.append(0)
            alg_result.append(x)
        i = i + 1
    return predict_y, alg_result


def kfold_with_formula(x,y, formula):
    x_array = np.array(x)
    y_array = np.array(y)
    predict_y = []
    split = 10
    kf = KFold(n_splits=split)
    sum_precision = 0
    sum_acc = 0
    sum_recall = 0
    i = 0
    for train_index, test_index in kf.split(x_array):
        current_predict = formula[i].predict(x_array[test_index])
        i = i + 1
        predict_y.append(current_predict)
        current_experiment = measure.matrix_confuzion(y_array[test_index], measure.threshold(current_predict, 0.5))

        recall = measure.recall(current_experiment[0], current_experiment[3])
        acc = measure.accuracy(current_experiment[0], current_experiment[1], current_experiment[2], current_experiment[3])
        presion = measure.precision(current_experiment[0], current_experiment[2])

        sum_precision = sum_precision + presion
        sum_acc = sum_acc + acc
        sum_recall = sum_recall + recall
    sum_acc = float(sum_acc)/split
    sum_precision = float(sum_precision) / split
    sum_recall = float(sum_recall) / split
    print 'avg presicion: ' + str(sum_precision)
    print 'avg acc: ' + str(sum_acc)
    print 'avg recall: ' + str(sum_recall)
    return predict_y

