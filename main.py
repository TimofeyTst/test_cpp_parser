import sys
from CPPFunctionLexer import CPPFunctionLexer
from CPPFunctionParser import CPPFunctionParser
from antlr4 import *

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CPPFunctionLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CPPFunctionParser(stream)
    tree = parser.function()

    print("Function parsed successfully")

if __name__ == '__main__':
    main(sys.argv)