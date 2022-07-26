"""pagination URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
# без нее тоже работет
# from stations.views import index ,bus_stations

urlpatterns = [
    path('', include('stations.urls')),

    # работает даже без этих путей и from stations.views import bus_stations
    # path('', index),
    # path('bus_stations/',bus_stations, name='bus-stations' ),
]
