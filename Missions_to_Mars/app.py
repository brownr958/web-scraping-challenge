  
#Dependencies
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

#Create an instance ofr Flask app
app = Flask(__name__)

#Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

@app.route("/")
def home():
    scraped_data = mongo.db.scraped_data.find_one()
    return render_template("index.html", mars=scraped_data)

# Scrape Data and pull into Mongo DB
@app.route('/scrape')
def scrape():
    scraped_data = mongo.db.scraped_data
    mars_data = scrape_mars.scrape()
    scraped_data.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)