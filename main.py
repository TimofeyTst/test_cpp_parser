import sys
from CPPFunctionLexer import CPPFunctionLexer
from CPPFunctionParser import CPPFunctionParser
from CPPFunctionErrorListener import CPPFunctionErrorListener
from antlr4 import *

def main(argv):
    # Открываем файл и читаем все строки
    with open(argv[1], 'r') as file:
        lines = file.readlines()

    # Проверяем каждую строку на корректность
    for line in lines:
        input_stream = InputStream(line)
        lexer = CPPFunctionLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CPPFunctionParser(stream)

        # Создаем экземпляр класса CPPFunctionErrorListener
        error_listener = CPPFunctionErrorListener()

        # Устанавливаем этот экземпляр в качестве слушателя ошибок парсера
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        # Парсим функцию
        tree = parser.function()

        # Если была ошибка парсинга, выводим сообщение об ошибке
        if error_listener.has_error:
            print(f"Error parsing function: {line}")
        else:
            print(f"Function {line} parsed successfully")

if __name__ == '__main__':
    main(sys.argv)
