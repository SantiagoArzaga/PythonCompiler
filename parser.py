from rply import ParserGenerator
from ast import Sum, Sub, Write, Mult, Div, Letter, Number, Equal


class Parser():
    def __init__(self, module, builder, write):  # -------
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'WRITE', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'PROGRAM', 'DIV', 'MULT',
              'MAIN', 'OPEN_BRACKET', 'CLOSE_BRACKET','EQUAL']
        )

        precedence = [
            ('left', ['SUM', 'SUB']),
            ('left', ['MULT', 'DIV'])
        ]

        self.module = module  # -------
        self.builder = builder  # -------
        self.write = write  # -------

        """
            ['LETTER', 'NUMBER', 'WRITE', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'PROGRAM', 'BEGIN',
             'END', 'VAR', 'IF', 'ELSE', 'FOR', 'THEN', 'DO', 'WHILE',
             'INT', 'FLOAT', 'STRING',
             'COLON', 'PERIOD', 'COMMA', 'DIV', 'MULT', 'GREATER', 'LESS']
            """

    def parse(self):
        # @self.pg.production('program: PROGRAM OPEN_BRACKET assign block CLOSE_BRACKET')
        @self.pg.production(
            'program : PROGRAM MAIN OPEN_BRACKET WRITE OPEN_PAREN expression CLOSE_PAREN SEMI_COLON CLOSE_BRACKET')
        def program(p):
            return Write(self.builder, self.module, self.write, p[5])  # --------

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MULT expression')
        @self.pg.production('expression : expression DIV expression')
        @self.pg.production('expression : expression EQUAL expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(self.builder, self.module, left, right)  # --------
            elif operator.gettokentype() == 'SUB':
                return Sub(self.builder, self.module, left, right)  # --------
            elif operator.gettokentype() == 'MULT':
                return Mult(self.builder, self.module, left, right)  # --------
            elif operator.gettokentype() == 'DIV':
                return Div(self.builder, self.module, left, right)  # --------
            elif operator.gettokentype() == 'EQUAL':
                return Equal(self.builder, self.module, left, right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(self.builder, self.module, p[0].value)  # --------


        # @self.pg.production('block: BEGIN END SEMI_COLON')
        # def block(p):
        #    declaration = p[1]
        #    return declaration

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
