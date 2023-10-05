import mmap
import os

def write_to_file(filename, message):
    with open(filename, 'a') as file:
        file.write(message + '\n')

def write_to_memory_mapped_file(filename, message):
    with open(filename, 'a') as file:
        file.write(message + '\n')
    with open(filename, 'r', encoding='utf-8') as file:
        # Create a memory-mapped file
        mmapped_file = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        mmapped_file.seek(0, os.SEEK_END)
        mmapped_file.write(message.encode('utf-8'))

if __name__ == "__main__":
    file_name = "chat_log.txt"
    print("Chat Writer Application")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "/exit":
            print("Exiting the chat.")
            break

        write_to_memory_mapped_file(file_name, f"You: {user_input}")
