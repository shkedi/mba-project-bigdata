from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import Ridge
from xgboost import XGBClassifier
from sklearn.neighbors import NearestNeighbors


def gradient_decent(x, y):
    clf = SGDClassifier(max_iter=5, loss="log", penalty="l2")
    return clf.fit(x, y)

def random_forest(x, y):
    clf = RandomForestClassifier(max_depth=3, random_state=0)
    clf.fit(x, y)
#    print('feature importance' + clf.feature_importances_)
    return clf


def neural_networks(x, y):
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    clf.fit(x, y)
    return clf


def ridge(x, y):
    clf = Ridge(alpha=1.0)
    clf.fit(x, y)
    return clf


def xg_boost(x, y):
    model = XGBClassifier()
    model.fit(x, y)
    return model


def naive_bayes(x, y):
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb.fit(x, y)
    return gnb


def knn(x, y):
    nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree')
    nbrs.fit(x, y)
    return nbrs



