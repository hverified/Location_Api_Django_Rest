from django.urls import path, re_path
from .views import RegionListAPIView, CountryListAPIView, StateListAPIView, CityListAPIView, LocationListAPIView

urlpatterns = [
    path('location/', RegionListAPIView.as_view(), name="RegionListAPIView"),
    path('location/<region>/', CountryListAPIView.as_view(),
         name="CountryListAPIView"),
    path('location/<region>/<country>/',
         StateListAPIView.as_view(), name="StateListAPIView"),
    path('location/<region>/<country>/<state>/',
         CityListAPIView.as_view(), name="CityListAPIView"),
    path('location/<region>/<country>/<state>/<city>/',
         LocationListAPIView.as_view(), name="LocationListAPIView"),
]
