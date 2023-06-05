from rply import Token

# data = []
# instructions = [{'Instruction': None, 'Value': None}]

variable_list = []

expression_quad = []
static_quad = []
quad = []
ignore_list = []
while_ignore_list = []


# 0 mult 3 4 12
# 1 sum r0 3 15
class AbstractSyntaxTree():
    def __init__(self, value):
        self.value = value


    def expression_instruction(self, value):
        new_row = {'Instruction': "expression", 'Op1': None, 'Op2': None, 'Result': value}
        expression_quad.append(new_row)
        # greater = int(left) > int(right)
        return len(quad) - 1

    def Greater(self, left, right):
        new_row = {'Instruction': "greater", 'Op1': left, 'Op2': right, 'Result': None}
        expression_quad.append(new_row)
        static_row = {'1': "greater", '2': left, '3': right, '4': None}
        static_quad.append(static_row)

        # greater = int(left) > int(right)
        return len(expression_quad) - 1

    def Less(self, left, right):
        new_row = {'Instruction': "less", 'Op1': left, 'Op2': right, 'Result': None}
        expression_quad.append(new_row)
        static_row = {'1': "less", '2': left, '3': right, '4': None}
        static_quad.append(static_row)
        return len(expression_quad) - 1

    def Equality(self, left, right):
        new_row = {'Instruction': "equality", 'Op1': left, 'Op2': right, 'Result': None}
        expression_quad.append(new_row)
        static_row = {'1': "equality", '2': left, '3': right, '4': None}
        static_quad.append(static_row)
        return len(expression_quad) - 1

    def Inequality(self, left, right):
        new_row = {'Instruction': "inequality", 'Op1': left, 'Op2': right, 'Result': None}
        expression_quad.append(new_row)
        static_row = {'1': "inequality", '2': left, '3': right, '4': None}
        static_quad.append(static_row)
        return len(expression_quad) - 1

    def GreaterEqual(self, left, right):
        new_row = {'Instruction': "greaterequal", 'Op1': left, 'Op2': right, 'Result': None}
        expression_quad.append(new_row)
        static_row = {'1': "greaterequal", '2': left, '3': right, '4': None}
        static_quad.append(static_row)
        return len(expression_quad) - 1

    def LessEqual(self, left, right):
        new_row = {'Instruction': "lessequal", 'Op1': left, 'Op2': right, 'Result': None}
        expression_quad.append(new_row)
        static_row = {'1': "lessequal", '2': left, '3': right, '4': None}
        static_quad.append(static_row)
        return len(expression_quad) - 1

    def Incremental(self, value):
        new_row = {'Instruction': "incremental", 'Op1': value, 'Op2': "0", 'Result': None}
        quad.append(new_row)
        # equality = left == right
        return len(expression_quad) - 1

    def Decremental(self, value):
        new_row = {'Instruction': "decremental", 'Op1': value, 'Op2': "0", 'Result': None}
        quad.append(new_row)
        # equality = left == right
        return len(expression_quad) - 1

    def Sum(self, left, right):
        new_row = {'Instruction': "sum", 'Op1': left, 'Op2': right, 'Result': None}
        expression_quad.append(new_row)
        static_row = {'1': "sum", '2': left, '3': right, '4': None}
        static_quad.append(static_row)
        return len(expression_quad) - 1

    def Sub(self, left, right):
        new_row = {'Instruction': "sub", 'Op1': left, 'Op2': right, 'Result': None}
        expression_quad.append(new_row)
        static_row = {'1': "sub", '2': left, '3': right, '4': None}
        static_quad.append(static_row)
        return len(expression_quad) - 1

    def Mult(self, left, right):
        new_row = {'Instruction': "mult", 'Op1': left, 'Op2': right, 'Result': None}
        expression_quad.append(new_row)
        static_row = {'1': "mult", '2': left, '3': right, '4': None}
        static_quad.append(static_row)
        return len(expression_quad) - 1

    def Div(self, left, right):
        new_row = {'Instruction': "div", 'Op1': left, 'Op2': right, 'Result': None}
        expression_quad.append(new_row)
        static_row = {'1': "div", '2': left, '3': right, '4': None}
        static_quad.append(static_row)
        return len(expression_quad) - 1

    def if_statement(self, begin, end, statement):
        new_row = {'Instruction': "if", 'Op1': begin, 'Op2': end, 'Result': statement}
        quad.append(new_row)
        return

    def else_statement(self, begin, end):
        new_row = {'Instruction': "else", 'Op1': begin, 'Op2': end, 'Result': len(quad) + 1}
        quad.append(new_row)
        return

    def while_statement(self, begin, end, statement):
        new_row = {'Instruction': "while", 'Op1': begin, 'Op2': end, 'Result': statement}
        quad.append(new_row)
        return

    def write_instruction(self, statement, type):
        if type == "string":
            new_row = {'Instruction': "WriteStr", 'Value': statement}
            quad_row = {'Instruction': "writestr", 'Op1': None, 'Op2': None, 'Result': statement}
            quad.append(quad_row)
        else:
            new_row = {'Instruction': "WriteVar", 'Value': statement}
            quad_row = {'Instruction': "writevar", 'Op1': None, 'Op2': None, 'Result': statement}
            quad.append(quad_row)
        # instructions.append(new_row)
        return

    def store_id(self, var_name):
        new_row = {'Variable': var_name, 'Type': None, 'Value': None}
        # data.append(new_row)
        return

    def variable_declaration(self, type_value):
        # for row in data:
        #    row['Type'] = type_value
        return

    def variable_assignation(self, variable, value):
        new_row = {'Instruction': "assign", 'Op1': variable, 'Op2': None, 'Result': value}
        quad.append(new_row)
        # for row in data:
        #    if row['Variable'] == variable:
        #        row['Value'] = value
        # print("value that reaches declaration : ", p[2])
        return

    def begin_statement(self):
        new_row = {'Instruction': "begin_state", 'Op1': "1", 'Op2': "1", 'Result': len(quad)}
        quad.append(new_row)
        return len(quad) - 1

    def end_statement(self):
        new_row = {'Instruction': "end_state", 'Op1': "1", 'Op2': "1", 'Result': len(quad)}
        quad.append(new_row)
        return len(quad) - 1

    def program_end(self, struct):
        print("--------------QUAD----------------")
        for row in reversed(quad):
            print(row)
        print("--------------OPQUAD----------------")
        for row3 in expression_quad:
            print(row3)
        print("--------------PROGRAM----------------")
        evaluate_instructions(quad, ignore_list)
        print("--------------QUAD----------------")
        for row in reversed(quad):
            print(row)
        print("--------------OPQUAD----------------")
        for row3 in expression_quad:
            print(row3)
        # print("=====================")
        # for row in ignore_list:
        #    print(row)


