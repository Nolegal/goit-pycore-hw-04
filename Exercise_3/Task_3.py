from pathlib import Path
from colorama import Fore

# Створення об'єкту Path для директорії
directory = Path("picture")

# Виведення переліку всіх файлів та піддиректорій
def    check_file(directory):
     for path in directory.iterdir():
        if path.is_dir():
            check_file(path)
        else:
            print(Fore.BLUE+f"{directory.name}/"+Fore.GREEN+f"{path.name}")
 


print(check_file(directory))

