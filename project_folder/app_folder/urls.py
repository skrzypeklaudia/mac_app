
from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.person_list),
    path('persons/<int:pk>/', views.person_detail),
    path('osoby/', views.osoba_list),
    path('osoby/<int:pk>/', views.osoba_details),
    path('osoby/search/<str:substring>/', views.osoba_search),
    path('stanowiska/', views.stanowisko_list),
    path('stanowiska/<int:pk>/', views.stanowisko_detail),
    path('welcome/', views.welcome_view),
    path('persons_html/', views.person_list_html),
    path("persons_html/<int:id>/", views.person_detail_html),
]