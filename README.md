imple HTTP Calculator

This is a small calculator server made with Python. It uses HTTP requests to add, subtract, multiply, and divide two numbers.

I made this project to practise how a basic HTTP server works in Python. It only uses modules that come with Python, so no extra packages are needed.

## Author

Samuel Hezekiah Epodoi
h.epodoi@alustudent.com


## How to run it

Make sure Python 3 is installed, then open the project folder in a terminal and run:

```bash
python3 server.py
```

The server runs at:

```text
http://localhost:5000
```

Press `Ctrl + C` to stop it.

## How to use it

Enter one of these links in a browser:

```text
http://localhost:5000/add?a=5&b=3
http://localhost:5000/subtract?a=5&b=3
http://localhost:5000/multiply?a=5&b=3
http://localhost:5000/divide?a=5&b=3
```

For example, the add request returns:

```json
{"result": 8.0}
```

The letters `a` and `b` are the two numbers used in the calculation.

## Errors

The server returns an error when:

- `a` or `b` is missing
- A value is not a number
- A number is divided by zero
- The URL does not match an available operation


