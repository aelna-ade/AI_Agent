import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if valid_target_dir is False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        listdir = os.listdir(target_dir)
        result = []
        for item in listdir:
            chemin = os.path.join(target_dir, item)
            taille = os.path.getsize(chemin)
            dossierverif = os.path.isdir(chemin)
            result.append(f'- {item}: file_size={taille} bytes, is_dir={dossierverif}')
        return "\n".join(result)

    except Exception as e:
        return f"Error: {e}"