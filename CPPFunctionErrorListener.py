from antlr4.error.ErrorListener import ErrorListener

class CPPFunctionErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.has_error = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"line {line}:{column} {msg}")
        self.has_error = True
