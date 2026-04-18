# Project: Digging DNS Info

Guide section: https://beej.us/guide/bgnet0/html/

## Goal
Query DNS records for a domain using Python's `socket` and/or the `dig`
command-line tool, then parse and display the results.

### Part A — using `dig` (shell)
```bash
dig example.com A
dig example.com MX
dig -x 93.184.216.34   # reverse lookup
```

### Part B — using Python
Use `socket.getaddrinfo()` and `socket.gethostbyname_ex()` to retrieve
address information for a given hostname.

## Run
```bash
python dig_dns.py example.com
```
