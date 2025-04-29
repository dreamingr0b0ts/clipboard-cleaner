import pyperclip

def clear_clipboard():
    pyperclip.copy('')
    print("Clipboard cleared.")

if __name__ == "__main__":
    clear_clipboard()

