"""
clients = []
new_client = ""

while new_client != "exit":
    new_client = input("Enter the new client: ")
    if new_client != "exit":
        clients.append(new_client)

    print("The clients are: ")
    for client in clients:
        print(f" {client}")
"""

points_scored = []
new_points = ""
total = 0

while new_points != "exit":
    new_points = input("Enter the points scored: ")
    if new_points != "exit":
        points_scored.append(new_points)

    for points in points_scored:
        total += int(points)
    print(f" {total}")