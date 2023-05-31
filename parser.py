from rply import ParserGenerator
from ast import Sum, Sub, Mult, Div, Number, Write, Equal

data = []


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'WRITE', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'PROGRAM', 'DIV', 'MULT',
             'LETTER', 'MAIN', 'OPEN_BRACKET', 'CLOSE_BRACKET', 'EQUAL', 'VAR', 'COMMA', 'COLON',
             'BEGIN', 'END', 'IF', 'ELSE', 'FOR', 'THEN', 'DO', 'WHILE', 'GREATER', 'LESS', 'INT', 'FLOAT', 'STRING',
             'EMPTY']
        )

        precedence = [
            ('left', ['SUM', 'SUB']),
            ('left', ['MULT', 'DIV'])
        ]

    def parse(self):
        @self.pg.production('program : PROGRAM MAIN OPEN_BRACKET variable_declaration block CLOSE_BRACKET')
        def program(p):
            return p[5]

        @self.pg.production('variable_declaration : VAR assignment COLON type SEMI_COLON')
        def variable_declaration(p):
            for row in data:
                row['Type'] = p[3]
            return

        @self.pg.production('assignment : store_id COMMA assignment')
        @self.pg.production('assignment : store_id')
        @self.pg.production('assignment : EMPTY')
        def assignment(p):
            return

        @self.pg.production('store_id : LETTER')
        def store_id(p):
            var_name = p[0].getstr()
            new_row = {'Variable': var_name, 'Type': None, 'Value': None}
            data.append(new_row)
            return


        @self.pg.production('type : FLOAT')
        @self.pg.production('type : INT')
        @self.pg.production('type : STRING')
        def type(p):
            return p[0].getstr()

        @self.pg.production('block : BEGIN SEMI_COLON declaration END SEMI_COLON')
        def block(p):
            return p[2]

        # @self.pg.production('declaration : IF expression THEN declaration declaration2')
        # @self.pg.production('declaration : WHILE expression DO declaration')
        # @self.pg.production('declaration : FOR OPEN_PAREN LETTER equal expression SEMI_COLON'
        #                    ' expression SEMI_COLON expression CLOSE_PAREN DO declaration')
        # @self.pg.production('declaration : declaration2')
        @self.pg.production('declaration : variable_assignation')
        @self.pg.production('declaration : write_statement')
        def declaration(p):
            return

        @self.pg.production('write_statement : WRITE OPEN_PAREN expression CLOSE_PAREN end_sentence')
        def write_statement(p):
            for row in data:
                if p[2].getstr() in row.values():
                    print(row['Value'])
            return

        @self.pg.production('variable_assignation : variable equal expression end_sentence')
        def variable_assignation(p):
            for row in data:
                if row['Variable'] == p[0].getstr():
                    row['Value'] = p[2]
            for row in data:
                print(row)
            print("value that reaches declaration : ", p[2])
            return

        @self.pg.production('end_sentence : SEMI_COLON')
        @self.pg.production('end_sentence : SEMI_COLON declaration')
        def end_sentence(p):
            return p[0]

        @self.pg.production('expression : simple GREATER simple')
        @self.pg.production('expression : simple LESS simple')
        @self.pg.production('expression : simple equality simple')
        @self.pg.production('expression : simple')
        def expression(p):
            if len(p) == 1:
                return p[0]
            else:
                return

        @self.pg.production('simple : term SUM term')
        @self.pg.production('simple : term SUB term')
        @self.pg.production('simple : term')
        def simple(p):
            if len(p) > 1:
                left = p[0]
                right = p[2]
                operator = p[1]
                if operator.gettokentype() == 'SUM':
                    return Sum(left, right)
                elif operator.gettokentype() == 'SUB':
                    return Sub(left, right)
            else:
                return p[0]

        @self.pg.production('term : factor MULT factor')
        @self.pg.production('term : factor DIV factor')
        @self.pg.production('term : factor')
        def term(p):
            if len(p) > 1:
                left = p[0]
                right = p[2]
                operator = p[1]
                if operator.gettokentype() == 'MULT':
                    return Mult(left, right)
                elif operator.gettokentype() == 'DIV':
                    return Div(left, right)
            else:
                return p[0]

        @self.pg.production('factor : NUMBER')
        def number(p):
            return p[0].value

        @self.pg.production('variable : LETTER')
        @self.pg.production('factor : LETTER')
        def variable(p):
            var_name = p[0]
            return var_name

        @self.pg.production('equal : COLON EQUAL')
        def equal(p):
            return

        @self.pg.production('equality : EQUAL')
        def equality(p):
            return

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
