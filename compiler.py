import sys
from antlr4 import *

from ExprLexer import ExprLexer
from ExprParser import ExprParser
from LLVMActions import LLVMActions
from LLVMGenerator import LLVMGenerator

def main(args):

    if len(args) > 1:

        stream = FileStream(args[1])


        lexer = ExprLexer(stream)


        tokens = CommonTokenStream(lexer)


        parser = ExprParser(tokens)

    # Step 5: Create parse tree
    tree = parser.prog()
    # print(tree.toStringTree(recog=parser))
    walker = ParseTreeWalker()
    try:
        walker.walk(LLVMActions(), tree)
    except:
        #  print(LLVMGenerator().generate())
        #  print(LLVMGenerator.buffer)
         print("Compilation finished with errors")
if __name__ == '__main__':
    main(sys.argv)