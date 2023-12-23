#! /usr/bin/env python
# coding=utf-8
import ply.yacc as yacc
from calclex import tokens

# rules for species
def p_splist_sp(p):
    'splist : splist sp'
    for sym,cnt in p[2].items():
        if sym not in p[1]:
            p[1][sym]=cnt
        else:
            p[1][sym]+=cnt
    p[0]=p[1]

def p_splist_to_sp(p):
    'splist : sp'
    p[0] = p[1]

def p_sp_symbol(p):
    'sp : SYMBOL'
    p[0] = {}
    p[0][p[1]] = 1

def p_sp_symbol_count(p):
    'sp : SYMBOL NUMBER'
    p[0] = {}
    p[0][p[1]] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

test=["He","H2","H2SO4","CH3COOH","NaCl","C60H60"]
for i in test:
   res=parser.parse(i)
   print(i)
   for a in res:
       print(a,res[a])