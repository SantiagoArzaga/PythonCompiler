from rply import ParserGenerator
from ast import Sum, Sub, Mult, Div, Number, Write, Equal

symbol_table = {}


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'WRITE', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'PROGRAM', 'DIV', 'MULT',
             'LETTER', 'MAIN', 'OPEN_BRACKET', 'CLOSE_BRACKET', 'EQUAL', 'VAR', 'COMMA', 'COLON',
             'BEGIN', 'END', 'IF', 'ELSE', 'FOR', 'THEN', 'DO', 'WHILE', 'GREATER', 'LESS', 'INT', 'FLOAT', 'STRING', 'EMPTY']
        )

        precedence = [
            ('left', ['SUM', 'SUB']),
            ('left', ['MULT', 'DIV'])
        ]

        """
            [ 'PERIOD']
             
                     #   def assignment(p):
        #        var_name = p[0].getstr()
        #         var_value = p[3]
        #          locals()[var_name] = var_value
        #           print(var_value)
        #            return var_value
        #@self.pg.production('assignment : expression')
        #@self.pg.production('statement : expression')
            """

    def parse(self):
        # @self.pg.production('program: PROGRAM OPEN_BRACKET assign block CLOSE_BRACKET')
        @self.pg.production('program : PROGRAM MAIN OPEN_BRACKET assignment block CLOSE_BRACKET')
        # @self.pg.production('program : PROGRAM MAIN OPEN_BRACKET statement SEMI_COLON CLOSE_BRACKET')
        def program(p):
            return

        @self.pg.production('assignment : VAR LETTER assignment2')
        def assignment(p):
            return

        @self.pg.production('assignment2 : COMMA LETTER assignment2')
        @self.pg.production('assignment2 : COLON INT SEMI_COLON')
        @self.pg.production('assignment2 : COLON FLOAT SEMI_COLON')
        @self.pg.production('assignment2 : COLON STRING SEMI_COLON')
        def assignment2(p):
            return

        @self.pg.production('block : BEGIN declaration END SEMI_COLON')
        def block(p):
            return

        @self.pg.production('declaration : variable equalsign expression')
        @self.pg.production('declaration : IF expression THEN declaration declaration2')
        @self.pg.production('declaration : WHILE expression DO declaration')
        @self.pg.production('declaration : FOR OPEN_PAREN LETTER equalsign expression SEMI_COLON'
                            ' expression SEMI_COLON expression CLOSE_PAREN DO declaration')
        @self.pg.production('declaration : declaration2')
        @self.pg.production('declaration : WRITE OPEN_PAREN expression CLOSE_PAREN')
        def declaration(p):
            return

        @self.pg.production('declaration2 : EMPTY')
        @self.pg.production('declaration2 : ELSE declaration')
        @self.pg.production('declaration2 : declaration')

        def declaration2(p):
            return

        @self.pg.production('expression : simple GREATER simple')
        @self.pg.production('expression : simple LESS simple')
        @self.pg.production('expression : simple equality simple')
        @self.pg.production('expression : simple')
        def expression(p):
            return

        @self.pg.production('simple : term SUM term')
        @self.pg.production('simple : term SUB term')
        @self.pg.production('simple : term')
        def simple(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)

        @self.pg.production('term : factor MULT factor')
        @self.pg.production('term : factor DIV factor')
        @self.pg.production('term : factor')
        def term(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'MULT':
                return Mult(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)

        @self.pg.production('factor : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.production('variable : LETTER')
        @self.pg.production('factor : LETTER')
        def variable(p):
            var_name = p[0].getstr()
            return locals().get(var_name)

        @self.pg.production('equalsign : COLON EQUAL')
        def equalsign(p):
            return

        @self.pg.production('equality : EQUAL')
        def equality(p):
            return

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
