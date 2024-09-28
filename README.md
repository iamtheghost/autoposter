# Easy Python Autoposter

    This is a quick script to illustrate a proof of concept for automatically posting content into Facebook groups can be achieved using Selenium WebDriver and Python. This is a simple script I wrote in a few minutes just to illustrate the possibilities.

# Index
 - [About](#about)
 - [Potential Usecases](#potential-usecases)
 - [Prerequisites](#prerequisites)
 - [Getting Started](#getting-started)
 - [Future Considerations]

## About

This is a single-file script (with an .env for credentials) that illustrates how to automate posting to Facebook using the Selenium WebDriver library and Python. The implications of this script are to illustrate how "[botting](https://en.wikipedia.org/wiki/Botting)" is a legitimate concern on the web — particularly for small e-commerce businesses selling limited but high-demand products, fledgling social media platforms, and similar user-driven web applications.

This simple script illustrates how to do something benign while simultaneously revealing how *easy* it is to automate things on the web and circumvent rudimentary human-only safeguards. This script posts YouTube links to FB Groups, but can be easily adjusted with minimal Python and Selenium experience to do a number of nefarious things.

## Potential Usecases
- Auto-purchase high-demand products for resale.
- Perform marketing tasks from "legitmate" user accounts without relying on platform marketing tools.
- Spam.
- Steer public opinion through information dissemination.

## Prerequisites
- [Python 3+](https://www.python.org/downloads/macos/)
- [Selenium](https://selenium-python.readthedocs.io/)
- Appropriate browser/webdriver (e.g. [ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads))
- Python [DotEnv](https://pypi.org/project/python-dotenv/) for managing credentials in env files
- An imagination (optional but helpful)

## Getting started
1. Install Python 3+, Selenium, and the Python DotEnv plugin and download the appropriate webdriver for your browser of choice (Chrome is easiest to manipulate)
2. Your login credentials must be saved in your browser of choice and you must have enabled "Keep me logged in", "Log me in automatically from now on", or similar login options in order for the script to operator smoothly.
3. Open `fb-group-poster.py` and `.env` in your text editor
4. Populate the `.env` with your FB login credentials
5. Fill out the various arrays in the script with your target groups and content
6. Run the script with `python3 fb-group-poster.py`

## Future Considerations
I'm omitting how to set this script up to run automatically, but it can easily be achieved using something like [Schedule](https://schedule.readthedocs.io/en/stable/) or [Cron](https://wiki.archlinux.org/title/Cron).

This can be adapted for other social media platforms fairly easily. The script is targetting the FB post box element using `driver.find_element(By.XPATH,"//*[text()='Write something...']")`, but you can easily adapt that to be the YouTube Comment box, the Twitter post box, or anything on another platform.

Happy hacking 💻.