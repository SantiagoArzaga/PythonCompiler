from rply import ParserGenerator
#from ast import Sum, Sub, Mult, Div, Number, Write, Equal
from ast import AbstractSyntaxTree as astfunc

data = []


class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'WRITE', 'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON', 'SUM', 'SUB', 'PROGRAM', 'DIV', 'MULT',
             'LETTER', 'MAIN', 'OPEN_BRACKET', 'CLOSE_BRACKET', 'EQUAL', 'VAR', 'COMMA', 'COLON',
             'BEGIN', 'END', 'IF', 'ELSE', 'FOR', 'THEN', 'DO', 'WHILE', 'GREATER', 'LESS', 'INT', 'FLOAT', 'STRING',
             'EMPTY', 'QUOTE', 'STRING']
        )

        precedence = [
            ('left', ['SUM', 'SUB']),
            ('left', ['MULT', 'DIV'])
        ]

    def parse(self):
        @self.pg.production('program : PROGRAM MAIN OPEN_BRACKET variable_declaration block CLOSE_BRACKET')
        def program(p):
            astfunc.program_end(astfunc)
            return p[5]

        @self.pg.production('variable_declaration : VAR assignment COLON type SEMI_COLON')
        def variable_declaration(p):
            return astfunc.variable_declaration(astfunc, p[3])
            #for row in data:
            #    row['Type'] = p[3]
            #return

        @self.pg.production('assignment : store_id COMMA assignment')
        @self.pg.production('assignment : store_id')
        @self.pg.production('assignment : EMPTY')
        def assignment(p):
            return

        @self.pg.production('store_id : LETTER')
        def store_id(p):
            var_name = p[0].getstr()
            astfunc.store_id(astfunc, var_name)
            #new_row = {'Variable': var_name, 'Type': None, 'Value': None}
            #data.append(new_row)
            return


        @self.pg.production('type : FLOAT')
        @self.pg.production('type : INT')
        @self.pg.production('type : STRING')
        def type(p):
            return p[0].getstr()

        @self.pg.production('block : BEGIN SEMI_COLON declaration END SEMI_COLON')
        def block(p):
            return p[2]

        # @self.pg.production('declaration : WHILE expression DO declaration')
        # @self.pg.production('declaration : FOR OPEN_PAREN LETTER equal expression SEMI_COLON'
        #                    ' expression SEMI_COLON expression CLOSE_PAREN DO declaration')
        # @self.pg.production('declaration : declaration2')
        @self.pg.production('declaration : variable_assignation')
        @self.pg.production('declaration : write_statement')
        @self.pg.production('declaration : if_statement')
        def declaration(p):
            return

        @self.pg.production('write_statement : WRITE OPEN_PAREN expression CLOSE_PAREN end_sentence')
        @self.pg.production('write_statement : WRITE OPEN_PAREN QUOTE expression QUOTE CLOSE_PAREN end_sentence')
        def write_statement(p):
            if len(p) == 5:
                return astfunc.write_instruction(astfunc, p[2].getstr(), "var")
            else:
                return astfunc.write_instruction(astfunc, p[3].getstr(), "string")

        
        @self.pg.production('variable_assignation : variable equal expression end_sentence')
        def variable_assignation(p):
            return astfunc.variable_assignation(astfunc, p[0].getstr(), p[2])

        @self.pg.production('if_statement : IF expression THEN declaration')
        def if_statement(p):
            #return astfunc.sub(p[1])
            return

        @self.pg.production('end_sentence : SEMI_COLON')
        @self.pg.production('end_sentence : SEMI_COLON declaration')
        def end_sentence(p):
            return p[0]

        @self.pg.production('expression : simple GREATER simple')
        @self.pg.production('expression : simple LESS simple')
        @self.pg.production('expression : simple equality simple')
        @self.pg.production('expression : expression expression')
        @self.pg.production('expression : simple')
        def expression(p):
            if len(p) > 1:
                left = p[0]
                right = p[2]
                operator = p[1]
                if operator.gettokentype() == 'GREATER':
                    return astfunc.Greater(astfunc, left, right)
                elif operator.gettokentype() == 'LESS':
                    return astfunc.Less(astfunc,left, right)
            else:
                return p[0]

        @self.pg.production('simple : term SUM term')
        @self.pg.production('simple : term SUB term')
        @self.pg.production('simple : term')
        def simple(p):
            if len(p) > 1:
                left = p[0]
                right = p[2]
                operator = p[1]
                if operator.gettokentype() == 'SUM':
                    return astfunc.Sum(astfunc,left, right)
                elif operator.gettokentype() == 'SUB':
                    return astfunc.Sub(astfunc,left, right)
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
                    return astfunc.Mult(astfunc,left, right)
                elif operator.gettokentype() == 'DIV':
                    return astfunc.Div(astfunc,left, right)
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

        @self.pg.production('factor : string')
        @self.pg.production('string : LETTER string')
        @self.pg.production('string : LETTER')
        def stringvariable(p):
            return

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
