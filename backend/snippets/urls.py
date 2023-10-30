from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

# function based
# urlpatterns = [
#     path('snippets/', snippet_list),
#     path('snippets/<int:pk>/', snippet_detail),
# ]

urlpatterns = [
    path('snippets/', SnippetList.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)