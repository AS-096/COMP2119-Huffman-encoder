# Run:
```
python hmencoder.py <input_file>
```
# Output:
```
code.txt
encodemsg.txt
```
> *both files ends without skipping a new line

the only escape character that is being handled is "\n", so if "\t" or similar characters appeared, format may not be acurrate since it was not explicitly listed as a requirement. The space character is changed into "Space", though. 

# Enviornment:
This code is only tested on my machine, with Python 3.10.11 on Windows 11 24H2 Build 26120.1542, so pray for it to work on your machine.
