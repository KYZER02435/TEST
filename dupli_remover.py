import os
import time

W = '\x1b[1;37m'
Y = '\x1b[1;33m'
B = '\x1b[1;34m'
P = '\x1b[1;35m'
G = '\x1b[1;32m'
R = '\x1b[1;31m'

def clear():
    os.system('clear')

logo = """
DUPLI REMOVER
"""

def linex():
    print('-' * 50)

def back():
    pass  # Define what should be done to go back

def remove_dub():
    clear()
    print(logo)
    try:
        filename = input(f" [{B}>>{W}] ENTER FILE NAME: ")
        sd = '/sdcard/'
        file_path = os.path.join(sd, filename)
        
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
        
        total_count = len(lines)
        unique_lines = list(dict.fromkeys(lines))  # Remove duplicates while preserving order
        unique_count = len(unique_lines)
        
        with open(file_path, 'w') as file:
            for line in unique_lines:
                file.write(line + '\n')
        
        linex()
        print(f' [{B}•{W}] SUCCESSFULLY REMOVED')
        print(f' [{B}•{W}] Total Count of IDs with Duplicates: {total_count}')
        print(f' [{B}•{W}] Total Saved IDs without Duplicates: {unique_count}')
        input(f' [{B}•{W}] PRESS ENTER TO BACK ')
        back()
    except FileNotFoundError:
        linex()
        print(f' [{B}×{W}] FILE NOT FOUND TRY AGAIN ')
        time.sleep(2)
        remove_dub()

if __name__ == "__main__":
    remove_dub()
