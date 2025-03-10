# microservice-a
Microservice A implemented for cs 361

# communication contract
This microservice uses zeromq as it's main communication method, and also relays information by writing to a txt file

# requesting data
To request data, you'll have to get the microservice up and running first. To do that, simply run the file in command prompt, and it will say "Waiting for request from client..."
After it's up and running, you'll have to get your main program connected to the same zeromq server, like so:
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
then to request data, simply type out one of these:
socket.send(b"My Groceries")
"My Groceries" should be replaced with whichever list from the JSON file you'd like to be printed, or anything other than a name of a list if you want all lists printed. 

# recieving data
Recieving data is a little more straight forward. 
The lists are printed out to a txt file, of which is in the same directory that the microservice is in. 
While nothing has to be done on your end to make this happen, zeromq needs the client side (main program) to recieve data back after requesting it, even though it won't be used.
To do this, simply add this to the end of your main program:
message = socket.recv()
The message will be a string "JSON exported successfully.", and as I said you don't need to do anything with the message unless you'd like to. The bulk on information is being put onto the txt file, which will be formatted in an organized way. 

![image](https://github.com/user-attachments/assets/7fd62934-39c4-4f97-b3d4-346851b5ff9a)



