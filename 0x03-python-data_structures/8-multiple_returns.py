#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        len_sent = len(sentence)
    else:
        len_sent = 0
    return (len_sent, sentence if not sentence else sentence[:1])
