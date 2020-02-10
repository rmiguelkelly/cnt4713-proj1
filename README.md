# CNT-4731 Project 1

Template for for FIU CNT-4731 Fall 2019 Project 1

## Makefile

Provides a `clean` target and `tarball` targets to create the submission file

    make clean
    make tarball

You will need to modify the `Makefile` to add your userid for the `.tar.gz` turn-in at the top of the file.

## Academic Integrity Note

You are encouraged to host your code in private repositories on [GitHub](https://github.com/), [GitLab](https://gitlab.com), or other places.  At the same time, you are PROHIBITED to make your code for the class project public during the class or any time after the class.  If you do so, you will be violating academic honestly policy that you have signed, as well as the student code of conduct and be subject to serious sanctions.

## Provided Files

`server.py` and `client.py` are the entry points for the server and client part of the project.

## TODO

###### Ronan M Kelly
###### 5864879
###### Project 1 - Accio

**server.py**
The server application requires a port and a path to store the files. The server uses 
multiple threads ran as daemons to handle client connections concurrently which is less scalable
and efficient as async input/output 

**client.py**
The client uses a spcified ip and port in addition to a path to a file to send it to the server. The client sends the file
by fragmenting it into a packets with a small size which allows for less network congestion.

**Acknowledgement of any online tutorials or code example** 
For the first time in forever, my most helpful source WASN'T stackoverflow. I used the python documentation
especially for sockets and threads and that provided adaquate information for this project. 

**Problems that occured and their solutions**
The actual list of my problems while programming my assignment would span around 100 pages. Before learning python,
all of the languages I used (excpet Javascript) were statically typed and as a result, it is easier to write clean and concise 
code due to knowing the returns and arguments of every function. This dynamic feature of python led me down many wrong paths and
weird errors and it took some time to work with it (And the fact that my computer would run the project fine and correctly but
the gradescope site didn't). On the gradescope site, the client was sending the data fine but the server wasn't processing it/saving it. I learned that because the files were opened and read with the 'wb' option.   