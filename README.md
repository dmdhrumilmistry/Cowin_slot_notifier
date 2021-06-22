# COWIN SLOT NOTIFIER (CSN)

<i>COWIN SLOT NOTIFIER</i> notifies user about the slots available according to their details entered in <strong>details.txt</strong> file. 


## How to use
  - Install [Python](https://www.python.org/) for your machine.
  - Add python to path.
  - Check if python is properly installed using
    ```
    $ python --version
    ```
  - [Download](https://codeload.github.com/dmdhrumilmistry/Cowin_slot_notifier/zip/refs/heads/main) <strong><i>OR</i></strong> clone the repository
    ```
    $ git clone https://github.com/dmdhrumilmistry/Cowin_slot_notifier.git
    ```
    you'll get something similar below
    ```
    Python 3.9.1
    ```
  - Install requirements using 
    ```
    $ pip install -r requirements.txt
    ```
    
  - Navigate to the cloned repository directory
    ```
    $ cd Cowin_slot_notifier
    ```
    
  - Edit details.txt as per your need.
 
    <img src="https://github.com/dmdhrumilmistry/Cowin_slot_notifier/blob/main/.images/1-details.png?raw=true" alt="Details.txt">
    
  - run the csn.py file using
    ```
    $ python csn.py
    ```
 - now you'll be notified if slots are found.


## TEST RUN (what your output should look like)
  - On Running python file
    ```
    $ python csn.py
    [*] details.txt file found.
    [*] Starting Program.....
    [*] Found following details in details.txt!
    [1] MINIMUM AGE LIMIT : 18
    [2] PINCODE : 401101
    [3] DATE : 22-06-2021
    [4] DELAY (in s): 5
    
    ```
  - If slots are found
    ```
    [*] Total Centers Available:  2
    [*] Eligible Centers Count :  1
    +-----------+------------------------------+------------------------------------------+-------------------+---------------+
    | Center ID |             Name             |                 Address                  |        Time       | Min Age Limit |
    +-----------+------------------------------+------------------------------------------+-------------------+---------------+
    |   551888  | NAZRETH HIGH SCHOOL B W COVA | Nazreth High School Behind Mbmc Bhy West | 11:00:00-17:00:00 |       18      |
    +-----------+------------------------------+------------------------------------------+-------------------+---------------+
    ```
    <img src=" " alt="notification image"> 

 
 ### Dependencies

   **`API SETU COWIN PUBLIC API `** requires following libraries to run properly -
   - `Python`
      - `requests`
      - `prettytable`
      - `win10toast`
      
   - API
      - [COWIN PUBLIC API](https://apisetu.gov.in/public/marketplace/api/cowin)

   > All the dependencies will be installed automatically when you run `pip install -r requirements.txt`
  
  
### Support Me on:

  <p align ="left">
    <a href = "https://github.com/dmdhrumilmistry" target="_blank"><img src = "https://img.shields.io/badge/Github-dmdhrumilmistry-333"></a>
    <a href = "https://www.instagram.com/dmdhrumilmistry/" target="_blank"><img src = "https://img.shields.io/badge/Instagram-dmdhrumilmistry-833ab4"></a>
    <a href = "https://twitter.com/dmdhrumilmistry" target="_blank"><img src = "https://img.shields.io/badge/Twitter-dmdhrumilmistry-4078c0"></a><br>
    <a href = "https://dhrumilmistrywrites.blogspot.com/" target="_blank"><img src = "https://img.shields.io/badge/YouTube-Dhrumil%20Mistry-critical"></a>
    <a href = "https://www.youtube.com/channel/UChbjrRvbzgY3BIomUI55XDQ" target="_blank"><img src = "https://img.shields.io/badge/Blog-Dhrumil%20Mistry-bd2c00"></a>
    <a href = "https://www.linkedin.com/in/dhrumil-mistry-312966192/" target="_blank"><img src = "https://img.shields.io/badge/LinkedIn-Dhrumil%20Mistry-4078c0"></a><br>

   </p>
