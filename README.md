# Just Eat Scraper
### Overview

  This web app scrapes list of restaurants from the https://www.just-eat.co.uk/, and save into Xlsx file.
  * Import Postcodes from xlsx file.
  * Search Restaurant URLs with Postcodes
  * Scrap detail list of restaurants with restaurant URLs
  * Export to xlsx file

###INSTALL
  * install python
  * install pip
     - Download get-pip.py to a folder on your computer.
     - Open a command prompt and navigate to the folder containing get-pip.py.
     - Run the command: python get-pip.py.
  *install requirements.txt
     - Go into project repository in your local.
     - Run the command: pip install -r requirements.txt
### RUN
  Run the following command:
         python main.py
### INPUT
  Postcode districts-modified.xlsx
### OUTPUT
  Restaurants.xlsx
### CLONE
  Run `git clone https://github.com/developer7132/Scraping_Just_Eat.git` to clone the files to your local machine.
  
### PACKAGES USED
 * selenium
 * xlrd
 * XlsxWriter
