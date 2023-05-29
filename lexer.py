from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):

        # Reserved
        self.lexer.add('PROGRAM', r'program')
        self.lexer.add('MAIN', r'main')
        self.lexer.add('BEGIN', r'begin')
        self.lexer.add('END', r'end')
        self.lexer.add('VAR', r'var')
        self.lexer.add('WRITE', r'write')
        self.lexer.add('IF', r'if')
        self.lexer.add('ELSE', r'else')
        self.lexer.add('FOR', r'for')
        self.lexer.add('THEN', r'then')
        self.lexer.add('DO', r'do')
        self.lexer.add('WHILE', r'while')

        #Types
        self.lexer.add('INT', r'int')
        self.lexer.add('FLOAT', r'float')
        self.lexer.add('STRING', r'string')

        # Print
        #self.lexer.add('PRINT', r'print')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        self.lexer.add('OPEN_BRACKET', r'\{')
        self.lexer.add('CLOSE_BRACKET', r'\}')

        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        self.lexer.add('COLON', r'\:')
        self.lexer.add('PERIOD', r'\.')
        self.lexer.add('COMMA', r'\,')


        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')

        self.lexer.add('DIV', r'\/')
        self.lexer.add('MULT', r'\*')
        self.lexer.add('GREATER', r'\>')
        self.lexer.add('LESS', r'\<')

        self.lexer.add('LETTER', r'[a-zA-Z_]+')

        # Number
        self.lexer.add('NUMBER', r'\d+')

        self.lexer.add('EQUAL', r'\=')

        # Ignore spaces
        self.lexer.ignore('\s+')



    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()