# -------------------------------------------------------------------------------------------------------------------

# Returns the row of a given pointer
def retrieve_row_from_ptr(ptr, quad_struct):
    counter = 0
    for row in quad_struct:
        if counter == ptr:
            # print(row)
            return row
            # eval
        else:
            counter += 1
    return


def reset_expression_quad():
    for row in expression_quad:
        for row2 in static_quad:
            row['Instruction'] = row2['1']
            row['Op1'] = row2['2']
            row['Op2'] = row2['3']
            row['Result'] = row2['4']
    return

def retrieve_token_value(tokenstring):
    for row in quad:
        if tokenstring == row['Op1']:
            return row['Result']

def modify_token_result(tokenstring, value):
    for row in reversed(quad):
        if tokenstring == row['Op1']:
            row['Result'] = value

# Checks if row has pointers if not it calculates the result of the row
def evaluate_row(row):
    """
    for brow in expression_quad:
        print(brow)
    print("----------") """
    temp_row = row
    if row is None:
        print("row is none")
        return 1
    if type(row['Op1']) is int:
        value1 = retrieve_row_from_ptr(row['Op1'], expression_quad)
        row['Op1'] = evaluate_row(value1)
    if type(row['Op2']) is int:
        value2 = retrieve_row_from_ptr(row['Op2'], expression_quad)
        row['Op2'] = evaluate_row(value2)
    if type(row['Op1']) is Token:
        row['Op1'] = retrieve_token_value(row['Op1'].getstr())
    if type(row['Op2']) is Token:
        row['Op2'] = retrieve_token_value(row['Op2'].getstr())
    resultado = calculate_row(row)
    # print("Result from row ", resultado)
    # print("=====================aaaaaaaaaaaaaaaaaaaaaaaaaa")
    return resultado  # calculate_row(row)


