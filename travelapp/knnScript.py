import numpy as np
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import geocoder


def getNearLocation(data=None):
    df = pd.read_excel('kathmandu.xlsx')


    location = df[['Latitude', 'Longitude']]

    arrayLocation = np.array(location)
    listlocation = location.values.tolist()

    # training the knn with the xy coordinates
    knn = NearestNeighbors(n_neighbors=6)
    knn.fit(arrayLocation)

    # distances, indices = knn.kneighbors(xy_coordinates)
    # finding the nearest point for a given coordinate
    if data == "self":
        my_location = geocoder.ip('me')
        userlocation = my_location.latlng
        userlocation = [27.767881, 85.290988]
    else:
        my_location = data
        userlocation = data

    userlocation = np.array([[userlocation[0], userlocation[1]]])
    distances, indices = knn.kneighbors(userlocation)
    print(distances, indices)
    indicetolist = indices.tolist()
    location_dict = {}
    for i in indicetolist[0]:
        location_dict[(df.loc[(df['Latitude'] == listlocation[i][0]) & (
            df['Longitude'] == listlocation[i][1]), 'Name']).values[0]] = listlocation[i]
        print("Location:", (df.loc[(df['Latitude'] == listlocation[i][0]) & (df['Longitude'] == listlocation[i][1]), 'Name']).values[0])
        print("cordinate:", listlocation[i])

    print(location_dict)
    return location_dict


def getNearLocation_withcatagory(places,data="self"):

    for i in places:
        a=i.name
    print("hello")
    print(a)

    df = pd.read_excel('kathmandu.xlsx')
    df_of_place=df[(df["Name"]==a)]
    print(df_of_place)
    print(df_of_place.values.tolist()[0][-1])
    #input("hello")

    b=df[df["Category"]==df_of_place.values.tolist()[0][-1]]

    location = b[['Latitude', 'Longitude']]

    print(len(location))
    print(location)
    arrayLocation = np.array(location)
    listlocation = location.values.tolist()

    # training the knn with the xy coordinates
    knn = NearestNeighbors(n_neighbors=6)
    knn.fit(arrayLocation)

    # distances, indices = knn.kneighbors(xy_coordinates)
    # finding the nearest point for a given coordinate
    if data == "self":
        my_location = geocoder.ip('me')
        userlocation = my_location.latlng
        userlocation = [27.767881, 85.290988]
    else:
        my_location = data
        userlocation = data

    userlocation = np.array([[userlocation[0], userlocation[1]]])
    distances, indices = knn.kneighbors(userlocation)
    print(distances, indices)
    indicetolist = indices.tolist()
    location_dict = {}
    for i in indicetolist[0]:
        location_dict[(df.loc[(df['Latitude'] == listlocation[i][0]) & (
            df['Longitude'] == listlocation[i][1]), 'Name']).values[0]] = listlocation[i]
        print("Location:", (df.loc[(df['Latitude'] == listlocation[i][0]) & (df['Longitude'] == listlocation[i][1]), 'Name']).values[0])
        print("cordinate:", listlocation[i])

    return location_dict