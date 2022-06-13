from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from pols import views
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.landing, name='home' ),
    path('cat/<int:category_id>/' ,views.get_category, name='category'),
    path('register/',views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('search', views.search, name='search'),
    path('tour_book/<int:detail_id>',views.tour_book,name='book'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
