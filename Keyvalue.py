# # Distributed Key Value Store Node
# Client program for Distributed Key Value Store
# This program sends requests to the Flask server

import requests

SERVER = "http://127.0.0.1:5000"

while True:
    print("\n==== Distributed Key Value Store Client ====")
    print("1. Store Key Value (PUT)")
    print("2. Get Value (GET)")
    print("3. Delete Key")
    print("4. Show All Data")
    print("5. Exit")

    choice = input("Enter choice: ")

    # PUT operation
    if choice == "1":
        key = input("Enter key: ")
        value = input("Enter value: ")

        data = {"key": key, "value": value}

        r = requests.post(SERVER + "/put", json=data)
        print("Server Response:", r.json())

    # GET operation
    elif choice == "2":
        key = input("Enter key to search: ")

        r = requests.get(SERVER + "/get/" + key)
        print("Server Response:", r.json())

    # DELETE operation
    elif choice == "3":
        key = input("Enter key to delete: ")

        r = requests.delete(SERVER + "/delete/" + key)
        print("Server Response:", r.json())

    # SHOW ALL
    elif choice == "4":

        r = requests.get(SERVER + "/all")
        print("Database:", r.json())

    elif choice == "5":
        print("Exiting client")
        break

    else:
        print("Invalid choice")


