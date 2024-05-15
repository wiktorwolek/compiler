import sys
from antlr4 import *

from ExprLexer import ExprLexer
from ExprParser import ExprParser
from LLVMActions import LLVMActions
from LLVMGenerator import LLVMGenerator

def main(args):

    if len(args) > 1:
        print(args)
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
        print(tree.toStringTree(recog=parser))
        walker = ParseTreeWalker()
        try:
            walker.walk(LLVMActions(), tree)
        except:
            print(LLVMGenerator().generate())
            print(":(")

    else:
        print("Not enough arguments")


if __name__ == '__main__':
    main(sys.argv)