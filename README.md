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
The message will be "JSON exported successfully.", and as I said you don't need to do anything with the message unless you'd like to. The bulk on information is being put onto the txt file.

[Uploading uml.drawio…]()<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36" version="26.0.11">
  <diagram name="Page-1" id="K5HNMTfDOryTdzJ6RLa1">
    <mxGraphModel dx="1257" dy="528" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="850" pageHeight="1100" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="wIC6l8k4wy8sYrZboMsS-2" value="client" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="60" y="90" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-3" value="server" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="610" y="90" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-4" value="zero mq" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="330" y="90" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-8" value="" style="shape=link;html=1;rounded=0;fillColor=#000000;" edge="1" parent="1">
          <mxGeometry width="100" relative="1" as="geometry">
            <mxPoint x="120" y="190" as="sourcePoint" />
            <mxPoint x="120" y="370" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-9" value="" style="endArrow=none;dashed=1;html=1;dashPattern=1 3;strokeWidth=2;rounded=0;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="120" y="190" as="sourcePoint" />
            <mxPoint x="120" y="150" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-10" value="" style="endArrow=none;dashed=1;html=1;dashPattern=1 3;strokeWidth=2;rounded=0;exitX=0.5;exitY=1;exitDx=0;exitDy=0;" edge="1" parent="1" source="wIC6l8k4wy8sYrZboMsS-3">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="680" y="170" as="sourcePoint" />
            <mxPoint x="670" y="190" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-11" value="" style="shape=link;html=1;rounded=0;fillColor=#000000;" edge="1" parent="1">
          <mxGeometry width="100" relative="1" as="geometry">
            <mxPoint x="669.5" y="190" as="sourcePoint" />
            <mxPoint x="670" y="360" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-12" value="" style="shape=link;html=1;rounded=0;fillColor=#000000;" edge="1" parent="1">
          <mxGeometry width="100" relative="1" as="geometry">
            <mxPoint x="389.5" y="220" as="sourcePoint" />
            <mxPoint x="390" y="360" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-13" value="" style="endArrow=none;dashed=1;html=1;rounded=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" target="wIC6l8k4wy8sYrZboMsS-4">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="390" y="220" as="sourcePoint" />
            <mxPoint x="450" y="240" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-14" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="120" y="230" as="sourcePoint" />
            <mxPoint x="390" y="230" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-15" value="connects to server for request" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="wIC6l8k4wy8sYrZboMsS-14">
          <mxGeometry x="0.2222" y="-4" relative="1" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-16" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="660" y="230" as="sourcePoint" />
            <mxPoint x="390" y="230" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-17" value="connects to server to reply" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="wIC6l8k4wy8sYrZboMsS-16">
          <mxGeometry x="0.3037" y="2" relative="1" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-18" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="120" y="270" as="sourcePoint" />
            <mxPoint x="390" y="270" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-20" value="send request" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="wIC6l8k4wy8sYrZboMsS-18">
          <mxGeometry x="0.3984" y="-1" relative="1" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-19" value="local files" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="810" y="89.99999999999989" width="120" height="60" as="geometry" />
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-21" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="390" y="280" as="sourcePoint" />
            <mxPoint x="670" y="280" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-22" value="request recieved" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="wIC6l8k4wy8sYrZboMsS-21">
          <mxGeometry x="0.1041" y="-3" relative="1" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-23" value="" style="endArrow=none;dashed=1;html=1;rounded=0;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="870" y="260" as="sourcePoint" />
            <mxPoint x="870" y="150" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-24" value="" style="shape=link;html=1;rounded=0;fillColor=#000000;" edge="1" parent="1">
          <mxGeometry width="100" relative="1" as="geometry">
            <mxPoint x="869.47" y="260" as="sourcePoint" />
            <mxPoint x="870" y="320" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-25" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="870" y="290" as="sourcePoint" />
            <mxPoint x="670" y="290" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-26" value="reads json" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="wIC6l8k4wy8sYrZboMsS-25">
          <mxGeometry x="0.3068" y="-1" relative="1" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-27" value="" style="endArrow=none;dashed=1;html=1;dashPattern=1 3;strokeWidth=2;rounded=0;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="680" y="310" as="sourcePoint" />
            <mxPoint x="870" y="310" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-29" value="edits/ creates txt file" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="wIC6l8k4wy8sYrZboMsS-27">
          <mxGeometry x="-0.2981" relative="1" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-28" value="" style="triangle;whiteSpace=wrap;html=1;direction=east;" vertex="1" parent="1">
          <mxGeometry x="860" y="300" width="10" height="10" as="geometry" />
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-30" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="660" y="330" as="sourcePoint" />
            <mxPoint x="390" y="330" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-31" value="send reply message (confirmation)" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="wIC6l8k4wy8sYrZboMsS-30">
          <mxGeometry x="0.276" y="-1" relative="1" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-32" value="" style="endArrow=classic;html=1;rounded=0;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="390" y="350" as="sourcePoint" />
            <mxPoint x="120" y="350" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-33" value="recieves reply message" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];" vertex="1" connectable="0" parent="wIC6l8k4wy8sYrZboMsS-32">
          <mxGeometry x="0.2175" y="4" relative="1" as="geometry">
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="wIC6l8k4wy8sYrZboMsS-34" value="" style="endArrow=none;dashed=1;html=1;rounded=0;" edge="1" parent="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="870" y="360" as="sourcePoint" />
            <mxPoint x="870" y="320" as="targetPoint" />
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>

