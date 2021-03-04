# Importing Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

def scrape():
    browser = init_browser()

    # NASA Mars News
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    news_title_scrape = soup.find_all('div',class_='content_title')
    news_title = news_title_scrape[1].text
    news_title

    news_p_scrape = soup.find_all('div',class_='article_teaser_body')
    news_p = news_p_scrape[0].text
    news_p 

    # JPL Mars Space Images - Featured Image
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    featured_image_scrape = soup.find_all("img", class_="headerimage fade-in")[0]["src"]
    image_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/"
    featured_image_url = image_url + featured_image_scrape
    featured_image_url

    # Mars Facts
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    mars_table = tables[0]
    mars_table 

    mars_table.rename(columns={0 : "Variable", 1 : "Measure"})
    mars_table = mars_table.to_html(classes="table table-striped")

#     # # Mars Hemispheres
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")
 #   cerberus_image = soup.find("img", class_="wide-image")["src"]
    cerberus_image = "/cache/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"
    cerberus_image = "https://astrogeology.usgs.gov" + cerberus_image
    cerberus_title = soup.find("h2", class_="title").text

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    schiaparelli_image = soup.find("img", class_="wide-image")["src"]
    schiaparelli_image = "https://astrogeology.usgs.gov" + schiaparelli_image
    schiaparelli_title = soup.find("h2", class_="title").text

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    syrtis_image = soup.find("img", class_="wide-image")["src"]
    syrtis_image = "https://astrogeology.usgs.gov" + syrtis_image
    syrtis_title = soup.find("h2", class_="title").text

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)

    html = browser.html
    soup = bs(html, "html.parser")

    valles_image = soup.find("img", class_="wide-image")["src"]
    valles_image = "https://astrogeology.usgs.gov" + valles_image
    valles_title = soup.find("h2", class_="title").text

    hemisphere_image_urls = [
                        {"title": cerberus_title, "img_url": cerberus_image},
                        {"title": schiaparelli_title, "img_url": schiaparelli_image},
                        {"title": syrtis_title, "img_url": syrtis_image},
                        {"title": valles_title, "img_url": valles_image}]

    scraped_data = { "news_title": news_title, 
                    "news_para": news_p,
                    "featured_image_url": featured_image_url,
                    "mars_table": mars_table,
                    "hemisphere_image_urls": hemisphere_image_urls
    }
    browser.quit()
    
    return scraped_data