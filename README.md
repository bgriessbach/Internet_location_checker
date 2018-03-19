# Internet Location Checker

This webapp allows the user to input a UK postcode and receive a tabulary overview of availablilties and average speeds.

## Installation: 
Currently, this webapp is not hosted online yet. 
In order to use it locally, please do the following:
1. Download the repository (https://github.com/bgriessbach/Internet_location_checker.git)  
2. Make sure Python 3 is available for the repository. (https://www.python.org/about/gettingstarted/)  
3. For a stable build and to avoid dependency conflicts, please use a Virtual Environment to install dependencies and run the project. (for example https://docs.python.org/3/tutorial/venv.html)  
4. Install the following dependencies:
  * flask (http://flask.pocoo.org/)
  * requests (http://docs.python-requests.org/en/master/user/install/#install)  
5. This project uses an external config file to get the path and base file name for the csvs needed. I have uploaded the files to an S3 bucket.
Please create a config.ini file on the app folder level with the following content:
```
[DEFAULT]
DATAPATH = https://s3.eu-west-2.amazonaws.com/internet-speed-data-ofcom/
FILEPREFIX = 2016_fixed_pc_r01_
```
## Setup
After the successful installation:
1. Start the Virtual Environment and navigate to the root folder of the project. 
2. Run "export FLASK_APP=main.py" (MAC) or "set FLASK_APP=main.py" (Windows)
3. Run "flask run"


## Dependencies used:
* Flask
* Python 3
* Bootstrap
* Request


## Current Status:
* Setup basic flask environmemnt
* added bootstrap
* added basic csv functionality
* add basic visualisation

## Next:
* add Error Handling
* possibly add different visualisation
