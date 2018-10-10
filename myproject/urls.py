
from django.urls import path
from myapp import views

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('contact/',views.contact),
    path('aboutus/',views.about_us,name='about'),
    path('count1/',views.count,name='count')
]
