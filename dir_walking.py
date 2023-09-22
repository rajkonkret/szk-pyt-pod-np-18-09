import os

# os do działań z katalogami/plikami

for root, dirs, files in os.walk("../szk-pyt-pod-np-18-09"):
    for file in files:
        if file == 'api_get.py':
            file_path = os.path.join(root, file)
            print(file_path)  # ../szk-pyt-pod-np-18-09\api_get.py
            # "\\szk-pyth\\api_get.py"

for root, dirs, files in os.walk(".."):
    abs_root = os.path.abspath(root)
    # print(abs_root)
    if dirs:
        print("Directories")
        for dir_ in dirs:
            print(dir_)
    if files:  # if files == True
        print("Files:")
        for filename in files:
            print(filename)
