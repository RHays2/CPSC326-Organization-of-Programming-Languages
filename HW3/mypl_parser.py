import mypl_error as error
import mypl_lexer as lexer
import mypl_token as token

class Parser(object):

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None

    def parse(self):
        """succeeds if program is syntactically well-formed"""
        self.__advance()
        self.__stmts()
        self.__eat(token.EOS, 'expecting end of file')

    def __advance(self):
        self.current_token = self.lexer.next_token()

    def __eat(self, tokentype, error_msg):
        if self.current_token.tokentype == tokentype:
            self.__advance()
        else:
            self.__error(error_msg)

    def __error(self, error_msg):
        s = error_msg + ', found "' + self.current_token.lexeme + '" in parser'
        l = self.current_token.line
        c = self.current_token.column
        raise error.MyPLError(error_msg, l, c)

    # Beginning of recursive descent functions

    def __stmts(self):
        """<stmts> ::= <stmt> <stmts> | e"""
        if self.current_token.tokentype != token.EOS:
            self.__stmt()
            self.__stmts()

    def __bstmts(self):
        """<bstms ::= <bstmt> <bstmts> | e"""
        if self.current_token.tokentype != token.EOS:
            self.__bstmt()
            self.__bstmts()

    def __stmt(self):
        """<stmt> ::= <sdecl> | <fdecl> | <bstmt>"""
        if self.current_token.tokentype == token.STRUCTTYPE:
            self.__sdecl()
        elif self.current_token.tokentype == token.FUN:
            self.__fdecl()
        else:
            self.__bstmt()

    def __bstmt(self):
        """<bstmt> ::= <vdecl> | <assign> | <cond> | <while> | <expr> SEMICOLON | <exit> """

    def __sdecl(self):
        """<sdecl> ::= STRUCT ID <vdecls> END"""

    def __vdecls(self):
        """<vdecls> ::= <vdecl> <vdecls> | e"""

    def __fdecl(self):
        """<fdecl> ::= FUN (<type> | NIL) ID LPAREN <params> RPAREN <bstmts> END"""

    def __params(self):
        """<params> ::= ID COLON <type> (COMMA ID COLON <type> )∗ | e"""

    def __type(self):
        """<type> ::= ID | INTTYPE | FLOATTYPE | BOOLTYPE | STRINGTYPE"""

    def __exit(self):
        """<exit> ::= RETURN( <expr> | e ) SEMICOLON"""

    def __vdecl(self):
        """<vdecl> ::= VAR ID <tdecl> ASSIGN <expr> SEMICOLON"""

    def __tdecl(self):
        """<tdecl> ::= COLON <type> | e"""

    def __assign(self):
        """<assign> ::= SET <lvalue> ASSIGN <expr> SEMICOLON"""

    def __lvalue(self):
        """<lvalue> ::= ID( DOT ID )∗"""

    def __cond(self):
        """<cond> ::= IF <bexpr> THEN <bstmts> <condt> END"""

    def __condt(self):
        """<condt> ::= ELIF <bexpr> THEN <bstmts> <condt> | ELSE <bstmts> | e"""

    def __while(self):
        """<while> ::= WHILE <bexpr> DO <bstmts> END """

    def __expr(self):
        """<expr> ::= ( <rvalue> | LPAREN <expr> RPAREN )( <mathrel> <expr> | e )"""

    def __mathrel(self):
        """<mathrel> ::= PLUS | MINUS | DIVIDE | MULTIPLY | MODULO"""

    def __rvalue(self):
        """<rvalue> ::= STRINGVAL | INTVAL | BOOLVAL | FLOATVAL | NIL | NEW ID | hidrvali"""

    def __idrval(self):
        """<idrval> ::= ID ( DOT ID )∗ | ID LPAREN <exprlist> RPAREN"""

    def __exprlist(self):
        """<exprlist> ::= <expr> ( COMMA <expr> )∗ | e"""

    def __bexpr(self):
        """<bexpr> ::= <expr> <bexprt> | NOT <bexpr> <bexprt> | LPAREN <bexpr> RPAREN <bconnct>"""

    def __bexprt(self):
        """<bexprt> ::= <boolrel> <expr> <bconnct> | <bconnct>"""

    def __bconnct(self):
        """<bconnct> ::= AND <bexpr> | OR <bexpr> | e"""

    def __boolrel(self):
        """<boolrel> ::= EQUAL | LESS_THAN | GREATER_THAN | LESS_THAN_EQUAL |
                      GREATER_THAN_EQUAL | NOT_EQUAL"""
