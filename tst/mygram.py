import sys
from antlr4 import *
from ExprLexer import MyGrammarLexer
from ExprParser import MyGrammarParser
 
def main(argv):
    input = FileStream(argv[1])
    lexer = MyGrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = MyGrammarParser(stream)
    tree = parser.startRule()
 
if __name__ == '__main__':
    main(sys.argv)