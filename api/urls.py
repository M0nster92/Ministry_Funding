from django.urls import path
from .views import fundings_list, funding_details, ministry_list, ministry_details

urlpatterns = [
    path('fundings/', fundings_list),
    path('funding/<int:param>', funding_details),
    path('ministry/', ministry_list),
    path('ministry/<str:param>', ministry_details)
]
