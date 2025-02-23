# Author: Shaheen Pedram
# Date: 02/20/2025
# Project: Deadline Reminder (Server)
# Description: Retrieve, set, update, or delete deadline reminders stored in a JSON file per request from the client.

import zmq   # ZeroMQ (for communicating with the client)
import json  # for 'dumps'

# function for writing/saving deadlines to the file
def write_to_file():
    # open the file and dump everything into it from the 'deadlines' list
    with open('deadlines.json', 'w') as file:
        json.dump(deadlines, file, indent=4)

# function for adding a new deadline
def set_deadline(request):
    # new dictionary entry to ignore "action" and only add "session" and "time"
        new_deadline = {
            "session": request.get("session"),
            "time": request.get("time")
        }

        # append the new deadline to the dictionary
        deadlines.append(new_deadline)
        # save changes to the file
        write_to_file()

        # return a reply message to be sent back to the client
        return {"status": "Deadline added!"}

# function to update an existing deadline
def update_deadline(request):
        # go through the 'deadlines' list to find a match
        for deadline in deadlines:
            # if a match is found, update its "time"
            if deadline["session"] == request.get("session"):
                deadline["time"] = request.get("time")

                write_to_file()

                return {"satus": "Deadline updated!"}

        # session does not exist if here, so send this reply
        return {"status": "Session not found! Nothing was updated."}

# function to delete an existing deadline
def delete_deadline(request):
    for deadline in deadlines:
        # if a match is found, delete it from the 'deadlines' list
        if deadline["session"] == request.get("session"):
            deadlines.remove(deadline)

            write_to_file()

            return {"satus": "Deadline deleted!"}

    return {"status": "Session not found! Nothing was deleted."}

# start connection point
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# open the file for reading
with open('deadlines.json', 'r') as file:
    # if data exists, populate 'deadlines' with data from file
    try:
        deadlines = json.load(file)
    # otherrwise, create a new empty list
    except:
        deadlines = []

# continue waiting for a request from the client FOREVER!!! :(
while True:
    # store the request once received
    request = socket.recv_json()
    print(f"received request: {request}")

    # gather and send all deadlines to the client
    if request.get("action") == "get_deadlines":
        # store what will be sent back into 'reply'
        reply = deadlines
    
    # add a new deadline to the database
    elif request.get("action") == "set_deadline":
        # do the operation and get a reply message
        reply = set_deadline(request)

    # update an existing deadline
    elif request.get("action") == "update_deadline":
        reply = update_deadline(request)

    # delete an existing deadline
    elif request.get("action") == "delete_deadline":
        reply = delete_deadline(request)

    # send back an error message if a request is invalid
    else:
        reply = {"status": "Error! Invalid request."}

    # send a reponse to the client
    socket.send_json(reply)