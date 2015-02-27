""" Capn'Kit is a set of tools to persist scikit-learn classes using 
Cap'n Proto serialization library. 

This allows using trained feature extractors and models from 
scikit-learn in other languages. As an added bonus it also side steps 
known security issues with pickle.

The goal of this project is to provide the minimum viable set of 
persistance and to be relatively efficient in doing so.
"""
__version__ = '0.0.1'

from .util import load
from .util import dump
