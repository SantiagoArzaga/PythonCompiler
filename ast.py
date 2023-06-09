from llvmlite import ir  # ------


class Number():
    def __init__(self, builder, module, value):  # ------
        self.builder = builder  # ------
        self.module = module  # ------
        self.value = value

    def eval(self):
        i = ir.Constant(ir.IntType(8), int(self.value))  # ------
        return i  # ------


class Letter():
    def __init__(self, builder, module, value):  # ------
        self.builder = builder  # ------
        self.module = module  # ------
        self.value = value

    def eval(self):
        i = ir.Constant(ir.ArrayType(8), str(self.value))  # ------ Esto probablemente es distinto dado que es letra
        return i  # ------


class BinaryOp():
    def __init__(self, builder, module, left, right):  # ------
        self.builder = builder  # ------
        self.module = module  # ------
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        i = self.builder.add(self.left.eval(), self.right.eval())
        return i


class Sub(BinaryOp):
    def eval(self):
        i = self.builder.sub(self.left.eval(), self.right.eval())
        return i


class Mult(BinaryOp):
    def eval(self):
        i = self.builder.mul(self.left.eval(), self.right.eval())
        return i


class Div(BinaryOp):
    def eval(self):
        i = self.builder.udiv(self.left.eval(), self.right.eval())
        return i


class Equal(BinaryOp):
    def eval(self):
        i = self.builder.store(self.left.eval(), self.right.eval())
        return i

class VariableAssign(BinaryOp):
    def eval(self):
        # Evaluate the right-hand side expression
        rhs_value = self.right.eval()

        # Store the value in the variable
        self.builder.store(rhs_value, self.left.eval())

        # Return the assigned value
        return rhs_value

# ----------------- #
class Write():
    def __init__(self, builder, module, write, value):
        self.builder = builder
        self.module = module
        self.write = write
        self.value = value

    def eval(self):
        value = self.value.eval()

        # Declare argument list
        voidptr_ty = ir.IntType(8).as_pointer()
        fmt = "%i \n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
                            bytearray(fmt.encode("utf8")))
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr")
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)

        # Call Print Function
        self.builder.call(self.write, [fmt_arg, value])

# ----------------- #
