from flask import Flask, render_template, redirect
import scrape_mars
from flask_pymongo import PyMongo

app = Flask(__name__)

