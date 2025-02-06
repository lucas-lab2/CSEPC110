clients = []
clients.append("John") #use append to add an element to the end of the list
clients.append("Mary")

print(clients) #['John', 'Mary']

new_client = input("Enter the new client: ") 
clients.append(new_client)
for client in clients:
    print(client) #John, Mary