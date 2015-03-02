import gzip

import capnp
import feature_extraction_capnp
import classification_capnp

from feature_extraction import _capnp_to_count_vectorizer, _capnp_to_tfidf_transformer, _count_vectorizer_to_capnp, _tfidf_transformer_to_capnp
from classification import _capnp_to_logisticreg, _logisticreg_to_capnp

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression

def _load_msg(cpnpc, filename):
    with gzip.open(filename, mode='rb') as f:
        return cpnpc.read(f)
    return None


def load(typ, filename):
    if CountVectorizer == typ:
        return _capnp_to_count_vectorizer(_load_msg(feature_extraction_capnp.NgramVectorizer, filename))
    elif TfidfTransformer == typ:
        return _capnp_to_tfidf_transformer(_load_msg(feature_extraction_capnp.TfidfTransformer, filename))
    elif LogisticRegression == typ:
        return _capnp_to_logisticreg(_load_msg(classification_capnp.LogisticRegression, filename))
    else:
        raise Exception('Cannot deserialize type: %s' % str(typ))


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

