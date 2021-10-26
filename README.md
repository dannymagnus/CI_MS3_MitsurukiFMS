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
<img src="docs/flowcharts/flowchartfms.png"></details>

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

## Validation

### Python Validation
The Python code of the each module was validated using [PEP8 Validation Service](http://pep8online.com/).  All modules returned a pass with 0 errors and 0 warnings.

<details><summary>run.py</summary>
<img src="docs/validation/python-validation/validation-runpy.png">
</details>

<details><summary>sheet1.py</summary>
<img src="docs/validation/python-validation/validation-sheet1.png">
</details>

<details><summary>vehicles.py</summary>
<img src="docs/validation/python-validation/validation-vehicles.png">
</details>

### Testing user stories

1. As a user I want the option to search vehicles or manage appraisals

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Find main menu       |      Select option 1       | User is presented with Vehicle sub-menu | Works as expected |
| Find main menu  |   Select option 2   | User is presented with Vehicle Appraisals submenu | Works as expected |

<details><summary>Screenshots</summary>
<img src="/docs/testing/user-story-1a.png">
<img src="/docs/testing/user-story-1b.png">
</details>

2. As a user, I want to be able to to search for a vehicle so I can assess it’s fitment and type.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Find Vehicle Menu  |   Select option 1   | Displays input reg | Works as expected |
| Find reg input prompt  |   Enter vehicle registration   | Returns prompt if vehicle exists to display vehicle details OR notifies if reg not found | Works as expected |
| Print vehicle details prompt  |   Select to display vehicle details   | Displays vehicle description | Works as expected |


<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-2a.png">
<img src="docs/testing/user-story-2b.png">
</details>


3. As a user I want to be able to add my appraisal details easily.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Find Appraisals Menu      |      Select option 1      | Prompt appears to enter vehicle registration | Works as expected |
| Enter vehicle registration prompt      |     User enters vehicle reg      |   If vehicle exists user prompted to enter appraisal details OR returns not found | Works as expected |
| Enter appraisal date and details  |  Prompt displayed to update database. |  Confirmation is shown that data has been uploaded  |Works as expected. |
| Update database prompt  |  Select to update OR cancel. |  Database updated with confirmation OR returns to Appraisal Menu  | Works as expected  |

<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-3a.png">
<img src="docs/testing/user-story-3b.png">
<img src="docs/testing/user-story-3c.png">
</details>

4. As a user I want to be able to add vehicles from each of the models to the vehicle database.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  Find Add Vehicle Menu Option     |      Enter vehicle details  |   Confirmation displayed with prompt to add to database | Works as expected |
| Update database prompt | Select to update OR cancel | Database updated with confirmation OR return to menu | Works as expected  |

<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-4a.png">
<img src="docs/testing/user-story-4b.png">
</details>

5. As a user I want to be able to remove vehicles from the database.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  Find Remove Vehicle Menu Option     |      Enter vehicle registration  |   Confirmation displayed with prompt to remove from database | Works as expected |
| Update database prompt | Select to update OR cancel | Database updated with confirmation OR return to menu | Works as expected  |

<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-5a.png">
<img src="docs/testing/user-story-5b.png">
</details>

6. As a user I want to be able to search and see appraisals submitted by drivers.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Search Appraisal Option    |      Enter vehicle registration and confirm prompt if vehicle is located   |  User is presented with all appraisal data for the vehicle selected  | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-6.png">
</details>

7. As a user I want to be informed if any of my choices are not valid.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Vehicle Reg length Validation     |      Enter incorrect reg length     |  Error message displayed with reason and resubmit | Works as expected |
| Menu option validation  |  Enter menu option not within range or non numeric.  |  Error message displayed with reason and resubmit | Works as expected |
| Date validation  |  Enter date incorrect format |  Error message displayed with reason and resubmit | Works as expected |
| Vehicle Reg Validation (not for Add Vehicle Menu option)    |      Enter vehicle registration not contained within Google Sheet     |  Vehicle not found displayed | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-7.png">
</details>

8. As a user I want feedback that my choices and actions have been acknowledged and executed.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|    Find menu options   |      Select menu options   |  User recieves acknowledgement from system  |  Works as expected  | Find vehicle input  |  Input vehicle details  |  User gets acknowledgement from system  |  Works as expected  |

<details><summary>Screenshots</summary>
<img src="docs/testing/user-story-8a.png">
<img src="docs/testing/user-story-8b.png">
</details>


## Deployment

### Heroku

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
2. Create a new app, add app name and your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars, add your sensitive data (creds.json for example)
6. For this project, I set buildpacks to and in that order.
7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
8. Enter your repository name and click on it when it shows below
9. Choose the branch you want to buid your app from
10. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository

### Forking the GitHub Repository 

By forking this GitHub repository you are making a copy of the original to view or make changes without affecting the original. You can do this by following these steps...

1. Log into your GitHub account and find the [repository](https://github.com/dannymagnus/CI_MS3_MitsurukiFMS).
2. Click 'Fork' (last button on the top right of the repository page).
3. You will then have a copy of the repository in your own GitHub account. 

### Making a Local Clone

1. Log into your GitHub account and find the [repository](https://github.com/dannymagnus/CI_MS3_MitsurukiFMS).
2. Click on the 'Code' button (next to 'Add file'). 
3. To clone the repository using HTTPS, under clone with HTTPS, copy the link.
4. Then open Git Bash.
5. Change the current working directory to where you want the cloned directory to be made.
6. In your IDE's terminal type 'git clone' followed by the URL you copied.
7. Press Enter. 
8. Your local clone will now be made.

## Credits

### Code

- **Code Institute** - for git template IDE and heroku deployment instructions.
- **Google** - for library [gspread](https://docs.gspread.org/en/latest/) and [APIS](https://developers.google.com/sheets/api)
- With the exception of the above, all code was written raw and occasional reference to W3C schools for classes. No code has been borrowed from other sources.

### Acknowledgements: 

- To my mentor Mo Shami for his invaluable guidance and direction.
- To the Code Institute online resources
