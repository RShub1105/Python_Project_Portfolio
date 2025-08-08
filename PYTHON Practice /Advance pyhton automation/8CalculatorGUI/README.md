
# 🧮 Calculator GUI App

A simple yet functional calculator built with Python's tkinter library. This desktop application supports basic arithmetic operations and provides a clean, responsive graphical user interface.

## Features

- Simple and intuitive GUI

- Supports:

- Addition

- Subtraction

- Multiplication

- Division

- Clear button to reset input

- Error handling for invalid expressions
## Build With Python
-     Python3.8

-     Tkinter — standard GUI library for Python
## 📂 File Structure

-     calculartor_gui.py
## How Its Work

-  GUI layout is created using tkinter.Entry and tkinter.Button.

-  Button clicks update the input string using the press() function.

- Evaluation is done using Python's eval() wrapped in a try/except block to catch errors.

- 'C' clears the current input, '=' evaluates the expression.


## 📈 Future Improvements

-  Add keyboard support

-  Enhance UI design with themes

-  Support advanced operations (%, square root, parentheses, etc.)

-  Prevent unsafe use of eval() by replacing with a proper math parser


## License

[MIT](https://choosealicense.com/licenses/mit/)

