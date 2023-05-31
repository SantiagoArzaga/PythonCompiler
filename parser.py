from rply import ParserGenerator
from ast import Sum, Sub, Mult, Div, Number, Write, Equal

variable_table = {}
values_table = {}
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
        # @self.pg.production('program: PROGRAM OPEN_BRACKET assign block CLOSE_BRACKET')
        @self.pg.production('program : PROGRAM MAIN OPEN_BRACKET variabledeclaration block CLOSE_BRACKET')
        # @self.pg.production('program : PROGRAM MAIN OPEN_BRACKET statement SEMI_COLON CLOSE_BRACKET')
        def program(p):
            return p[5]

        @self.pg.production('variabledeclaration : VAR assignment COLON type SEMI_COLON')
        def variable_declaration(p):
            #variable_table[values_table][p[3]] = None
            #for var_name in values_table:
            #    values_table[var_name][p[3]] = None
            for row in data:
                row['Type'] = p[3]
            #print("values Table:", values_table)
            return

        @self.pg.production('assignment : LETTER COMMA assignment')
        @self.pg.production('assignment : LETTER')
        @self.pg.production('assignment : EMPTY')
        def assignment(p):
            if len(p) > 2:
                var_name = p[0].getstr()
                #values_table[var_name] = {}
                new_row = {'Variable': var_name, 'Type': None, 'Value': None}
                data.append(new_row)
            elif p[0].gettokentype() == 'LETTER':
                var_name = p[0].getstr()
                #values_table[var_name] = {}
                new_row = {'Variable': var_name, 'Type': None, 'Value': None}
                data.append(new_row)
            else:
                return

        @self.pg.production('type : FLOAT')
        @self.pg.production('type : INT')
        @self.pg.production('type : STRING')
        def type(p):
            return p[0].getstr()


        @self.pg.production('block : BEGIN SEMI_COLON declaration END SEMI_COLON')
        def block(p):
            return p[2]


        @self.pg.production('declaration : variable equal expression endsentence')
        def variable_assignation(p):
            #values_table[p[0].getstr()]["int"] = p[2]
            #data[p[0].getstr()]['Value'] = p[2]
            for row in data:
                if row['Variable'] == p[0].getstr():
                    row['Value'] = p[2]
            for row in data:
                print(row)
            print("value that reaches declaration : ", p[2])
            #print("variable that is assigned: ", values_table[p[0].getstr()])
            return
        #@self.pg.production('declaration : IF expression THEN declaration declaration2')
        #@self.pg.production('declaration : WHILE expression DO declaration')
        #@self.pg.production('declaration : FOR OPEN_PAREN LETTER equal expression SEMI_COLON'
        #                    ' expression SEMI_COLON expression CLOSE_PAREN DO declaration')
        #@self.pg.production('declaration : declaration2')
        @self.pg.production('declaration : WRITE OPEN_PAREN expression CLOSE_PAREN endsentence')
        def write_statement(p):
            for row in data:
                if p[2].getstr() in row.values():
                    print(row['Value'])
                else:
                    print("Variable not declared")
            #print(p[2].getstr())
            return #Write(p[2])

        @self.pg.production('endsentence : SEMI_COLON')
        @self.pg.production('endsentence : SEMI_COLON declaration')
        def end_sentence(p):
            return p[0]


        #@self.pg.production('declaration2 : EMPTY')
        #@self.pg.production('declaration2 : ELSE declaration')
        #@self.pg.production('declaration2 : declaration')
        #def declaration2(p):
        #    return

        @self.pg.production('expression : simple GREATER simple')
        @self.pg.production('expression : simple LESS simple')
        @self.pg.production('expression : simple equality simple')
        @self.pg.production('expression : simple')
        def expression(p):
            if len(p) == 1:
                #print("expression: ", p[0])
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
                #print("simple: ", p[0])
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
                #print("term: ", p[0])
                return p[0]

        @self.pg.production('factor : NUMBER')
        def number(p):
            #print("factor", p[0])
            return p[0].value

        @self.pg.production('variable : LETTER')
        @self.pg.production('factor : LETTER')
        def variable(p):
            var_name = p[0]
            #print("variable", var_name)
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
