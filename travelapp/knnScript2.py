from .models import location
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np

def searchNearPlaces():
    df = pd.read_excel('kathmandu.xlsx')
    location = df[['Latitude ', 'Longitude']]
    arrayLocation = np.array(location)
    listlocation = location.values.tolist()
    
    # training the knn with the xy coordinates
    knn = NearestNeighbors(n_neighbors=4)
    knn.fit(arrayLocation)

