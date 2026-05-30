import ast
import inspect
import numpy as np
def homework(a):
    a=np.array(a)
    result = a[(a % 5 == 0) & (a % 2 == 1)]
    return result

def hw_public_tests():
    print("=== Public Tests ===")

    source = inspect.getsource(homework)
    tree = ast.parse(source)

    # Test 1: Disallow import statements
    print("Test 1: Check for import statements...", end=" ")
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            print("NG")
            print("  homework() contains import statements. Please remove them.")
            return
    print("OK")

    print("=== All Public Tests Passed ===")


hw_public_tests()
a = np.array([1, 5, 10, 3, 4, 25, 30])
print(homework(a))