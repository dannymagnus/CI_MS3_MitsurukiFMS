# Mitsuruki - FMS (Fleet Management System)
(Developer: Daniel Richards)

![Mockup FMS](docs/mockup/mockup.png)

[View live site](https://dannymagnus.github.io/CI_MS3_Mitsuruki_FMS/)

## Table of Content

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Stories](#user-stories)
3. [Technical Design](#technical-design)
    1. [Flowchart](#flowchart)
    2. [Data Models](#data-models)   
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
5. [Features](#features)
6. [Testing](#validation)
    1. [Python Validation](#Python-validation)
    2. [Testing user stories](#testing-user-stories)
8. [Bugs](#Bugs)
10. [Deployment](#deployment)
11. [Credits](#credits)
12. [Acknowledgements](#acknowledgements)

## Project Goals 

- The Fleet Management System is the beginning of a real world application for an automotive company engineering company. Mitsuruki has been used as a fictional as not to infringe any brand or copyright.

### User Goals
- Be able to search vehicles from an automotive engineering fleet to pick vehicles with feature fitments I wish to assess.
- Add appraisals to the database.
- Read previous appraisals of particular vehicles so issues can be raised for engineering investigation.

### Site Owner Goals
- Create an application so that drivers can easily enter vehicle appraisals.
- Create an application that is easy and intuitive to navigate and provide feedback to the user.
- Create an application that gives all appraisal data for a vehicle.

## User Experience

### Target Audience
- Vehicle assessors, engineers and managers.
- Fleet/product engineers.

### User Stories

#### First-time User 
1. As a user I want the option to search vehicles or manage appraisals
2. As a user, I want to be able to to search for a vehicle so I can assess it’s fitment and type.
3. As a user I want to be able to add my appraisal details easily.
4. As a user I want to be able to add vehicles from each of the models to the vehicle database.
5. As a user I want to be able to remove vehicles from the database.
6. As a user I want to be able to search and see appraisals submitted by drivers.
7. As a user I want to be informed if any of my choices are not valid.
8. As a user I want feedback that my choices and actions have been acknowledged and executed.

#### Site Owner
9. As a site owner, I want the user to be able to select a vehicle from the engineering fleet catalogue.
10. As a site owner, I want the fleet details to be synced to and from a google sheet.
11. As a site owner; I want users to be able to submit appraisals which are to be stored in a separate worksheet in the google sheet.
12. As a site owner, I want data entry to be validated, to guide the user on how to correctly format the input.

## Technical Design

### Flow Chart

Below you can see the flowchart, created with [diagrammes.io](www.diagrammes.io)

<details><summary>Flowchart</summary>
<img src=“docs/flowcharts/fms-flowchart">
</details>

### Data models

For this project I have used largely lists, dictionaries and 4 classes for the vehicle lines themselves.
As the programme is working closely with Google Sheets, I have used lists and dictionaries.  List to work with adding data and dictionaries to search for objects within the sheets.
I have used classes for the vehicle lines as some have fitments that others don’t.  Where this is the case, those options are removed from user choice.

## Technologies Used

### Languages
- [Python 3](https://www.python.org/)

### Frameworks & Tools
1. [Git](https://git-scm.com/)
- Git was used for version control within VSCode to push the code to GitHub.
2. [GitHub](https://github.com/)
- GitHub was used as a remote repository to store project code. 
3. [Visual Studio Code (VSCode)](https://code.visualstudio.com/)
VSCode was the IDE used to write the remainder of the project code.
4. [Diagrams.net](https://app.diagrams.net/) - was used to draw flowchart.
5. [Google Sheets](https://www.google.co.uk/sheets/about/) - was used to store data outside of the program.  The vehicle catalogue and appraisal data stored in 2 separate sheets.
6. [Google Cloud Platform](https://cloud.google.com/cloud-console/) - was used to manage access and permissions to the google services, google auth, sheets etc.

## Features

### Main Menu
![Main Menu](docs/features/feature-main-menu.png)

The main menu gives a paragraph welcome and introduction to the Fleet Management System.  It presents the user with 2 options for the Vehicle Catalogue and the Appraisal Menu respectively.

<details><summary>Main Menu</summary>
<img src=“docs/features/main-menu“>
</details>

**This screen covers the following user stories:**

*1. As a user I want the option to search vehicles or manage appraisals*

### Vehicle Menu

The vehicle menu gives the user 3 options where they can search and retrieve vehicle information from a registration giving a description of the vehicle including it’s model type, and fitment of luxury items, in particular in this release, whether heated and/or massage seats are fitted.

<details><summary>Vehicle Menu</summary>
<img src=“docs/features/vehicle-menu“>
</details>

**This screen covers the following user stories:**

*1. As a user I want the option to search vehicles or manage appraisals.*

*7. As a user I want to be informed if any of my choices are not valid.*

*8. As a user I want feedback that my choices and actions have been acknowledged and executed.*

*9. As a site owner, I want the user to be able to select a vehicle from the engineering fleet catalogue.*

*12. As a site owner, I want data entry to be validated, to guide the user on how to correctly format the input.*

#### Search vehicle

This give the user the function of searching the fleet database by registration to return the full vehicle description including any special fitment such as heated or massage seats, so the user can assess the vehicle before booking for an appraisal.  This can also be used by engineers to find the spec of the vehicle after an appraisal.  This function will search vehicles on record and return an error if no such vehicle exists.  It will also validate data entry to a degree (eg. Reg length etc).  It does rely to a degree that the user is in earnest trying to complete entry successfully.  Once located, a prompt will be given to ask if the user wishes to display the data.

<details><summary>Search Vehicle</summary>
<img src=“docs/features/search-vehicle“>
</details>

**This screen covers the following user stories:**

*1. As a user I want the option to search vehicles or manage appraisals*
*2. As a user, I want to be able to to search for a vehicle so I can assess it’s fitment and type.*
*7. As a user I want to be informed if any of my choices are not valid.*
*8. As a user I want feedback that my choices and actions have been acknowledged and executed.*
*9. As a site owner, I want the user to be able to select a vehicle from the engineering fleet catalogue.*
*12. As a site owner, I want data entry to be validated, to guide the user on how to correctly format the input.*

#### Add Vehicle

This give the user the function of adding a vehicle to the fleet database.  The user will be prompted for the key values, registration, model, colour and fitments. If data validation is successful then the user has the option to add the vehicle.

<details><summary>Add vehicle</summary>
<img src=“docs/features/add-vehicle“>
</details>

**This screen covers the following user stories:**

*4. As a user I want to be able to add vehicles from each of the models to the vehicle database.*
*7. As a user I want to be informed if any of my choices are not valid.*
*8. As a user I want feedback that my choices and actions have been acknowledged and executed.*
*9. As a site owner, I want the user to be able to select a vehicle from the engineering fleet catalogue.*
*10. As a site owner, I want the fleet details to be synced to and from a google sheet.*
*12. As a site owner, I want data entry to be validated, to guide the user on how to correctly format the input.*

#### Remove Vehicle

This gives the user the function of removing a vehicle from the fleet database.  The user will be prompted for the key values, registration. If data validation is successful and the vehicle exist in the database, and the user confirms the prompt then the vehicle will be removed.

<details><summary>Remove vehicle</summary>
<img src=“docs/features/remove-vehicle“>
</details>

**This screen covers the following user stories:**

*5. As a user I want to be able to remove vehicles from the database.*
*7. As a user I want to be informed if any of my choices are not valid.*
*8. As a user I want feedback that my choices and actions have been acknowledged and executed.*
*9. As a site owner, I want the user to be able to select a vehicle from the engineering fleet catalogue.*
*10. As a site owner, I want the fleet details to be synced to and from a google sheet.*
*12. As a site owner, I want data entry to be validated, to guide the user on how to correctly format the input.*

### Appraisal Menu

The appraisal menu gives the user 2 options where they can add and search vehicle appraisals.  Drivers/users can submit their experience as an appraisal and then engineers and fleet/vehicle owners can review the data provided and raise issues for engineers to investigate.

<details><summary>Appraisal Menu</summary>
<img src=“docs/features/appraisal-menu“>
</details>

**This screen covers the following user stories:**

*1. As a user I want the option to search vehicles or manage appraisals.*
*3. As a user I want to be able to add my appraisal details easily.*
*7. As a user I want to be informed if any of my choices are not valid.*
*8. As a user I want feedback that my choices and actions have been acknowledged and executed.*
*12. As a site owner, I want data entry to be validated, to guide the user on how to correctly format the input.*

#### Add Appraisal

This give the user the function of adding an appraisal report to the FMS database(google sheet). The user is prompted to enter vehicle registration, and if vehicle exists, date and then the appraisal details.  The user will then have the option to add this report to the database.

<details><summary>Add appraisal</summary>
<img src=“docs/features/add-appraisal“>
</details>

**This screen covers the following user stories:**

*3. As a user I want to be able to add my appraisal details easily.*
*7. As a user I want to be informed if any of my choices are not valid.*
*8. As a user I want feedback that my choices and actions have been acknowledged and executed.*
*11. As a site owner; I want users to be able to submit appraisals which are to be stored in a separate worksheet in the google sheet.*
*12. As a site owner, I want data entry to be validated, to guide the user on how to correctly format the input.*

#### Search Appraisal

This give the user the function of searching an appraisal report to the FMS database(google sheet). The user is prompted to enter vehicle registration, and if vehicle exists the user will issued a prompt which allows them to display all of the appraisals linked to that vehicle.

<details><summary>Search appraisal</summary>
<img src=“docs/features/search-appraisal“>
</details>

**This screen covers the following user stories:**

*3. As a user I want to be able to add my appraisal details easily.*
*7. As a user I want to be informed if any of my choices are not valid.*
*8. As a user I want feedback that my choices and actions have been acknowledged and executed.*
*12. As a site owner, I want data entry to be validated, to guide the user on how to correctly format the input.*
