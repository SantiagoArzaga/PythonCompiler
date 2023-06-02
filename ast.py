from rply import Token

data = []
instructions = [{'Instruction': None, 'Value': None}]
expression_quad = []
quad = []


# 0 mult 3 4 12
# 1 sum r0 3 15
class AbstractSyntaxTree():
    def __init__(self, value):
        self.value = value
    def expression_instruction(self, value):
        new_row = {'Instruction': "expression", 'Op1': None, 'Op2': None, 'Result': value}
        expression_quad.append(new_row)
        #greater = int(left) > int(right)
        return len(quad) - 1
    def Greater(self, left, right):
        new_row = {'Instruction': "greater", 'Op1': left, 'Op2': right, 'Result': None}
        expression_quad.append(new_row)
        #greater = int(left) > int(right)
        return len(expression_quad) - 1

    def Less(self, left, right):
        new_row = {'Instruction': "less", 'Op1': left, 'Op2': right, 'Result': None}
        expression_quad.append(new_row)
        #less = int(left) < int(right)
        return len(expression_quad) - 1

    def Equality(self, left, right):
        new_row = {'Instruction': "equality", 'Op1': left, 'Op2': right, 'Result': None}
        expression_quad.append(new_row)
        #equality = left == right
        return len(expression_quad) - 1

    def Sum(self, left, right):
        new_row = {'Instruction': "sum", 'Op1': left, 'Op2': right, 'Result': None}
        expression_quad.append(new_row)
        #sum = int(left) + int(right)
        return len(expression_quad) - 1

    def Sub(self, left, right):
        new_row = {'Instruction': "sub", 'Op1': left, 'Op2': right, 'Result': None}
        expression_quad.append(new_row)
        #sub = int(left) - int(right)
        return len(expression_quad) - 1

    def Mult(self, left, right):
        new_row = {'Instruction': "mult", 'Op1': left, 'Op2': right, 'Result': None}
        expression_quad.append(new_row)
        #mult = int(left) * int(right)
        return len(expression_quad) - 1

    def Div(self, left, right):
        new_row = {'Instruction': "div", 'Op1': left, 'Op2': right, 'Result': None}
        expression_quad.append(new_row)
        #div = int(left) / int(right)
        return len(expression_quad) - 1

    def if_statement(self, statement):
        new_row = {'Instruction': "if", 'Op1': None, 'Op2': None, 'Result': statement}
        quad.append(new_row)
        return
    def while_statement(self, statement):
        new_row = {'Instruction': "while", 'Op1': None, 'Op2': None, 'Result': statement}
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
        instructions.append(new_row)
        return

    def store_id(self, var_name):
        new_row = {'Variable': var_name, 'Type': None, 'Value': None}
        data.append(new_row)
        return

    def variable_declaration(self, type_value):
        for row in data:
            row['Type'] = type_value
        return

    def variable_assignation(self, variable, value):
        new_row = {'Instruction': "assign", 'Op1': variable, 'Op2': None, 'Result': value}
        quad.append(new_row)
        for row in data:
            if row['Variable'] == variable:
                row['Value'] = value
            # print("value that reaches declaration : ", p[2])
        return

    def begin_statement(self):
        new_row = {'Instruction': "begin_state", 'Op1': "1", 'Op2': "1", 'Result': len(quad)}
        quad.append(new_row)
        return
    def end_statement(self):
        new_row = {'Instruction': "end_state", 'Op1': "1", 'Op2': "1", 'Result': len(quad)}
        quad.append(new_row)
        return
    def program_end(self, struct):
        #if struct == None:
        #    struct = quad
        struct = expression_quad
        print("--------------QUAD----------------")
        for row in reversed(quad):
            print(row)
        print("--------------OPQUAD----------------")
        for row3 in struct:
            print(row3)
        print("--------------PROGRAM----------------")
        for row in reversed(quad):
            if row['Instruction'] == "writestr":
                # print("write var")
                print(row['Result'])
            elif row['Instruction'] == "assign":
                #result = get_value(row['Result'], struct)
                var_retrieved_value = evaluate_row(retrieve_ptr_row(row['Result'], struct))
                #print("Value mafaca is ", var_retrieved_value)
                row['Result'] = var_retrieved_value
                #llamar funcion que corra la instruccion del ptr del resultado
                #si cualquier operador tiene ptr correr la misma funcion
                #print(result)
            elif row['Instruction'] == "writevar":
                for row2 in reversed(quad):
                    if row2['Op1'] == row['Result']:
                        print(row2['Result'])
                #variable_pointer = get_value(row['Result'], struct)
                #result = get_value(variable_pointer, struct)
                #print(result)
            elif row['Instruction'] == "if":
                #print("if")
                var_retrieved_value = evaluate_row(retrieve_ptr_row(row['Result'], struct))
                row['Result'] = var_retrieved_value
                #print(var_retrieved_value)
                skip = True
                if int(var_retrieved_value) == 1:
                    print("True")
                else:
                    print("False")
                    if skip:
                        if row['Instruction'] != "end_statement":
                            print("Skipped row", row)
                            continue
                        else:
                            skip = False

                    print("False")
            #elif row['Instruction'] == "begin_state":
                #result = get_value(row['Result'], struct)
                #print(result)

        print("dick")
        for row in reversed(quad):
            print(row)

        for row3 in struct:
            print(row3)


            """
        for row in struct:
            if row['Instruction'] == "mult":
                #print("mult")
                row['Result'] = get_value(row['Op1'], struct) * get_value(row['Op2'], struct)
                #print(row['Result'])
            elif row['Instruction'] == "div":
                #print("div")
                row['Result'] = get_value(row['Op1'], struct) / get_value(row['Op2'], struct)
                #print(row['Result'])
            elif row['Instruction'] == "sum":
                #print("sum")
                row['Result'] = get_value(row['Op1'], struct) + get_value(row['Op2'], struct)
                #print(row['Result'])
            elif row['Instruction'] == "sub":
                #print("sub")
                row['Result'] = get_value(row['Op1'], struct) - get_value(row['Op2'], struct)
                #print(row['Result'])
            elif row['Instruction'] == "greater":
                #print("sub")
                row['Result'] = get_value(row['Op1'], struct) > get_value(row['Op2'], struct)
                #print(row['Result'])
            elif row['Instruction'] == "less":
                #print("sub")
                row['Result'] = get_value(row['Op1'], struct) < get_value(row['Op2'], struct)
                #print(row['Result']) """

        """
        for row in reversed(struct):
            if row['Instruction'] == "writevar":
                #print("write var")
                row['Result'] = get_pointer(row['Result'], struct)
                variable_pointer = get_value(row['Result'], struct)
                result = get_value(variable_pointer, struct)
                print(result)
            elif row['Instruction'] == "writestr":
                #print("write var")
                print(row['Result'])
            elif row['Instruction'] == "if":
                result = get_value(row['Result'], struct)
                print(result) """
                #for row in reversed(struct):
                #    if row['Instruction'] == "begin_state":
                #        begin_ptr = row['Result']
                #    elif row['Instruction'] == "end_state":
                #        end_ptr = row['Result']
                #temporal = generate_temp_quad()
                #struct = remove_statement_rows(struct)
                #if result:
                    #print(begin_ptr, end_ptr)
                    #self.program_end(self, temporal)
                    #if_quad.clear()
            #"""
            #elif row['Instruction'] == "while":
            #    result = get_value(row['Result'], struct)
            #    temp_quad = generate_temp_quad(struct)
            #    struct = remove_statement_rows(struct)
            #    if result:
            #        print("TRUE WHILE") """
                    #self.program_end(self, temp_quad)


                #depending on result, evaluate quad from begin state to end state, then continue

        #print("Value of x ", get_value("x"))
        #print("=====================")
        #for row in struct:
        #    print(row)

