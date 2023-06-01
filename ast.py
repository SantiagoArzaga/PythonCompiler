from rply import Token

data = []
instructions = [{'Instruction': None, 'Value': None}]
quad = []


# 0 mult 3 4 12
# 1 sum r0 3 15
class AbstractSyntaxTree():
    def __init__(self, value):
        self.value = value

    def retrieve_var_value(self, variable):
        # Find the variable in the table
        value_found = False
        for row in data:
            print(row)
        int(variable)
        if isinstance(variable, int):
            print("true")
            return variable
        else:
            print("false")
            for row in data:
                if row['Variable'] == variable:
                    return row['Value']
                    value_found = True
            if not value_found:
                print("Variable '", row['Value'], "' not declared")
                return

    def Greater(self, left, right):
        new_row = {'Instruction': "greater", 'Op1': left, 'Op2': right, 'Result': None}
        quad.append(new_row)
        #greater = int(left) > int(right)
        return #greater

    def Less(self, left, right):
        new_row = {'Instruction': "less", 'Op1': left, 'Op2': right, 'Result': None}
        quad.append(new_row)
        #less = int(left) < int(right)
        return len(quad)#less

    def Equality(self, left, right):
        new_row = {'Instruction': "equality", 'Op1': left, 'Op2': right, 'Result': None}
        quad.append(new_row)
        #equality = left == right
        return #equality

    def Sum(self, left, right):
        new_row = {'Instruction': "sum", 'Op1': left, 'Op2': right, 'Result': None}
        quad.append(new_row)
        #sum = int(left) + int(right)
        return len(quad) - 1#sum

    def Sub(self, left, right):
        new_row = {'Instruction': "sub", 'Op1': left, 'Op2': right, 'Result': None}
        quad.append(new_row)
        #sub = int(left) - int(right)
        return #sub

    def Mult(self, left, right):
        new_row = {'Instruction': "mult", 'Op1': left, 'Op2': right, 'Result': None}
        quad.append(new_row)
        #mult = int(left) * int(right)
        return len(quad) - 1#mult

    def Div(self, left, right):
        new_row = {'Instruction': "div", 'Op1': left, 'Op2': right, 'Result': None}
        quad.append(new_row)
        #div = int(left) / int(right)
        return len(quad) - 1#div

    def write_instruction(self, statement, type):
        if type == "string":
            new_row = {'Instruction': "WriteStr", 'Value': statement}
            quad_row = {'Instruction': "writestr", 'Op1': None, 'Op2': None, 'Result': statement}
            quad.append(quad_row)
        else:
            quad_row = {'Instruction': "writevar", 'Op1': None, 'Op2': None, 'Result': statement}
            quad.append(quad_row)
            new_row = {'Instruction': "WriteVar", 'Value': statement}
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

    def program_end(self):
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
        for row in quad:
            print(row)
        for row in quad:
            if row['Instruction'] == "mult":
                #print("mult")
                row['Result'] = get_value(row['Op1']) * get_value(row['Op2'])
                #print(row['Result'])
            elif row['Instruction'] == "div":
                #print("div")
                row['Result'] = get_value(row['Op1']) / get_value(row['Op2'])
                #print(row['Result'])
            elif row['Instruction'] == "sum":
                #print("sum")
                row['Result'] = get_value(row['Op1']) + get_value(row['Op2'])
                #print(row['Result'])
            elif row['Instruction'] == "sub":
                #print("sub")
                row['Result'] = get_value(row['Op1']) - get_value(row['Op2'])
                #print(row['Result'])

        for row in reversed(quad):
            if row['Instruction'] == "writevar":
                #print("write var")
                row['Result'] = get_pointer(row['Result'])
                variable_pointer = get_value(row['Result'])
                result = get_value(variable_pointer)
                print(result)
            elif row['Instruction'] == "writestr":
                #print("write var")
                print(row['Result'])
        #print("Value of x ", get_value("x"))


#make a function to just return the values

def get_value(value):
    if type(value) is Token:
        get_value(value.getstr())
    elif type(value) is int:
        return quad[value]['Result']
    elif value.isnumeric():
        return int(value)
    else:
        for row in quad:
            if value == row['Op1']:
                return get_value(row['Result'])


def get_pointer(value):
    counter = 0
    for row in quad:
        if value == row['Op1']:
            return counter
        else:
            counter += 1

