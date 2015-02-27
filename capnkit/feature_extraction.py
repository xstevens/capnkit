import numpy as np
import scipy as sp

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

import capnp
import feature_extraction_capnp

def _capnp_to_count_vectorizer(vmsg): 
    v = CountVectorizer()
    v.token_pattern = vmsg.tokenPattern
    v.ngram_range = (vmsg.ngramRange.min, vmsg.ngramRange.max)
    v.vocabulary_ = {w: i for i, w in enumerate(vmsg.vocabulary)}
    v.stop_words_ = {w for w in vmsg.stopWords}
    return v

    
def _count_vectorizer_to_capnp(v):
    ngram_range = feature_extraction_capnp.NgramRange.new_message(
        min=v.ngram_range[0], 
        max=v.ngram_range[1]
    )
    vmsg = feature_extraction_capnp.NgramVectorizer.new_message(
        ngramRange=ngram_range,
        tokenPattern=v.token_pattern
    )
    
    vocab = vmsg.init('vocabulary', len(v.vocabulary_))
    for feature, i in v.vocabulary_.iteritems():
        vocab[i] = feature
    
    stop_words = vmsg.init('stopWords', len(v.stop_words_))
    for i, w in enumerate(v.stop_words_):
        stop_words[i] = w    
    return vmsg
    

def _capnp_to_tfidf_transformer(tmsg):
    t = TfidfTransformer()
    t._idf_diag = sp.sparse.dia_matrix(np.diag(np.array(tmsg.idf)))
    return t

    
def _tfidf_transformer_to_capnp(t):
    tmsg = feature_extraction_capnp.TfidfTransformer.new_message()
    idf = tmsg.init('idf', len(t.idf_))
    for i, freq in enumerate(t.idf_.tolist()):
        idf[i] = freq
    return tmsg