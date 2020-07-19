from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from opd import views
from users import views as user_view
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('alert_zone/', views.alert_zone, name='alert_zone'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('register/',user_view.register, name="register"),
    path('admin/', admin.site.urls),
    path('',views.country_search,name = 'country_search'),
    path('corona/',views.corona,name = 'corona'),
    path('corona/statewise/',views.statewise_status,name = 'statewise'),
    path('transmission/',views.transmission,name="transmission"),
    path('precaution/',views.precaution,name="precaution"),
    path('map/', views.map, name="map"),
    path('profile/',user_view.profile,name = 'profile'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)