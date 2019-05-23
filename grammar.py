# -*- coding: utf-8 -*-
"""
Created on Sun May 19 19:35:08 2019

@author: Jeff Lai
"""

import nltk
#nltk.download('treebank')
from nltk.corpus import treebank
from nltk.grammar import PCFG
from nltk.grammar import Nonterminal
from nltk.grammar import induce_pcfg
from nltk.grammar import Production

treebank_productions = set()
for sent in treebank.parsed_sents():
    for production in sent.productions():
        treebank_productions.add(production)

def remove_dash(strr):
    if len(strr.split('-'))>1:
        result = strr.split('-')[0]
    else:
        result = strr
    if result == 'NNS':
        result = 'NN'
    if result == 'NNPS':
        result = 'NNP'
    if result == 'JJR' or result == 'JJS':
        result = 'JJ'
    return result

productions = list(treebank_productions)
output = set()
for p in productions:
    p = str(p)
    if 'NONE' in p or "'" in p or "'" in p or ":" in p or "," in p or "PDT" in p or "FW" in p:
        continue
    lhs = remove_dash(p.split()[0])
    rhs = []
    for strr in p.split()[2:]:
        rhs.append(remove_dash(strr))
    
    temp_rhs = rhs[:]
    if len(temp_rhs) == 1:
        output.add(Production(Nonterminal(lhs),[Nonterminal(rhs[0])]))
    else:
        rhs_head = "-".join(temp_rhs[1:])
        output.add(Production(Nonterminal(lhs),[Nonterminal(temp_rhs[0]),Nonterminal(rhs_head)]))
        lhs = rhs_head
        temp_rhs = temp_rhs[1:]

grammar = induce_pcfg(Nonterminal('S'),list(output))

print('ROOT -> S 1')
for g in grammar.productions():
    temp = str(g).split('[')
    print(temp[0],temp[1].strip(']'))
            