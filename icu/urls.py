
from django.contrib import admin
from django.urls import path
from opd import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.country_search,name = 'country_search'),
    path('corona/',views.corona,name = 'corona'),
    path('corona/statewise/',views.statewise_status,name = 'statewise'),
    path('transmission/',views.transmission,name="transmission"),
    path('precaution/',views.precaution,name="precaution"),


]
