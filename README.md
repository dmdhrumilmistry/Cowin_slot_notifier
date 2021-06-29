# COWIN SLOT NOTIFIER (CSN)

<i>COWIN SLOT NOTIFIER</i> notifies user about the slots available according to their details entered in <strong>details.txt</strong> file. 
This program can run in the background while you work on your machine and notifies you whenever a slot is available.

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
 
    <img src="https://github.com/dmdhrumilmistry/Cowin_slot_notifier/blob/main/.images/1-details.png" alt="Details.txt"> <br>
    
     ```
    NOTE:
    1. Make sure there's no space between variable and value. It should be in <variable>:<value> format
       eg. i. age_limit:18
          ii. age_limit:45

    2. Enter date in dd-mm-yyyy format, pad date with 0's for single values.
       eg. i. 23-06-2021
          ii. 01-07-2021

    3. Enter delay in seconds.

    4. Enter which dose you want to opt for 1 or 2.
       eg. i. dose:1
          ii. dose:2

    ```
  
 
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
    [5] DOSE : 2
    ```
  - If slots are found
  ```
[*] Total Centers Available:  1
[*] Eligible Centers Count :  1
+-----------+------------------------------+------------------------------------------+-------------------+---------------+---------+------+--------------------+----+----+
| Center ID |             Name             |                 Address                  |        Time       | Min Age Limit | Vaccine | Fee  | Available Capacity | D1 | D2 |
+-----------+------------------------------+------------------------------------------+-------------------+---------------+---------+------+--------------------+----+----+
|   551888  | NAZRETH HIGH SCHOOL B W COVA | Nazreth High School Behind Mbmc Bhy West | 11:00:00-17:00:00 |       18      | COVAXIN | Free |         97         | 0  | 97 |
+-----------+------------------------------+------------------------------------------+-------------------+---------------+---------+------+--------------------+----+----+
[*] Visit https://selfregistration.cowin.gov.in/ to register your slot.
[*] COWIN LINK has been copied to your clipboard. Now open your browser and paste link in URL.
[*] Opening your Default browser...
  ```
   - Notification Image
   
   <img src="https://github.com/dmdhrumilmistry/Cowin_slot_notifier/blob/main/.images/2-notification.png" alt="notification image"> 
   
   
   - Browser Image
   
   <img src="https://github.com/dmdhrumilmistry/Cowin_slot_notifier/blob/main/.images/3-browser.png" alt="browser image"> 
   

 - If no slots are found
 ```
[*] Total Centers Available:  4
[*] Eligible Centers Count :  0
[-] No slots available, according to specified details.
[*] Press Control+C simultaneously to exit.
 ```
 
 - When Control+C is pressed.
```
[-] Keyboard Interrupt Detected! 

[*] Thank You For using COWIN SLOT NOTIFIER...
[*] This program is written by DHRUMIL MISTRY 
```

 ### Dependencies

   **`API SETU COWIN PUBLIC API `** requires following libraries to run properly -
   - `Python`
      - `requests`
      - `prettytable`
      - `win10toast`
      
   - API
      - [COWIN PUBLIC API](https://apisetu.gov.in/public/marketplace/api/cowin)

   > All the dependencies will be installed automatically when you run `pip install -r requirements.txt`
  
   > Tested on Windows10 and Windows7.

### Feel Free to create issue or Pull Requests
If you face any issue or have any ideas do create an issue.
This is an open source software so feel free to pull requests.
  
### Contributions
- Need collaborators for Android and Linux Operating Systems.
- Anyone interested to contribute to this project, fork this repository and make necessary changes and create a pull request.
- Help me to make this documentation better.
- Have any ideas? create an issue.

### Liked this repo and my work
- Leave a star ⭐
- Share with others 

### Support Me on:

  <p align ="left">
    <a href = "https://github.com/dmdhrumilmistry" target="_blank"><img src = "https://img.shields.io/badge/Github-dmdhrumilmistry-333"></a>
    <a href = "https://www.instagram.com/dmdhrumilmistry/" target="_blank"><img src = "https://img.shields.io/badge/Instagram-dmdhrumilmistry-833ab4"></a>
    <a href = "https://twitter.com/dmdhrumilmistry" target="_blank"><img src = "https://img.shields.io/badge/Twitter-dmdhrumilmistry-4078c0"></a><br>
    <a href = "https://dhrumilmistrywrites.blogspot.com/" target="_blank"><img src = "https://img.shields.io/badge/YouTube-Dhrumil%20Mistry-critical"></a>
    <a href = "https://www.youtube.com/channel/UChbjrRvbzgY3BIomUI55XDQ" target="_blank"><img src = "https://img.shields.io/badge/Blog-Dhrumil%20Mistry-bd2c00"></a>
    <a href = "https://www.linkedin.com/in/dhrumil-mistry-312966192/" target="_blank"><img src = "https://img.shields.io/badge/LinkedIn-Dhrumil%20Mistry-4078c0"></a><br>

   </p>
