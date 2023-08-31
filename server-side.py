import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print("Waiting for a connection...")
connection, client_address = server_socket.accept()

try:
    print("Connection established with", client_address)
    
    while True:
        # Receive data from the client
        data = connection.recv(1024)
        if data:
            print("Received:", data.decode())
            
            # Get user input for response
            response = input("Enter a response: ")
            
            # Send the response back to the client
            connection.send(response.encode())
except KeyboardInterrupt:
    pass
finally:
    # Close the connection and socket
    connection.close()
    server_socket.close()
