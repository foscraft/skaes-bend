from flask import Blueprint, render_template, request, redirect, url_for, session
import sqlite3
import re

skae = Blueprint('skae', __name__)

