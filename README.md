ABOUT
=====
The program becomes useful in situations where you are working in an environment without UI. So instead of having to go through the process of configuring the x server, we can expose a paticular folder that contains the data we want to expose. 

The contents of the folder can be viewed over the browser.


REQUIREMENTS
===========

A golang installation in the system.
If not present. Please do 

`sudo apt-get install go`

If not in ubuntu. 
Checkout https://golang.org/doc/install

RUNNING APPLICATION
===================

`go run server.go`

The statement above starts a server instance that runs on port 8080. The instance can be accessed by hitting the ip address that exposes it.

SPOILERS
========

* Firewalls that block 8080 can be a spoiler. 
* Port Number currently hard-quoted in the code. Feel free to change as per your requirements.

* Another server that is already running on the port. 
