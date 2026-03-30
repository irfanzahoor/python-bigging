# try to raise TypeError

a = "This language is fun!"

if not type(a) is int:
    raise TypeError("Only integer numbers are allowed here!")