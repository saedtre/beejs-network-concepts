# Project: A Better Web Server

Guide section: https://beej.us/guide/bgnet0/html/

## Goal
Extend the ch04 HTTP server to serve actual files from a directory.

### Requirements
- Accept a root directory and port as arguments
- Map the request path to a file on disk
- Return the file contents with a `200 OK` response
- Return `404 Not Found` when the file doesn't exist

## Run
```bash
python server.py ./webroot 8080
```
