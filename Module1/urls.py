from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello1/',hello1,name='hello'),
    path('', newhomepage, name='newhomepage'),
    path('travelpackage/',travelpackage,name='travelpackage'),
    path('print/',console,name='console'),
    path('p/',print1,name="print1"),
    path('randomcall/', randomcall, name='randomcall'),
    path('randomlogic/', randomlogic, name='randomlogic'),
    path('getdate1/',getdate1,name='getdate1'),
    path('get_date/',get_date,name='get_date'),
    path('getregistercall/',getregistercall,name='getregistercall'),
    path('registerloginfunction/',registerloginfunction,name='registerloginfunction'),
    path('piechartcall/', piechartcall, name='piechartcall'),
    path('pie_chart/', pie_chart, name='pie_chart'),
    path('carrentcall/', carrentcall, name='carrentcall'),
    path('weatherpagecall/', weatherpagecall, name='weatherpagecall'),
    path('weatherlogic/',weatherlogic,name='weatherlogic'),
    path('getfeedbackcall/',getfeedbackcall,name='getfeedbackcall'),
    path('contactfunction/', contactfunction, name='contactfunction'),
    path('login/',login,name='login'),
    path('login1/', login1, name='login1'),
    path('signup/',signup,name='signup'),
    path('signup1/', signup1, name='signup1'),
    path('logout/',logout,name='logout'),
    path('logout/', logout, name='logout'),

]