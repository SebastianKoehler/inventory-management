# Inventory Management Application

## Description

This application is a simple project to keep track of all incoming/outgoing groceries at home. \
It will hold its own local sqlite database to manage all your supplies.\
Default functions will be inserting, updating, searching and removing products. \
Each product got its own name, amount, BBD and the storage location.\
Later I will add more functionality like receive a notification by email or SMS, \
using this application on your smartphone and maybe a barcode scanner mode.


## Installation

### Virtual environment
#### Windows
```commandline
    To create the virtual environment:
    python -m venv .venv
    
    To activate and use the virtual environment:
    .\.venv\Scripts\activate
    
    To deactivate the virtual environment:
    deactivate
```
#### Linux/ Ubuntu22.04
```shell
    # To create the virtual environment:
    python3 -m venv .venv
    
    # To activate and use the virtual environment:
    source .venv/bin/activate
    
    # To deactivate the virtual environment:
    deactivate
```
---
### Requirements
#### Windows
```bash
    # To create and fill the requirements.txt with all modules/packages:
    pip freeze > requirements.txt
    
    # To install from the requirements.txt file:
    pip install -r requirements.txt
```
#### Linux/ Ubuntu22.04
```shell
    # To create and fill the requirements.txt with all modules/packages:
    pip3 freeze > requirements.txt
    
    # To install from the requirements.txt file:
    pip3 install -r requirements.txt
```
