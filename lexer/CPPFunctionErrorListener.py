from antlr4.error.ErrorListener import ErrorListener

class CPPFunctionErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.has_error = False

    # def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # print(f"\033[93mline {line}:{column} {msg}\033[0m")
        # self.has_error = True

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_error = True
        self.errors.append(f"line {line}:{column} {msg}")

    def printErrors(self):
        for error in self.errors:
            print(f"\033[93mError: {error}\033[0m")


    def addError(self, error_message):
        self.errors.append(error_message)