def calculate_row(row):
    # print("Operand 1 value is ", row['Op1'])
    # print("Operand 2 value is ", row['Op2'])
    value1 = int(row['Op1'])
    value2 = int(row['Op2'])
    if row['Instruction'] == "mult":
        row['Result'] = value1 * value2
    elif row['Instruction'] == "div":
        row['Result'] = value1 / value2
    elif row['Instruction'] == "sum":
        row['Result'] = value1 + value2
    elif row['Instruction'] == "sub":
        row['Result'] = value1 - value2
    elif row['Instruction'] == "greater":
        row['Result'] = value1 > value2
    elif row['Instruction'] == "less":
        row['Result'] = value1 < value2
    elif row['Instruction'] == "equality":
        row['Result'] = value1 == value2
    elif row['Instruction'] == "inequality":
        row['Result'] = value1 != value2
    elif row['Instruction'] == "greaterequal":
        row['Result'] = value1 >= value2
    elif row['Instruction'] == "lessequal":
        row['Result'] = value1 <= value2
    elif row['Instruction'] == "incremental":
        row['Result'] = value1 + 1
    elif row['Instruction'] == "decremental":
        row['Result'] = value1 - 1
    return str(int(row['Result']))


def add_to_ignore_list(struct, begin, end):
    for i in range(begin, end + 1):  # Range from index 1 to 3 (exclusive)
        ignore_list.append(struct[i])


def add_to_while_ignore_list(struct, begin, end, while_row):
    for i, value in enumerate(struct):
        if begin <= i <= end:
            continue
        while_ignore_list.append(struct[i])
    for row2 in while_ignore_list:
        if row2 == while_row:
            while_ignore_list.remove(row2)


def evaluate_instructions(struct, evaluate_ignore_list):
    #reset_expression_quad()
    skip = False
    counter = 0
    for row in reversed(struct):
        counter += 1
        for ignore_row in evaluate_ignore_list:
            if row == ignore_row:
                skip = True
                break
            else:
                skip = False
        if skip:
            continue

        if row['Instruction'] == "writestr":
            # print("write var")
            print(row['Result'])

        elif row['Instruction'] == "assign":
            if type(row['Result']) is int:
                var_retrieved_value = evaluate_row(retrieve_row_from_ptr(row['Result'], expression_quad))
                row['Result'] = var_retrieved_value
            elif type(row['Result']) is Token:
                row['Result'] = retrieve_token_value(row['Result'].getstr())
            else:
                continue
        elif row['Instruction'] == "writevar":
            # print("writevar")
            for row2 in reversed(struct):
                if row2['Op1'] == row['Result']:
                    print( row2['Result'])

        elif row['Instruction'] == "if":
            #print("if", counter)
            var_retrieved_value = evaluate_row(retrieve_row_from_ptr(row['Result'], expression_quad))
            row['Result'] = var_retrieved_value
            if int(var_retrieved_value) == 1:
                if_list = quad[row['Op2']:row['Op1']]
                evaluate_instructions(if_list, ignore_list)
                add_to_ignore_list(struct, row['Op2'], row['Op1'])
                #skip = False
            else:
                add_to_ignore_list(struct, row['Op2'], row['Op1'])
                #skip = True

        elif row['Instruction'] == "else":
            # print("else")
            if_row = retrieve_row_from_ptr(row['Result'], struct)
            if if_row['Result'] == "0":
                continue
            else:
                add_to_ignore_list(struct, row['Op2'], row['Op1'])

        elif row['Instruction'] == "while":
            # print("while")
            # revisar statement de while
            reset_expression_quad()
            var_retrieved_value = evaluate_row(retrieve_row_from_ptr(row['Result'], expression_quad))
            #row['Result'] = var_retrieved_value
            #print("corriendo mafacka", var_retrieved_value)
            # if true
            # print("Retrieved while bool", var_retrieved_value)
            if int(var_retrieved_value) == 1:
                #evaluar si es la primera corrida, si no es no hacer ete pedo
                add_to_while_ignore_list(struct, row['Op2'], row['Op1'], row)
                print("===========While Ignore List==========")
                for row2 in while_ignore_list:
                    print(row2)
                print("======================================")
                evaluate_instructions(quad, while_ignore_list)
            else:
                print("falaso")

            # añadir lo que no sea el bloque a la ignore_list
            # evaluar instrucciones de nuevo con  evaluate instruction y
            # probablemente alterar el statement del while con el codigo del bloque
            # else
            # eliminar valores del ignore list
            # continuar la ejecucion

        elif row['Instruction'] == "incremental" or row['Instruction'] == "decremental":
            if type(row['Op1']) is Token:
                variable = row['Op1'].getstr()
            else:
                variable = row['Op1']
            result = evaluate_row(row)
            row['Result'] = result
            modify_token_result(variable, result)
    return