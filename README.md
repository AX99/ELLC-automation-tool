# ELLC Choice Homes Property Automation Tool

This python automation tool logs you into the [East London Lettings Company](www.ellcchoicehomes.org.uk/) website
using the credentials in the [Secrets.py](Secrets.py) file. (You must have an account for this to work)

## Usage

### Config
The [Secrets.py](Secrets.py) file contains the login credentials.
Enter the following:  
    - 6 digit username  
    - Date of birth

### Running the tool
1. Open the file directory in your command shell
2. Create and activate a virtual environment.
2. Run the following to install dependencies:
   - `pip install -r requirements.txt`
3. Run the following to run the app:
   - `python3 main.py`
   (Your browser may ask you to allow connections, click yes/allow)
