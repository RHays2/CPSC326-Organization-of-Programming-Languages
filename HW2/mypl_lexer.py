import mypl_token as token
import mypl_error as error

class Lexer(object):
    def __init__(self, input_stream):
        self.line = 1
        self.column = 0
        self.input_stream = input_stream
    def __peek(self):
        pos = self.input_stream.tell()
        symbol = self.input_stream.read(1)
        self.input_stream.seek(pos)
        return symbol
    def __read(self):
        return self.input_stream.read(1)
    def next_token(self):
        #... define next token here ...
        self.column += 1
        currentSymbol = ''
        reserved = False

        #Check for Newlines
        if (self.__peek() == '\n'):
            self.__read()
            self.line += 1
            self.column = 0
            return self.next_token()

        #read in symbol
        symbol = self.__read()

        #check for end of file
        if (self.__peek() == ''):
            return token.Token(token.EOS, '',  self.line, self.column)

        #check for spaces
        if symbol.isspace():
            #self.column += 1
            return self.next_token()

        #check for comments
        if (symbol == '#'):
            while(self.__peek() != '\n'):
                self.__read()
            self.__read()
            self.line += 1
            self.column = 0
            return self.next_token()

        #ASSIGN
        if (symbol == '=' and self.__peek() != '='):
            currentSymbol = '='
            return token.Token(token.ASSIGN, currentSymbol, self.line, self.column)
        #EQUAL
        if (symbol == '=' and self.__peek() == '='):
            currentSymbol = '=='
            symbol = self.next_token()
            return token.Token(token.EQUAL, currentSymbol, self.line, self.column - 1)
        #COLON
        if (symbol == ':'):
            return token.Token(token.COLON, symbol, self.line, self.column)
        #COMMA
        if (symbol == ','):
            return token.Token(token.COMMA, symbol, self.line, self.column)
        #DIVIDE
        if (symbol == '/'):
            return token.Token(token.DIVIDE, symbol, self.line, self.column)
        #DOT
        if (symbol == '.'):
            return token.Token(token.DOT, symbol, self.line, self.column)
        #GREATER THAN
        if (symbol == '>' and self.__peek() != '='):
            currentSymbol = '>'
            return token.Token(token.GREATER_THAN, currentSymbol, self.line, self.column)
        #GREATER THAN EQUAL
        if (symbol == '>' and self.__peek() == '='):
            symbol = self.next_token()
            currentSymbol = '>='
            return token.Token(token.GREATER_THAN_EQUAL, currentSymbol, self.line, self.column - 1)
        #LESS THAN
        if (symbol == '<' and self.__peek() != '='):
            currentSymbol = '<'
            #self.column += 1
            return token.Token(token.LESS_THAN, currentSymbol, self.line, self.column)
        #LESS THAN EQUAL
        if (symbol == '<' and self.__peek() == '='):
            symbol = self.next_token()
            currentSymbol = '<='
            return token.Token(token.LESS_THAN_EQUAL, currentSymbol, self.line, self.column - 1)
        #NOT EQUAL
        if (symbol == '!' and self.__peek() == '='):
            symbol = self.next_token()
            currentSymbol = '!='
            return token.Token(token.NOT_EQUAL, currentSymbol, self.line, self.column)

        #LPAREN
        if (symbol =='('):
            return token.Token(token.LPAREN, symbol, self.line, self.column)
        #RPAREN
        if (symbol ==')'):
            return token.Token(token.RPAREN, symbol, self.line, self.column)
        #MINUS
        if (symbol =='-'):
            return token.Token(token.MINUS, symbol, self.line, self.column)
        #MODULO
        if (symbol =='%'):
            return token.Token(token.MODULO, symbol, self.line, self.column)
        #MULTIPLY
        if (symbol =='*'):
            return token.Token(token.MULTIPLY, symbol, self.line, self.column)
        #PLUS
        if (symbol =='+'):
            return token.Token(token.PLUS, symbol, self.line, self.column)
        #SEMICOLON
        if (symbol ==';'):
            return token.Token(token.SEMICOLON, symbol, self.line, self.column)

        if (symbol.isalpha()):
            reserved = False
            currentSymbol += symbol
            startPosition = self.column

            if (self.__peek() in ('=,:/><()*+;-!')):
                reserved = True

            while(not(self.__peek().isspace() or reserved)):
                symbol = self.__read()
                currentSymbol += symbol
                self.column += 1

            #bool type
            if (currentSymbol == 'bool'):
                return token.Token(token.BOOLTYPE, currentSymbol, self.line, startPosition)

            #int type
            elif (currentSymbol == 'int'):
                return token.Token(token.INTTYPE, currentSymbol, self.line, startPosition)

            #float type
            elif (currentSymbol == 'float'):
                return token.Token(token.FLOATTYPE, currentSymbol, self.line, startPosition)

            #struct type
            elif (currentSymbol == 'struct'):
                return token.Token(token.STRUCTTYPE, currentSymbol, self.line, startPosition)

            #and type
            elif (currentSymbol == 'and'):
                return token.Token(token.AND, currentSymbol, self.line, startPosition)

            #or type
            elif (currentSymbol == 'or'):
                return token.Token(token.OR, currentSymbol, self.line, startPosition)

            #not type
            elif (currentSymbol == 'not'):
                return token.Token(token.NOT, currentSymbol, self.line, startPosition)

            #while type
            elif (currentSymbol == 'while'):
                return token.Token(token.WHILE, currentSymbol, self.line, startPosition)

            #do type
            elif (currentSymbol == 'do'):
                return token.Token(token.DO, currentSymbol, self.line, startPosition)

            #if type
            elif (currentSymbol == 'if'):
                return token.Token(token.IF, currentSymbol, self.line, startPosition)

            #then type
            elif (currentSymbol == 'then'):
                return token.Token(token.THEN, currentSymbol, self.line, startPosition)

            #else type
            elif (currentSymbol == 'else'):
                return token.Token(token.ELSE, currentSymbol, self.line, startPosition)

            #elif type
            elif (currentSymbol == 'elif'):
                return token.Token(token.ELIF, currentSymbol, self.line, startPosition)

            #end type
            elif (currentSymbol == 'end'):
                return token.Token(token.END, currentSymbol, self.line, startPosition)

            #fun type
            elif (currentSymbol == 'fun'):
                return token.Token(token.FUN, currentSymbol, self.line, startPosition)

            #var type
            elif (currentSymbol == 'var'):
                return token.Token(token.VAR, currentSymbol, self.line, startPosition)

            #set type
            elif (currentSymbol == 'set'):
                return token.Token(token.SET, currentSymbol, self.line, startPosition)

            #return type
            elif (currentSymbol == 'return'):
                return token.Token(token.RETURN, currentSymbol, self.line, startPosition)

            #new type
            elif (currentSymbol == 'new'):
                return token.Token(token.NEW, currentSymbol, self.line, startPosition)

            #nil type
            elif (currentSymbol == 'nil'):
                return token.Token(token.NIL, currentSymbol, self.line, startPosition)

            #true
            elif (currentSymbol == 'true'):
                return token.Token(token.BOOLVAL, currentSymbol, self.line, startPosition)

            #false
            elif (currentSymbol == 'false'):
                return token.Token(token.BOOLVAL, currentSymbol, self.line, startPosition)

            #identifier
            else:
                return token.Token(token.ID, currentSymbol, self.line, startPosition)

        if (symbol.isdigit()):
            reserved = False
            isFloat = 0
            currentSymbol += str(symbol)
            startPosition = self.column

            if (self.__peek() in ('=,:/><()*+;-!')):
                reserved = True

            while(not(self.__peek().isspace() or reserved)):
                if (self.__peek().isdigit()):
                    symbol = str(self.__read())
                    currentSymbol += symbol
                    self.column += 1

                if (self.__peek() == '.'):
                    symbol = self.__read()
                    currentSymbol += symbol
                    self.column += 1
                    isFloat = 1

            #integer value
            if (isFloat == 0):
                return token.Token(token.INTVAL, currentSymbol, self.line, startPosition)

            #float value
            if (isFloat == 1):
                return token.Token(token.FLOATVAL, currentSymbol, self.line, startPosition)

        #string values
        if (symbol == '"'):
            startPosition = self.column
            while(not(self.__peek() == '"')):
                currentSymbol += self.__read()
                self.column += 1
            self.__read()
            self.column += 1
            return token.Token(token.STRINGVAL, currentSymbol, self.line, startPosition)
        if (symbol == "'"):
            startPosition = self.column
            while(not(self.__peek() == "'")):
                currentSymbol += self.__read()
                self.column += 1
            self.__read()
            self.column += 1
            return token.Token(token.STRINGVAL, currentSymbol, self.line, startPosition)
