from flask import Flask, render_template, redirect
import scrape_mars
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():
    mars_data = scrape_mars.scrape_info()
    return render_template("index.html", data=mars_data)
@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape_info()
    mongo.db.collection.update({}, mars_data, upsert=True)
    print(mars_data)
    return redirect("/", 302)
if __name__ == "__main__":
    app.run(debug=True)



