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
