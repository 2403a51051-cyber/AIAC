import operator as op

operation = "multiply"
a, b = 5, 3

operations = {
    "add": op.add,
    "subtract": op.sub,
    "multiply": op.mul,
}

func = operations.get(operation)
result = func(a, b) if func else None
print(result)


