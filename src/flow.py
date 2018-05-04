import preprocessing.PrepareReview as pr
import preprocessing.featureEngeniring as fe
import processing.fold as f
import preprocessing.manipulateFeedback as mf
import preprocessing.normalize as n
import preprocessing.predictAlgorithm as pa
import preprocessing.upSample as us

import PresistPredict as pp
from src import dataLoader as dl


def sum_predict(predict, real):
    x = 0
    sum = 0
    for elem in real:
        sum = sum + 1
        if elem == 1:
            x = x + 1

    print '----real-----'
    print 'positive:' + str(x)
    print 'sum:' + str(sum)
    print float(x) / sum

    x = 0
    sum = 0
    for elem in predict:
        for i in elem:
            sum = sum + 1
            if i > 0.5:
                x = x + 1
    print '----predict-----'
    print 'positive:' + str(x)
    print 'sum:' + str(sum)
    print float(x) / sum

path_to_file = '/Users/yairshkedi/tau/bigData/finalProject/'
input = dl.load_data(path_to_file + 'data.csv')
#preprocessing

#remove columns

#edit values

#feature engenring

#adding more data

#normilized

#up sample if needed


normelized_x = n.normelized(input[0])

print 'some algorithm'
predict_y = f.kfold(input[0], input[1], pa.gradient_decent) #example of algorithm
sum_predict(predict_y[1], input[1])  #calculate measure
