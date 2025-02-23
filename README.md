# Deadline Reminder

Deadline Reminder is a microservice that stores and retrieves deadlines. It can send deadline reminders, add new deadlines, update existing deadlines, or delete existing deadlines.

## Content

- [Setup](#setup)
  - [Requirements](#requirements)
  - [Execution](#execution)
- [Usage](#usage)
  - [Requesting Data](#requesting-data)
  - [Receiving Data](#receiving-data)
- [UML Sequence Diagram](#uml-sequence-diagram)

## Setup

### Requirements

1. You can run this microservice using a terminal or an IDE.
2. Ensure that [Python](https://www.python.org/) 3.12 is installed on your system.
3. This microserice uses ZeroMQ as its communication pipeline. Ensure that [ZeroMQ](https://zeromq.org/download/) is installed on your system.
4. Do not move, change, rename. or delete the "deadlines.json" file without making the necessary changes to "deadline-reminder.py" to accommodate.
5. Ensure the port that is being used by the microservice and ZeroMQ is open/available. If not, use a different port.

### Execution

Run the microservice in your terminal of choice using the following command:

```
python3 deadline-reminder.py
```

In order to stop tje process, use the following keys on your keyboard: Ctrl+C

## Usage

### Requesting Data

Once the microservice is up and running, you can send it requests by connecting to it via ZeroMQ (see the "test-main.py" file for an example).

### Receiving Data



## UML Sequence Diagram

![Screenshot of a UML diagram](readme-assets/uml-sequence-diagram.png)
