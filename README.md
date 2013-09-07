This is an experiment that I put together to drive the Google Earth browser plugin from Python.
So far this is known to work in Chrome on Windows.  I believe it also works on Mac.  
Unfortunately, the Google Earth plugin does not function on Linux.

To make this work, you will need Python 2.7+, Tornado, and pyzmq.

To run the server, run the following command:

cd src/server
python server.py

Open a web browser and navigate to http://localhost:8888/static/index.html. 
You should be presented with 4 Google Earth plugin panes.

To run the test client:

cd src/test
python console.py

To send a lat/lon, enter a string like this:
&gt; {"lat":40,"lon":-105}

If everything worked, the Google Earth panels should all zoom to a spot somewhere in the middle of Colorado.

To exit the console, use Ctrl-c.
