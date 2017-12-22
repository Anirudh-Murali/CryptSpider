# DataMiningforCrypto

An easy to use data scrapping tool to automate data gathering to help you devise trade stratergies.
All the data is scrapped from the reputed website https://coinmarketcap.com/ . The current version 

# How to use

## Installation
To use the scrapper you need to first install python,pip and all of it's required dependancies
1. Install Python

https://www.python.org/downloads/
Select the version for your OS. 

2. Install pip

https://pip.pypa.io/en/stable/installing/

Once pip has been installed,we can move ahead to install the required dependancies

3.Installing Dependancies
Open a terminal/command promt and run the following commands
  * `pip install pandas`
  * `pip install requests`
  * `pip install json`
  * `pip install BeautifulSoup`
 
 ## Running the script
 
 In the project directory open coins.csv and write the names of the required coins. While doing so,please keep the following points in mind:
 1. Do not open the file using excel. Just open it using a notepad.
 2. Ensure that coins name is in the same format as that mentioned on the url
  https://coinmarketcap.com/currencies/bitcoin-gold/
 for example in this url bitcoin gold is written as bitcoin-gold.
 just keep note of this and no unnecessary errors will pop up.
 3. Open a terminal and run the python script
  * `python data_Scrapper.py`
  
 ## Future version
 
 I plan to incorporate data visualization and also automate coin selection using data science. 
 For more ideas feel free to contribute.
 
 If there are any issues comment and I will look into it.
 Enjoy!
`
