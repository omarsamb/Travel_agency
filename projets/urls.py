from . import views
from django.urls import path

urlpatterns = [
    #path('',views.index)
    path('excursion/',views.excursion),
    path('voyage/',views.voyage),
    path('destination/',views.destination),
    path('excursion/voyage_detail',views.voyage_detail),
    path('destination/voyage_dest',views.voyage_dest),
    path('destination/ajout_voyage',views.ajout_voyage)

]