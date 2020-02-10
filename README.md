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

server.py
The server application requires a port and a path to store the files. The server uses 
multiple threads ran as daemons to handle client connections concurrently which is less scalable
and efficient as async input/output but whatever...  


client.py
The client uses a spcified ip and port in addition to a path to a file to send it to the server. The client sends the file
by fragmenting it into a packets with a small size which allows for less network congestion.

