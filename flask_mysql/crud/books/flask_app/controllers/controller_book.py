import re
from flask_app import app, bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models import model_user, model_sighting
import datetime