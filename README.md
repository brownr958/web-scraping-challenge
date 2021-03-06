# #web-scraping-challenge

Background
In this assignment, the ask was to build a web application that scrapes various websites for data related to the Mission to Mars and display the information in a single HTML page. The following outlines the steps taken:


Step 1: Scraping
Initial scraping of the following websites was completed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter:

NASA Mars News Site:
The latest news title
The latest news paragraph text

JPL Featured Space Image:
The image url for the current Featured Space image
The title of the current Featured Space image


the Mars facts table: Pandas was used to convert the data to a HTML table string
USGS Astrogeology:

The full-resolution image url of each hemisphere
The title of the hemisphere name
The above two were saved into a Python dictionary

Step 2: MongoDB and Flask Application

MongoDB with Flask templating was used to create a new HTML page that displays all of the information that was scraped from the URLs above. The following tasks were completed:

The Jupyter notebook was converted into a Python script called scrape_mars.py with a function called scrape that executes all of the scraping code from above and returns one Python dictionary containing all of the scraped data.

A root route / was created, that simply displays the current information with a button to begin the initial scraping (index.html).

A route called /scrape was created, that imports the scrape_mars.py script and calls the .scrape() function. This returns a Python dictionary that is stored in Mongo. Splinter's browser has been given a headless value of True so that scraping runs in the background (takes ~40 seconds).



