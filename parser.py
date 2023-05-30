from rply import ParserGenerator
from ast import Sum, Sub, Mult, Div, Number, Write, Equal

symbol_table = {}
class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'WRITE', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'PROGRAM', 'DIV', 'MULT',
             'LETTER', 'MAIN', 'OPEN_BRACKET', 'CLOSE_BRACKET', 'EQUAL', 'VAR']
        )

        precedence = [
            ('left', ['SUM', 'SUB']),
            ('left', ['MULT', 'DIV'])
        ]

        """
            ['NUMBER', 'WRITE', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'PROGRAM', 'BEGIN',
             'END', 'IF', 'ELSE', 'FOR', 'THEN', 'DO', 'WHILE',
             'INT', 'FLOAT', 'STRING',
             'COLON', 'PERIOD', 'COMMA', 'DIV', 'MULT', 'GREATER', 'LESS']
            """

    def parse(self):
        # @self.pg.production('program: PROGRAM OPEN_BRACKET assign block CLOSE_BRACKET')
        @self.pg.production('program : PROGRAM MAIN OPEN_BRACKET WRITE OPEN_PAREN statement CLOSE_PAREN SEMI_COLON CLOSE_BRACKET')
        @self.pg.production('program : PROGRAM MAIN OPEN_BRACKET statement SEMI_COLON CLOSE_BRACKET')
        def program(p):
            if p[3].gettokentype() == 'WRITE':
                return Write(p[5])
            else:
                return

        @self.pg.production('statement : expression')
        @self.pg.production('statement : VAR LETTER EQUAL NUMBER')
        def statement(p):
            var_name = p[0].getstr()
            var_value = p[3]
            locals()[var_name] = var_value
            print(var_value)
            return var_value

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MULT expression')
        @self.pg.production('expression : expression DIV expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MULT':
                return Mult(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)



        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.production('expression : LETTER')
        def variable(p):
            var_name = p[0].getstr()
            return locals().get(var_name)



        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
