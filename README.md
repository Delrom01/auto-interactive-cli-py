# auto-interactive-cli-py
Python Library that builds a complete CLI given one or more functions.

Most options are set using introspection/signature and annotation functionality, so very little configuration has to be done.


## Install
1. ```git clone https://github.com/Delrom01/auto-interactive-cli-py.git```
2. ```cd auto-interactive-cli-py```
3. ```pip install .```


## Usage

###### Organisation
In the ```auto-interactive-cli-py``` folder, you will find 
- file ```commands.py``` : who contains all the commands that can be used/launched with the cli
- file ```cli_select_list.py``` : who create a cli with a list of functions to be selected by arrows
- file ```cli_select_input.py``` : who create a cli with a list of functions to be selected by keyboard input 


## Documentation
- questionary -> https://questionary.readthedocs.io/en/stable/
- colorama -> https://pypi.org/project/colorama/
