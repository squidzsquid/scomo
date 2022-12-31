# README

## Description:
Simple GUI application to retrieve specific data from a user, 
then write the given data to a database (sqlite), and Excel 
sheet and a draft email in Outlook.

## To run:
* Configure any parameters as necessary in config.yaml
* Install requirements as defined in requirements.txt
  ```commandline
  pip install -r requirements.txt

* Launch main.pyw directly from the terminal, i.e.:
    ```commandLine
  python main.pyw
  
## Limitations:
* GUI could obviously look much less basic (and the various 
fields should probably have actual names)
* Add better error handling in case things go wrong when 
writing data etc.
* Writing to database is currently sqlite only -- could 
be extended/adapted to different DB types as necessary