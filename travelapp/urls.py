from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('travelapp/destination', views.destination, name='destination'),
    path('travelapp/search',SearchView.as_view(), name='search'),
    path('travelapp/search/nearbyplaces', views.nearbyplaces, name='nearbyplaces'),
    path('travelapp/search/similarplaces', views.similar_places, name='nearbyplaces'),
    path('travelapp/search/destination', views.destination, name='destination'),
    path('travelapp/yourlocation', views.nearbyplacesyourlocation, name='nearbyplacesonlocation'),
]

