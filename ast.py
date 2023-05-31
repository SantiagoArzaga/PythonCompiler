
data = []
instructions = [{'Instruction': None, 'Value': None}]
class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Mult(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()


class Equal(BinaryOp):
    def eval(self):
        a = self.left.eval()
        b = self.right.eval()
        return self.left.eval() % self.right.eval()


class Write(Number):
    def __init__(self, value):
        self.value = value

    print(Number)

    def eval(self):
        print(self.value.eval())

class AbstractSyntaxTree():
    def __init__(self, value):
        self.value = value

    def Sum(left, right):
        sum = int(left) + int(right)
        return sum

    def Sub(left, right):
        sub = int(left) - int(right)
        return sub

    def Mult(left, right):
        mult = int(left) * int(right)
        return mult

    def Div(left, right):
        div = int(left) / int(right)
        return div

    def write_instruction(self, statement):
        new_row = {'Instruction': "Write", 'Value': statement}
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
        for row in data:
            if row['Variable'] == variable:
                row['Value'] = value
            #print("value that reaches declaration : ", p[2])
        return

    def program_end(self):
        for row in instructions:
            if row['Instruction'] == "Write":
                for row2 in data:
                    if row2['Variable'] == row['Value']:
                        print(row2['Value'])
