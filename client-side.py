import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    while True:
        # Get user input for the message to send
        message = input("Enter a message: ")
        
        # Send the message to the server
        client_socket.send(message.encode())
        
        # Receive and display the server's response
        response = client_socket.recv(1024)
        print("Server response:", response.decode())
except KeyboardInterrupt:
    pass
finally:
    # Close the socket
    client_socket.close()
