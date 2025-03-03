# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:42:21 2025

@author: user_name
"""

import zmq
import json



# ZeroMQ Server
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print('Microservice is running...')

while True:

    # Wait for a request from the client
    print('Waiting for request from client...')
    message = socket.recv()
    
    # name of list they want printed to txt
    list_name = message.decode('utf-8')
    
    print('Received request')
    
    # open json file
    json_file = open('shopping_lists.json')
    data = json.load(json_file)
    
    # open txt file
    txt_file = open('list_export.txt', 'w')
    
    list_found = False
    
    # checks if a valid list name was given
    for list in data: 
        
        if list == list_name:
            
            # if they find the list, write it to txt
            list_found = True
            txt_file.write (list_name)
            txt_file.write ('\n\n')
            txt_file.write ('Item          Quantity          Priority\n')

            for item in data[list]:
                txt_file.write (item['item'])
                length = len(item['item'])
                space_length = 15 - length
                for i in range(space_length):
                    txt_file.write (' ')
                txt_file.write (item['quantity'])
                length = len(item['quantity'])
                space_length = 15 - length
                for i in range(space_length):
                    txt_file.write (' ')
                txt_file.write (item['priority'])
                txt_file.write ('\n')
            
    if list_found is False:
        
        # if list name wasnt found, prints out all lists
        for list in data:
            #print name of list
            txt_file.write ('\n')
            txt_file.write (list)
            txt_file.write ('\n\n')
            txt_file.write ('Item          Quantity        Priority\n')
        
            
            for item in data[list]:
                txt_file.write (item['item'])
                length = len(item['item'])
                space_length = 15 - length
                for i in range(space_length):
                    txt_file.write (' ')
                txt_file.write (item['quantity'])
                length = len(item['quantity'])
                space_length = 15 - length
                for i in range(space_length):
                    txt_file.write (' ')
                txt_file.write (item['priority'])
                txt_file.write ('\n')
                
    txt_file.close()
                
    # Send response back to client
    response = "JSON exported successfully."
    socket.send(response.encode("utf-8"))





    


