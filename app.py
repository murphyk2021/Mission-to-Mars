#Use Flask to render a template, redirect to another url, and create a url
#use the scraping code to convert from jupyter notebook to python
from flask import Flask, render_template, redirect, url_for

#use PyMongo to interact with Mongo Database
from flask_pymongo import PyMongo
import scraping 

#Set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#What should we see at our homepage?
@app.route("/")
def index():
   #Use PyMongo to find the "mars" collection in the database (assigned as 'mars')
   mars = mongo.db.mars.find_one()
   #Tell Flask to return an HTML template using index.html, 
   #'mars=mars' tells python to use the 'mars' collection in MongoDB
   return render_template("Challenge_index.html", mars=mars)

#Set up the Scraping Route
@app.route("/scrape")
def scrape():
   #assign mars variable to the mars database data
   mars = mongo.db.mars
   # new variable for scraped data (using spraping.py instructions)
   mars_data = scraping.scrape_all()
   #Add new data to mars (upsert = create new document if one doesnt already exist)
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

if __name__ == "__main__":
    app.run()
