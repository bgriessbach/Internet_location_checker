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

## Decisions:
* Multiple datasets on https://www.ofcom.org.uk/research-and-data/multi-sector-research/infrastructure-research/connected-nations-2016/downloads. 
* I decided to use Postcode centric lookup because it provides a more localized result then City Name Lookup.
* from the csv files, I use the download and upload speed average/min/max data for the first table. It will provide the technicians with the opportunity to show the current possibilities in the area. 
* for the second table, I settled on the availability of certain technologuies and line speeds in the area.
* Because the user may input only part of a postcode, the resuling tables can become quite large. I am limiting the output to 50 lines per table to keep loading times low. 
* In terms of fameworks, I have decided on Flask because it is quick to setup and satisfies the MVP of this task.
* For styling I used bootstrap so the interface is adaptive to different monitor/window sizes. 
* For endpoints, I decided that in essence 2 pages, 1 for input and 1 for output were enough to acchieve NVP.
* In order to keep the interaction in the user as smooth and easy as possible, most errors from faulty input to HTTP errors will redirect the user to the input page and show an explaination for the behaviour. 
* I uploaded the csvs to a public S3 bucket, in order to keep the package size of the website down. On the original page, the csvs are zipped, which would complicate reading specific csvs directly. 
* I decided to outsource the path to the csvs to an ini file. This means the path can be changed or updated without having to update the code base. 

## Current Status:
* Setup basic flask environmemnt
* added bootstrap
* added basic csv functionality
* add basic visualisation
* added return button and error handling
* tested successfully in latest Chrome, FF, Opera

## Known Limitation:
* IE and MEdge currently have issues displaying table scrolls properly. Please use Chrome, Firefox, Opera or Safari. 


