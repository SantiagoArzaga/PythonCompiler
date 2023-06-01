from rply import Token

data = []
instructions = [{'Instruction': None, 'Value': None}]
quad = []
tempquad = []


# 0 mult 3 4 12
# 1 sum r0 3 15
class AbstractSyntaxTree():
    def __init__(self, value):
        self.value = value

    def Greater(self, left, right):
        new_row = {'Instruction': "greater", 'Op1': left, 'Op2': right, 'Result': None}
        quad.append(new_row)
        #greater = int(left) > int(right)
        return len(quad) - 1

    def Less(self, left, right):
        new_row = {'Instruction': "less", 'Op1': left, 'Op2': right, 'Result': None}
        quad.append(new_row)
        #less = int(left) < int(right)
        return len(quad) - 1

    def Equality(self, left, right):
        new_row = {'Instruction': "equality", 'Op1': left, 'Op2': right, 'Result': None}
        quad.append(new_row)
        #equality = left == right
        return len(quad) - 1

    def Sum(self, left, right):
        new_row = {'Instruction': "sum", 'Op1': left, 'Op2': right, 'Result': None}
        quad.append(new_row)
        #sum = int(left) + int(right)
        return len(quad) - 1

    def Sub(self, left, right):
        new_row = {'Instruction': "sub", 'Op1': left, 'Op2': right, 'Result': None}
        quad.append(new_row)
        #sub = int(left) - int(right)
        return len(quad) - 1

    def Mult(self, left, right):
        new_row = {'Instruction': "mult", 'Op1': left, 'Op2': right, 'Result': None}
        quad.append(new_row)
        #mult = int(left) * int(right)
        return len(quad) - 1

    def Div(self, left, right):
        new_row = {'Instruction': "div", 'Op1': left, 'Op2': right, 'Result': None}
        quad.append(new_row)
        #div = int(left) / int(right)
        return len(quad) - 1

    def if_statement(self, statement):
        new_row = {'Instruction': "if", 'Op1': None, 'Op2': None, 'Result': statement}
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
        new_row = {'Instruction': "begin_state", 'Op1': None, 'Op2': None, 'Result': None}
        quad.append(new_row)
        return
    def end_statement(self):
        new_row = {'Instruction': "end_state", 'Op1': None, 'Op2': None, 'Result': None}
        quad.append(new_row)
        return
    def program_end(self, struct):
        if struct == None:
            struct = quad
        """
        for row in reversed(instructions):
            if row['Instruction'] == "WriteVar":
                # Find the variable in the table
                value_found = False
                for row2 in data:
                    if row2['Variable'] == row['Value']:
                        print(row2['Value'])
                        value_found = True
                if not value_found:
                    print("Variable '", row['Value'], "' not declared")
            elif row['Instruction'] == "WriteStr":
                print(row['Value'])"""

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
                #print(row['Result'])

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
                temp_quad = generate_temp_quad(struct)
                struct = remove_statement_rows(struct)

                if result:
                    self.program_end(self, temp_quad)
                else:
                    print("IF is false")

                #depending on result, evaluate quad from begin state to end state, then continue

        #print("Value of x ", get_value("x"))
        print("=====================")
        for row in struct:
            print(row)

#-------------------------------------------------------------------------------------------------------------------
#get value from a pointer or string
def get_value(value, quad):
    if type(value) is Token:
        get_value(value.getstr())
    elif type(value) is int:
        return quad[value]['Result']
    elif value.isnumeric():
        return int(value)
    else:
        #If the value is not a Token, not a pointer and not a "number" i.e. it's a variable string like "x"
        #then it gets the value of the pointer in the var quad row
        for row in quad:
            if value == row['Op1']:
                #change instruction to one that runs on the inverse quad
                return get_value(row['Result'])


def get_pointer(value, quad):
    counter = 0
    for row in quad:
        if value == row['Op1']:
            return counter
        else:
            counter += 1

def generate_temp_quad(struct):
    temp_quad = []
    empty_rows = 0
    empty_count = 0
    begin_count = 0
    end_count = 1
    begin_ptr = 0
    end_ptr = 0
    for row in struct:
        if row['Instruction'] == "begin_state":
            begin_ptr = begin_count
            empty_rows = empty_count
        elif row['Instruction'] == "end_state":
            end_ptr = end_count
        else:
            begin_count += 1
            end_count += 1
            empty_count += 1
    while empty_rows > 0:
        temp_quad.append({'Instruction': None, 'Op1': None, 'Op2': None, 'Result': None})
        empty_rows -= 1
    temp_quad.extend(struct[begin_ptr:end_ptr])
    return temp_quad

def remove_statement_rows(struct):
    replacement_row = {'Instruction': None, 'Op1': None, 'Op2': None, 'Result': None}
    begin_count = 0
    end_count = 1
    begin_ptr = 0
    end_ptr = 0
    for row in struct:
        if row['Instruction'] == "begin_state":
            begin_ptr = begin_count
        elif row['Instruction'] == "end_state":
            end_ptr = end_count
        else:
            begin_count += 1
            end_count += 1
    struct[begin_ptr:end_ptr] = [replacement_row] * (end_ptr - begin_ptr)
    return struct
