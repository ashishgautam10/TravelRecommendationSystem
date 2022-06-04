import numpy as np
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import requests
import json

def getNearLocation():
    df = pd.read_excel('kathmandu.xlsx')

