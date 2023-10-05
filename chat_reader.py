import mmap
import os

def read_from_memory_mapped_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        # Create a memory-mapped file
        mmapped_file = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        mmapped_file.seek(0, os.SEEK_SET)

        # Read and print the content of the memory-mapped file
        content = mmapped_file.read().decode('utf-8')
        print(content)

if __name__ == "__main__":
    file_name = "chat_log.txt"
    print("Chat Reader Application")

    while True:
        input("Press Enter to read the chat:")
        read_from_memory_mapped_file(file_name)
