import hashlib
import os

def hash_file(file_path1, file_path2):
    hasher1 = hashlib.sha1()
    hasher2 = hashlib.sha1()

    try:
        with open(file_path1, "rb") as file1:
            for chunk in iter(lambda: file1.read(4096), b''):
                hasher1.update(chunk)

        with open(file_path2, "rb") as file2:
            for chunk in iter(lambda: file2.read(4096), b''):
                hasher2.update(chunk)

        return hasher1.hexdigest(), hasher2.hexdigest()

    except FileNotFoundError:
        print("Error: One or both files not found.")
        return None, None

file_path1 = os.path.abspath("pd1.pdf")
file_path2 = os.path.abspath("pd1.pdf")

msg1, msg2 = hash_file(file_path1, file_path2)

if msg1 is not None and msg2 is not None:
    if msg1 != msg2:
        print("These files are not identical.")
    else:
        print("These files are identical.")
