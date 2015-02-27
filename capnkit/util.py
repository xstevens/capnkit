import gzip

import capnp
import feature_extraction_capnp
import classification_capnp

from .feature_extraction import *
from .classification import *

def load_msg(cpnpc, filename):
    with gzip.open(filename, mode='rb') as f:
        return cpnpc.read(f)
    return None


def load(cpnpc, filename):
    msg = load_msg(cpnpc, filename)
    if isinstance(msg, feature_extraction_capnp.NgramVectorizer.Reader):
        return _capnp_to_count_vectorizer(msg)
    elif isinstance(msg, feature_extraction_capnp.TfidfTransformer.Reader):
        return _capnp_to_tfidf_transformer(msg)
    elif isinstance(msg, classification_capnp.LogisticRegression.Reader):
        return _capnp_to_logisticreg(msg)
    else:
        raise Exception('Unknown message type: %s' % cpnpc)


def dump(obj, filename):
    msg = None
    if isinstance(obj, CountVectorizer):
        msg = _count_vectorizer_to_capnp(obj)
    elif isinstance(obj, TfidfTransformer):
        msg = _tfidf_transformer_to_capnp(obj)
    elif isinstance(obj, LogisticRegression):
        msg = _logisticreg_to_capnp(obj)
    else:
        raise Exception('Cannot serialize object type: ' % str(type(obj)))
        
    with gzip.open(filename, mode='wb') as f:
        msg.write(f)

