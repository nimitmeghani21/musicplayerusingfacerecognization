import socket

def send_file_request(client_socket):
    filename = input("Enter the filename to transfer: ")
    client_socket.send(filename.encode())
    response = client_socket.recv(1024).decode()
    
    if response == "FILE_FOUND":
        with open("received_" + filename, 'wb') as f:
            data = client_socket.recv(1024)
            while data:
                f.write(data)
                data = client_socket.recv(1024)
        print("File received successfully.")
    else:
        print("File not found on server.")

def perform_calculation(client_socket):
    print("Select operation:")
    print("1. Addition (add)")
    print("2. Subtraction (sub)")
    print("3. Multiplication (mul)")
    print("4. Division (div)")
    
    operation = input("Enter operation: ").lower()
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    client_socket.send(operation.encode())
    client_socket.send(num1.encode())
    client_socket.send(num2.encode())
    
    result = client_socket.recv(1024).decode()
    print("Result:", result)

def start_client():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 8080))
        print("Connected to the server.")
        
        while True:
            print("\nMenu:")
            print("1. Say Hello to Server")
            print("2. File Transfer")
            print("3. Calculator (Arithmetic)")
            print("Type 'exit' to close the connection")
            
            choice = input("Select an option: ")
            client_socket.send(choice.encode())

            if choice == "1":
                message = client_socket.recv(1024).decode()
                print("Server:", message)

            elif choice == "2":
                send_file_request(client_socket)

            elif choice == "3":
                perform_calculation(client_socket)

            elif choice == "exit":
                print("Closing connection...")
                break

            else:
                print(client_socket.recv(1024).decode())

    except ConnectionAbortedError:
        print("Connection aborted by the server.")
    except ConnectionResetError:
        print("Connection reset by peer.")
    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    start_client()
