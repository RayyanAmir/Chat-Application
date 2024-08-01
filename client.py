import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog

# Global variables
client = None
nickname = None
password = None
stop_thread = False


def enter_server():
    global nickname
    global password
    global client

    server_ip = simpledialog.askstring("Server IP", "Enter the server IP address:")
    server_port = simpledialog.askinteger("Server Port", "Enter the server port number:")
    nickname = simpledialog.askstring("Nickname", "Choose Your Nickname:")

    if nickname == 'admin':
        password = simpledialog.askstring("Password", "Enter Password for Admin:", show='*')

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))


def receive():
    global stop_thread
    while True:
        if stop_thread:
            break
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
                next_message = client.recv(1024).decode('ascii')
                if next_message == 'PASS':
                    client.send(password.encode('ascii'))
                    if client.recv(1024).decode('ascii') == 'REFUSE':
                        print("Connection is Refused !! Wrong Password")
                        stop_thread = True
                elif next_message == 'BAN':
                    print('Connection Refused due to Ban')
                    client.close()
                    stop_thread = True
            else:
                chat_area.config(state=tk.NORMAL)
                chat_area.insert(tk.END, message + '\n')
                chat_area.yview(tk.END)
                chat_area.config(state=tk.DISABLED)
        except socket.error:
            print('Error Occurred while Connecting')
            client.close()
            break


def write():
    global stop_thread
    while True:
        if stop_thread:
            break


def send_message(event=None):
    message = f'{nickname}: {message_entry.get()}'
    if message[len(nickname) + 2:].startswith('/'):
        if nickname == 'admin':
            if message[len(nickname) + 2:].startswith('/kick'):
                client.send(f'KICK {message[len(nickname) + 2 + 6:]}'.encode('ascii'))
            elif message[len(nickname) + 2:].startswith('/ban'):
                client.send(f'BAN {message[len(nickname) + 2 + 5:]}'.encode('ascii'))
        else:
            chat_area.config(state=tk.NORMAL)
            chat_area.insert(tk.END, "Commands can be executed by Admins only !!\n")
            chat_area.yview(tk.END)
            chat_area.config(state=tk.DISABLED)
    else:
        client.send(message.encode('ascii'))
    message_entry.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Chat Client")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_area.pack(padx=20, pady=5)

message_entry = tk.Entry(root, width=80)
message_entry.pack(padx=20, pady=5)
message_entry.bind("<Return>", send_message)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Prompt the user to enter the server
enter_server()

# Start the receive and write threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

root.mainloop()