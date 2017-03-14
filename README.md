# Simple Smart Home Control

This is a small project influenced by an episode of The big Bang Theory series in which they allowed others to control their home electric devicess like light and speakers through the internet.

The device to be controlled is controlled with an arduino uno through a 5v rely which is connected to PIN 8 of the arduino.

turning it on and off is done using USB serial communication using python pyserial library

the server is built using python bottle library which is deplyed locally on local host or local ip on the local network. You can run the server globally by opening the webserver port 80 for your PC on your router and if you have a dynamic IP you can use dynamic DNS service like noip.com