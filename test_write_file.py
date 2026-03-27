from functions.write_file import write_file

def run_tests():

    print('Test 1: Fichier simple')
    res1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Result: {res1}\n")


    print('Test 2: Fichier dans un sous-dossier')
    res2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Result: {res2}\n")


    print('Test 3: Tentative hors zone autorisée')
    res3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Result: {res3}\n")

if __name__ == "__main__":
    run_tests()