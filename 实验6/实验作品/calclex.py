# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'NUMBER',
   'SYMBOL'
)


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_SYMBOL(t):
    r"""
    C[laroudsemf]?|Os?|N[eaibdpos]?|S[icernbmg]?|P[drmtboau]?|
    H[eofgas]?|A[lrsgutcm]|B[eraik]?|Dy|E[urs]|F[erm]?|G[aed]|
    I[nr]?|Kr?|L[iaur]|M[gnodt]|R[buhenaf]|T[icebmalh]|
    U|V|W|Xe|Yb?|Z[nr]
    """

    return t;



# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print ("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

## Build the lexer
lexer = lex.lex()

# # Test it out
# data = "He3O2"
# # Give the lexer some input
# lexer.input(data)
# # Tokenize
# while True:
# 	tok = lexer.token()
# 	if not tok: break # No more input
# 	print (tok)
