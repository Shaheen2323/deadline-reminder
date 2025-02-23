# Author: Shaheen Pedram
# Date: 02/22/2025
# Project: Deadline Reminder (Test Program)
# Description: Send 'retrieve', 'set', 'update', or 'delete' requests to the microservice for testing.

import zmq   # ZeroMQ (for communicating with the server)
import json  # for 'dumps'

# function for printing an error message in case of invalid input
def print_error():
    print("\nError! Invalid input. Try again.")

def print_menu():
    print("\nWhat would you like to do?\n")
    print("1. Get Deadline Reminders")
    print("2. Add a Deadline")
    print("3. Update a Deadline")
    print("4. Delete a Deadline")
    print("5. Exit\n")

# start connection
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# print an interactive menu until user quits
while True:
    try:
        print_menu()
        
        # get user choice
        choice = int(input("Choice: "))

        # get all the deadlines
        if choice == 1:
            # the request to be sent the server (no user input needed here)
            request = {"action": "get_deadlines"}

        # add a new deadline
        elif choice == 2:
            # get specific request from the user
            session = input("\nWhat is the deadline/reminder for? ")
            due = input("What's the deadline? ")

            request = {"action": "set_deadline", "session": session, "time": due}

        # update a deadline
        elif choice == 3:
            session = input("\nWhich session would you like to update? ")
            due = input("What's the new deadline? ")

            request = {"action": "update_deadline", "session": session, "time": due}

        # delete a deadline
        elif choice == 4:
            session = input("\nWhich session would you like to delete? ")

            request = {"action": "delete_deadline", "session": session}

        # exit
        elif choice == 5:
            print("\nGoodbye!\n")
            break

        # invalid menu option, so continue looping
        else:
            print_error()
            continue

    # invalid [non-int] input
    except ValueError:
        print_error()
        continue

    # send the request to the server
    print("\nSending request...\n")
    socket.send_json(request)

    # receive info from the server and show it
    reply = socket.recv_json()
    print(json.dumps(reply, indent=4))