# weatherpy
Command line utility for fetching weather information from https://openweathermap.org

# How to use
1. Go to [Open Weather](https://home.openweathermap.org/users/sign_up) and sign up for a new API key
1. Clone the repo
1. Open ``` API.py``` and insert your API key
1. Insert your city name and [ISO-3166](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) country code
1. Now simply run ```main.py```

# Requirements
Python 3.6 or higher
# Running the application

```bash
git clone https://github.com/mirajus-salehin/weatherpy.git
cd weatherpy
python main.py
```
# Adding to command line
Add this line to your ```.bashrc``` or ```.zshrc``` file

```bash
export WEATHERPY_API_KEY="<YOUR_API_KEY>"
export WEATHERPY_COUNTRY_CODE="<COUNTRY_CODE"
export WEATHERPY_CITY_NAME="<CITY_NAME>"
export WEATHERPY_UNITS="metric"

alias weatherpy='cd <YOUR_CLONED_DIRECTORY> && python main.py'
```
After this open your terminal and type ```weatherpy```