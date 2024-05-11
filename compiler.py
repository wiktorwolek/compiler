import sys
from antlr4 import *

from ExprLexer import ExprLexer
from ExprParser import ExprParser
from LLVMActions import LLVMActions


def main(args):
    print(":(")
    # Step 1: Load input source into the stream object
    stream = FileStream(args[1])

    # Step 2: Create an instance of AssignmentStLexer
    lexer = ExprLexer(stream)

    # Step 3: Convert the input source into a list of tokens
    tokens = CommonTokenStream(lexer)

    # Step 4: Create an instance of the AssignmentStParser
    parser = ExprParser(tokens)

    # Step 5: Create parse tree
    tree = parser.prog()


    # Step 7: Create a walker to traverse the parse tree and callback our listener
    walker = ParseTreeWalker()
    walker.walk(LLVMActions(), tree)
if __name__ == '__main__':
    main(sys.argv)