# How is My Team?
A simple Django application to allow daily checkins and monitoring of your teams happiness.

## Assumptions
1. A user can be part of one or more groups.
2. Statistic is calculated for the current day only.

## API Contract
**Endpoint**: /survey/api/submit  
**Methods Allowed**: POST  
**Body**:
> raw = ```{"happiness_value": number}```  
> Content-type = application/json

**Responses**:

* In case the user is authenticated and submit the rating for the first time on the day  
Status Code: 201(CREATED)
```json
{
    "frequency": {
        "Neutral": 1,
        "Very Happy": 0,
        "Unhappy": 0
    },
    "average": {
        "bts": 3.0,
        "gds": 0.0
    }
}
```

* In case the user is authenticated but already submitted the rating for the day  
Status Code: 400(BAD REQUEST)
```json
{
    "error_code": 1
}
```

* In case the user is authenticated but has given the non-existent happiness value  
Status Code: 400(BAD REQUEST)
```json
{
    "error_code": 2
}
```
* In case the user is unauthenticated then in all cases he/she will get this response  
Status Code: 200(OK)
```json
{
    "frequency": {
        "Neutral": 1,
        "Very Happy": 0,
        "Unhappy": 0
    },
    "average": {
        "all": 3.0
    }
}
```


## Installation instructions
Pre-requisite system installations:
1. Python 3.5
2. SQLite3
3. Virtualenv

The top level directory has 2 files to help install and run the server:
* install.sh
> * Check for pre-requisite system installation.  
> * Creates the virtual environment in the current directory.
> * Install all the requirements from the project into the newly created virtual environment
> * Run the migration needed for the application
> * Create the Happiness Levels for the application
> * Create a super user for the application

* run_server.sh
> * Activate the virtual environment created by install.sh
> * Setup the environment variable needed by the application
> * Run the django Development server

#### To run the project:
1. Deactivate from any current virtual environment
2. Run install.sh using ```./install.sh```
3. Run run_server using ```./run_server.sh```


## Future Improvements
This is a Minimal Viable Product. I would probably take up the following tasks in future interations:
1. Using automated deployment using tools like Ansible
2. Supporting HappinessLevel to also store images corresponding to each happiness level
3. Decouple analytics from the survey collection
4. Support more response types