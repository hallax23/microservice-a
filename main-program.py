# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:41:35 2025

@author: user_name
"""

import zmq

# ZeroMQ Client
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Send request
socket.send(b"My Groceries")

# Wait for response
message = socket.recv()
print(f"Response: {message.decode('utf-8')}")
