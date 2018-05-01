from sklearn.neural_network import MLPClassifier
X = [[0., 0.], [1., 1.]]
y = [0, 1]
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                     hidden_layer_sizes=(5, 2), random_state=1)

clf.fit(X, y)

MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
       beta_1=0.9, beta_2=0.999, early_stopping=False,
       epsilon=1e-08, hidden_layer_sizes=(5, 2), learning_rate='constant',
       learning_rate_init=0.001, max_iter=200, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
       solver='lbfgs', tol=0.0001, validation_fraction=0.1, verbose=False,
       warm_start=False)
#After fitting (training), the model can predict labels for new samples:

print clf.predict([[2., 2.], [-1., -2.]])
#MLP can fit a non-linear model to the training data. clf.coefs_ contains the weight matrices that constitute the model parameters:

print [coef.shape for coef in clf.coefs_]
#[(2, 5), (5, 2), (2, 1)]'''