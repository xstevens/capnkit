import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing.label import LabelEncoder

import capnp
import classification_capnp

def _capnp_to_logisticreg(clfmsg):
    coef = np.array(clfmsg.coef)
    # for consistency wrap this thing in an np.array, not sure why scikit does this
    intercept = np.array([np.float64(clfmsg.intercept)])
    clf = LogisticRegression()
    clf.coef_ = coef
    clf.intercept_ = intercept
    # TODO: persist this in dump and make this multi-class safe
    clf._enc = LabelEncoder()
    clf._enc.classes_ = np.array([0, 1])
    
    return clf

    
def _logisticreg_to_capnp(clf):
    clfmsg = classification_capnp.LogisticRegression.new_message()
    rows = clfmsg.init('coef', clf.coef_.shape[0])
    for i, row in enumerate(clf.coef_):
        rows[i] = clf.coef_[i].tolist()
    
    clfmsg.intercept = float(clf.intercept_[0])
    return clfmsg