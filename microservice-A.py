# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:42:21 2025

@author: user_name
"""

import zmq
import json

def printBlankSpaces(item_name, txt_file, spaces = 15):
    """ Prints a set of blank spaces to the given text file"""
    space_length = spaces - len(item_name)
    for _ in range(space_length):
        txt_file.write (' ')

def printListHeader(list_name, txt_file):
    """ Prints the List Name and Table Header to the given text file"""
    txt_file.write('\n')
    txt_file.write (list_name)
    txt_file.write ('\n\n')
    txt_file.write ('Item')
    printBlankSpaces('Item', txt_file)
    txt_file.write('Quantity')
    printBlankSpaces('Quantity', txt_file)
    txt_file.write('Priority\n')

def printList(list_data, txt_file):
    """ Prints all the items in the list by  their name, quantity and priority values to the given text file"""
    for item in list_data:
        txt_file.write (item['item'])
        printBlankSpaces(item['item'], txt_file)

        txt_file.write (item['quantity'])
        printBlankSpaces(item['quantity'], txt_file)

        txt_file.write (item['priority'])
        txt_file.write ('\n')


def main():
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
                printListHeader(list_name, txt_file)
                printList(data[list], txt_file)
                break
                
        if list_found is False:
            
            # if list name wasnt found, prints out all lists
            for list in data:
                #print name of list
                printListHeader(list, txt_file)          
                printList(data[list], txt_file)
                    
        txt_file.close()
                    
        # Send response back to client
        response = "JSON exported successfully."
        socket.send(response.encode("utf-8"))


if __name__ == "__main__":
    main()


        


