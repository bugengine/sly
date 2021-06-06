# -----------------------------------------------------------------------------
# calc.py
# -----------------------------------------------------------------------------

import sys
sys.path.insert(0, '../..')

from sly import Lexer, Parser

class AABCLexer(Lexer):
    tokens = { A, B, C }

    # Tokens
    A = r'a'
    B = r'b'
    C = r'c'

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

class AABCParser(Parser):
    tokens = AABCLexer.tokens
    debugfile = 'aabc.out'

    #precedence = (
    #    ('left', ELSE),
    #    )

    def __init__(self):
        pass

    @_('prog a')
    @_('a')
    def prog(self, p):
        pass

    @_('A b C')
    @_('A A b C')
    def a(self, p):
        pass

    @_('A B')
    @_('B')
    def b(self, p):
        pass

if __name__ == '__main__':
    lexer = AABCLexer()
    parser = AABCParser()
    parser.parse(lexer.tokenize("aabc"))
