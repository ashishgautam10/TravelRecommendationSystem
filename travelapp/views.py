from django.shortcuts import render, HttpResponse
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from django.contrib import messages
from . import knnScript
from .models import location
from django.views.generic import TemplateView
from .new import apriorialgo


# Create your views here.


def index(request):
    return render(request, 'travelapp/index.html')

def destination(request):
    recommend = knnScript.getNearLocation()
    df = pd.read_excel('kathmandu.xlsx')
    desc = {}
    counter = 0
    for each_place in df["Name"]:
        if each_place in recommend:
            desc[each_place] = df["Description"][counter]
        counter += 1
    return render(request, 'travelapp/destination.html', {"recommend": recommend, "desc": desc})



class SearchView(TemplateView):
    template_name = "travelapp/search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET["search"]
        print(kw)
        print("keyword argument recieved")
# call apriori with arguments as kw
        
        myresults=apriorialgo(kw)
        print(myresults)
        try:
            myresults=[results.strip() for results in myresults]
        except:
            print("no association rules found")

        print(myresults)
        if kw is not None:
            loc = location.objects.filter(name__icontains=kw)
            context["loc"] = loc
            context['data']=myresults
          
            return context
        else:
            pass


def nearbyplaces(request):
    if request.method == "POST":
        placename = request.POST['searchnear']

        places = location.objects.all().filter(name=placename)
        for i in places:
            print(i)
        #input(len(places)) len =1
        for cordinate in places:

            nearCordinate = [cordinate.latitude, cordinate.longitude]# getting the cordinate of the search place
        recommend = knnScript.getNearLocation(nearCordinate)
        #recommend1 = knnScript.getNearLocation_withcatagory(places,nearCordinate)
        #recommend.update(recommend1)


        df = pd.read_excel('kathmandu.xlsx')

        desc = {}
        counter = 0
        for each_place in df["Name"]:
            if each_place in recommend:
                desc[each_place] = df["Description"][counter]
            counter += 1
        ##########################################
        a=[]
        for count,i in enumerate(recommend):
            try:
                print(count)
                l=location.objects.get(name=i)
                b={}
                b["name"]=l.name
                b["img"]=l.img
                a.append(b)
            except:
                pass




        #############################################
        recommend=a

    return render(request, 'travelapp/nearbyplaces.html', {'places': recommend, "desc": desc})




def nearbyplacesyourlocation(request):
    if request.method == "GET":
        latitude = request.GET['latitude']
        longitude = request.GET['longitude']




        nearCordinate = [latitude, longitude]# getting the cordinate of the search place
        recommend = knnScript.getNearLocation(nearCordinate)
        df = pd.read_excel('kathmandu.xlsx')

        desc = {}
        counter = 0
        for each_place in df["Name"]:
            if each_place in recommend:
                desc[each_place] = df["Description"][counter]
            counter += 1

        a=[]
        for count,i in enumerate(recommend):
            try:
                print(count)
                l=location.objects.get(name=i)
                b={}
                b["name"]=l.name
                b["img"]=l.img
                a.append(b)
            except:
                pass




        #############################################
        recommend=a

    return render(request, 'travelapp/nearbyplaces.html', {'places': recommend, "desc": desc})




def similar_places(request):

    if request.method == "POST":
        placename = request.POST['searchnear']

        places = location.objects.all().filter(name=placename)
        for i in places:
            print(i)
        #input(len(places)) len =1
        for cordinate in places:

            nearCordinate = [cordinate.latitude, cordinate.longitude]# getting the cordinate of the search place
        #recommend = knnScript.getNearLocation(nearCordinate)
        try:

            recommend = knnScript.getNearLocation_withcatagory(places,nearCordinate)
        except:
            recommend = knnScript.getNearLocation(nearCordinate)

        #recommend.update(recommend1)



        df = pd.read_excel('kathmandu.xlsx')

        desc = {}
        counter = 0
        for each_place in df["Name"]:
            if each_place in recommend:
                desc[each_place] = df["Description"][counter]
            counter += 1
        ##########################################
        a=[]
        for count,i in enumerate(recommend):
            try:
                print(count)
                l=location.objects.get(name=i)
                b={}
                b["name"]=l.name
                b["img"]=l.img
                a.append(b)
            except:
                pass




        #############################################
        recommend=a

    return render(request, 'travelapp/nearbyplaces.html', {'places': recommend, "desc": desc})

