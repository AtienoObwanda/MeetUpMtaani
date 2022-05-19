##### By FeverCode 
### MeetUp Mtaani

## Table of Content

+ [Description](#description)
+ [Requirements](#requirements)
+ [Installation](#installation)
+ [Running Project](#running-project)
+ [Running Tests](#running-tests)
+ [Project Objectives](#project-objectives)
+ [Behaviour Driven Development(BDD)](#behaviour-driven-development-bdd)
+ [Technologies Used](#technologies-used)
+ [Licence](#licence)
+ [Contributors](#contributors)


## Description
<p>MeetUp Mtaani is a community building webapp which gives people the opportunity to organise groups and host in-person events for people with similar interest at budget friendly rates.</p>

Live link to the project
[MeetUp Mtaani]()

## Requirements
* A computer running on either Windows, MacOS or Ubuntu operating system installed with the following:

```
-Python version 3.9
-Flask
-Pip
-virtualenv
-A text  Editor
```

## Installation
* Open Terminal {Ctrl+Alt+T} on ubuntu
* git clone `https://github.com/AtienoObwanda/MeetUpMtaani`
* cd News-Source
* code . or atom . based on prefered text editor

## Running Project
* On terminal where you have opened the cloned project
    * `python3.8 -m venv --without-pip virtual` - To create virtual enviroment
    * `source venv/bin/activate` - To activate the virtual enviroment
    * `pip install -r requirements.txt` - To install requirements
    * `$ chmod a+x start.sh` - to make the projet executable
    * `$ ./start.sh` - to run the project

## Running Tests
* To run test for the project
    * `$ python3.9 manager.py test`

# Project Objectives:
* The project has a functioning authentication system
* The project contains migration files for the different model structure
* The project has a user model
* The project has a profile page
* The project has a User Dasboard
* Users can edit and delete reservations
* Users can make reservations 

## Behaviour Driven Development (BDD)
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get to the landing page, View Deals, Select between signup and login|
|Select View Deals | **Our Deals**| Get to page with curated MeetUp Mtaani Deals|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with dashboards and view of the landing page|
| Select reserve button | **Reserve** | Form that you input your MeetUp Mtaani deal and reserve details|
| Click on reserve | **Add Reservation** | Saves selected choices to dashboard|
|Select Dasboard | **Active Reservations**| Get reserved spots|
|Click delete icon | **Delete Icon**| Deletes reservation from view|
|Click Edit Button | **Edit Icon**| Get to add reserve form to edit|

 
## Technologies Used
* python3.9
* Flask


## Licence

MIT License

Copyright (c) [2022] [FeverCode]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Contributors

Gedion Onsongo - [https://www.linkedin.com/in/gedion-onsongo-112543210/]

Innoncencia Kakan- [https://www.linkedin.com/in/innoncencia-kakan-28b3a199/]

Maureen Njung'e- [https://www.linkedin.com/in/maureen-njung-e-61b362181/]

Gladys Mwangi- [https://www.linkedin.com/in/gladys-mwangi-a2994088/]

Atieno Obwanda- [https://www.linkedin.com/in/millicent-atieno/]
   


