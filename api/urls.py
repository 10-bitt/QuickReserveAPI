from django.urls import path
from .views import (
    UserList, UserDetail,
    FacilityList, FacilityDetail,
    ReservationList, ReservationDetail
)

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),

    path('facilities/', FacilityList.as_view()),
    path('facilities/<int:pk>/', FacilityDetail.as_view()),

    path('reservations/', ReservationList.as_view()),
    path('reservations/<int:pk>/', ReservationDetail.as_view()),
]