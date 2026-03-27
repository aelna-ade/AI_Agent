from google.genai import types
from copy import deepcopy
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file


# Mapping des noms de fonction vers les fonctions réelles
function_map = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file,
}


def call_function(function_call, verbose=False):
    """
    Appelle une des quatre fonctions disponibles et retourne le résultat.
    """
    # Récupérer le nom de la fonction (garantir une chaîne de caractères)
    function_name = function_call.name or ""
    
    # Afficher selon le mode verbose
    if verbose:
        print(f"Calling function: {function_name}({function_call.args})")
    else:
        print(f" - Calling function: {function_name}")
    
    # Vérifier si la fonction existe dans le mapping
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    # Faire une copie shallow des arguments
    args = dict(function_call.args) if function_call.args else {}
    
    # Ajouter le working_directory
    args["working_directory"] = "./calculator"
    
    # Appeler la fonction réelle avec les arguments (keyword arguments)
    function = function_map[function_name]
    function_result = function(**args)
    
    # Retourner le résultat dans un objet types.Content
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
