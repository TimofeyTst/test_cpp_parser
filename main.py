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

        # Если была ошибка парсинга, выводим сообщение об ошибке красным цветом
        if error_listener.has_error:
            print(f"\033[91mError parsing function: '{line.strip()}'\033[0m")
        else:
            # Если парсинг прошел успешно, выводим сообщение о успешном парсинге зеленым цветом
            print(f"\033[92mFunction '{line.strip()}' parsed successfully\033[0m")
        
        print()

if __name__ == '__main__':
    main(sys.argv)
