def parse_number(prompt: str) -> float:
    """Prompt until the user enters a valid number, then return it as float."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Invalid number. Please try again.")


def parse_operator(prompt: str) -> str:
    """Prompt until the user enters a supported operator using if/elif/else.

    Supports symbol operators and their word forms.
    """
    while True:
        raw = input(prompt).strip().lower()

        # Direct symbol checks
        if raw == "+":
            return "+"
        elif raw == "-":
            return "-"
        elif raw == "*":
            return "*"
        elif raw == "/":
            return "/"
        elif raw == "%":
            return "%"
        elif raw == "//":
            return "//"
        elif raw == "**":
            return "**"

        # Word forms mapping via if/elif/else
        elif raw in ("add", "plus", "sum"):
            return "+"
        elif raw in ("subtract", "minus", "difference"):
            return "-"
        elif raw in ("multiply", "times", "product"):
            return "*"
        elif raw in ("divide", "division"):
            return "/"
        elif raw in ("mod", "modulo", "remainder"):
            return "%"
        elif raw in ("floor", "floor-divide", "floordivide"):
            return "//"
        elif raw in ("power", "pow", "exponent"):
            return "**"
        else:
            print("Invalid operator. Choose one of: +, -, *, /, %, //, ** or words like add, subtract, multiply, divide, mod, floor, power.")


def calculate(left: float, operator: str, right: float) -> float:
    """Perform a calculation for the given operands and operator."""
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return left / right
    if operator == "%":
        if right == 0:
            raise ZeroDivisionError("Modulo by zero is not allowed.")
        return left % right
    if operator == "//":
        if right == 0:
            raise ZeroDivisionError("Floor division by zero is not allowed.")
        return left // right
    if operator == "**":
        return left ** right
    raise ValueError(f"Unsupported operator: {operator}")


# Safe expression evaluation using Python AST
import ast
import operator as pyop


_ALLOWED_BINOPS = {
    ast.Add: pyop.add,
    ast.Sub: pyop.sub,
    ast.Mult: pyop.mul,
    ast.Div: pyop.truediv,
    ast.Mod: pyop.mod,
    ast.FloorDiv: pyop.floordiv,
    ast.Pow: pyop.pow,
}


def _eval_ast(node: ast.AST) -> float:
    if isinstance(node, ast.Expression):
        return _eval_ast(node.body)
    if isinstance(node, ast.BinOp):
        left_val = _eval_ast(node.left)
        right_val = _eval_ast(node.right)
        op_type = type(node.op)
        if op_type not in _ALLOWED_BINOPS:
            raise ValueError("Unsupported operator in expression.")
        if op_type in {ast.Div, ast.Mod, ast.FloorDiv} and right_val == 0:
            raise ZeroDivisionError("Division/modulo by zero in expression.")
        return _ALLOWED_BINOPS[op_type](left_val, right_val)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        operand_val = _eval_ast(node.operand)
        return +operand_val if isinstance(node.op, ast.UAdd) else -operand_val
    if isinstance(node, ast.Num):  # Python <3.8
        return float(node.n)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    raise ValueError("Unsupported expression element.")


def evaluate_expression(expr: str) -> float:
    """Safely evaluate a math expression using a restricted AST.

    Supports: +, -, *, /, %, //, **, parentheses, and unary +/-. No names or function calls.
    """
    parsed = ast.parse(expr, mode="eval")
    return _eval_ast(parsed)


def main() -> None:
    print("Simple Calculator (supports +, -, *, /, %, //, **)")
    print("You can either:")
    print("  1) Enter numbers and an operator when prompted, or")
    print("  2) Enter a full expression (e.g., 2 + 3 * 4) when asked.")
    while True:
        mode = input("Use full expression mode? (y/n): ").strip().lower()
        try:
            if mode in {"y", "yes"}:
                expr = input("Enter expression: ").strip()
                result = evaluate_expression(expr)
                print(f"Result: {result}")
            else:
                left = parse_number("Enter the first number: ")
                operator = parse_operator("Enter operator (+, -, *, /, %, //, ** or words): ")
                right = parse_number("Enter the second number: ")
                result = calculate(left, operator, right)
                print(f"Result: {left} {operator} {right} = {result}")
        except ZeroDivisionError as err:
            print(f"Error: {err}")
        except Exception as err:
            print(f"Error: {err}")

        again = input("Do another calculation? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()


