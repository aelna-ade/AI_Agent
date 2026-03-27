from functions.run_python_file import run_python_file

def run_tests():

    print("--- Test 1: main.py (Usage) ---")
    print(run_python_file("calculator", "main.py"))
    print("\n")


    print("--- Test 2: main.py (3 + 5) ---")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print("\n")


    print("--- Test 3: tests.py ---")
    print(run_python_file("calculator", "tests.py"))
    print("\n")


    print("--- Test 4: Sécurité ../ ---")
    print(run_python_file("calculator", "../main.py"))
    print("\n")

    
    print("--- Test 5: Inexistant ---")
    print(run_python_file("calculator", "nonexistent.py"))
    print("\n")

    
    print("--- Test 6: Pas un .py ---")
    
    print(run_python_file("calculator", "lorem.txt"))
    print("\n")

if __name__ == "__main__":
    run_tests()