#-------------------------------------------------------------------------------------------------------------------
#get value from a pointer or stri
# ng

def retrieve_ptr_row(ptr, quad_struct):
    counter = 0
    for row in quad_struct:
        if counter == ptr:
            #print(row)
            return row
            #eval
        else:
            counter += 1
    return

def retrieve_token_value(tokenstring):
    for row in quad:
        if tokenstring == row['Op1']:
            return row['Result']

#Checks if row has pointers if not it calculates the result of the row
def evaluate_row(row):
    """
    for brow in expression_quad:
        print(brow)
    print("Row is " , row)
    print("----------") """
    if row['Op1'] is None:
        print("Row is empty")
    if type(row['Op1']) is int:
        value1 = retrieve_ptr_row(row['Op1'], expression_quad)
        row['Op1'] = evaluate_row(value1)
    if type(row['Op2']) is int:
        value2 = retrieve_ptr_row(row['Op2'], expression_quad)
        row['Op2'] = evaluate_row(value2)
    if type(row['Op1']) is Token:
        row['Op1'] = retrieve_token_value(row['Op1'].getstr())
    if type(row['Op2']) is Token:
        row['Op2'] = retrieve_token_value(row['Op2'].getstr())
    resultado = calculate_row(row)
    #print("Result from row ", resultado)
    #print("=====================aaaaaaaaaaaaaaaaaaaaaaaaaa")
    return resultado #calculate_row(row)

def calculate_row(row):
    #print("Operand 1 value is ", row['Op1'])
    #print("Operand 2 value is ", row['Op2'])
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
    return str(int(row['Result']))












def get_value(value, quad_struct):
    if type(value) is Token:
        get_value(value.getstr(),quad_struct)
    elif type(value) is int:
        return quad_struct[value]['Result']
    elif value.isnumeric():
        return int(value)
    else:
        #If the value is not a Token, not a pointer and not a "number" i.e. it's a variable string like "x"
        #then it gets the value of the pointer in the var quad row
        for row in quad_struct:
            if value == row['Op1']:
                #change instruction to one that runs on the inverse quad
                return get_value(row['Result'],quad_struct)

#si es instruccion assign, va a tener un valor que hacer en la tabla de expresiones

#si un operador es pointer, resuelve ese pointer primero,
#luego regresa el valor de la operacion y lo guarda

def get_pointer(value, quad_list2):
    counter = 0
    for row in quad_list2:
        if value == row['Op1']:
            return counter
        else:
            counter += 1

def generate_temp_quad():
    temp = []
    empty_rows = 0
    empty_count = 0
    for row in reversed(quad):
        if row['Instruction'] == "begin_state":
            begin_ptr = row['Result']
            empty_rows = empty_count
        elif row['Instruction'] == "end_state":
            end_ptr = row['Result']
        else:
            empty_count += 1
    while empty_rows > 0:
        temp.append({'Instruction': "empty", 'Op1': "0", 'Op2': "0", 'Result': 0})
        empty_rows -= 1
    temp.extend(quad[begin_ptr:end_ptr+1])
    return temp

def remove_statement_rows(data_list2):
    replacement_row = {'Instruction': "empty", 'Op1': "0", 'Op2': "0", 'Result': 0}
    for row in reversed(quad):
        if row['Instruction'] == "begin_state":
            begin_ptr = row['Result']
        elif row['Instruction'] == "end_state":
            end_ptr = row['Result'] + 1
    data_list2[begin_ptr:end_ptr] = [replacement_row] * (end_ptr - begin_ptr)
    return data_list2
