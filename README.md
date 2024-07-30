# Daily Video Scheduler for Facebook Reels

This project automates the scheduling of daily video posts on a Facebook Business account.

## Features

* Logs in to Facebook Meta Business using credentials stored in a text file.
* Navigates to the Reels Composer page.
* Uploads a video (assumed to be present elsewhere).
* Sets a title and description for the reel based on information in the text file.
* Schedules the reel for a specific date and time (8:00 AM by default).

## Requirements

* Python 3.x
* Selenium WebDriver (install using `pip install selenium`)
* SeleniumBase (install using `pip install seleniumbase`)
* A web browser with WebDriver support (e.g., Chrome, Firefox)

## Setup

1. **Install Libraries:**
```sh
pip install selenium seleniumbase
```
2. **Download WebDriver:**

Download the appropriate WebDriver for your browser from [selenium](https://www.selenium.dev/downloads/).

3. **Place WebDriver:**

Place the downloaded WebDriver executable in a location accessible by your system (e.g., project directory or system PATH).

4. **Create Script.txt:**

Create a text file named `Script.txt` on your Desktop in the following format (one key-value pair per line):

```sh
Email: your_email@example.com
Password: your_password
Name_of_video: Name of your video
Description: Description of video
Start_date: MM/DD/YYYY (format of your starting date)
Time: HH:MM AM/PM (formate of Time)
Last_day_uploaded: Integer (last uploaded day)
Upload_until_day: Integer (day to stop uploading)
```

## Usage

Run the script using:
```sh
python main.py
```

## Notes

* This script uses hardcoded credentials and video paths. Consider using environment variables or a configuration file for improved security and flexibility.
* Automating interactions with Facebook may violate their terms of service. Use this script responsibly and at your own risk.

## Further Development

* Implement error handling for potential issues like login failures or network errors.
* Allow customization of scheduling time and video paths.
* Add support for uploading captions or thumbnails.