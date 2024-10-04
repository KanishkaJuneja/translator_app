from django.urls import path
from .views import home, TranslateTextView

urlpatterns = [
    path('', home, name='home'),  # This will match the root URL
    path('api/translate/', TranslateTextView.as_view(), name='translate-text'),
]
