from django.urls import path
from .views import ArticleYearArchiveView, EventTodayArchiveView

urlpatterns = [
    path('articles/<int:year>/', ArticleYearArchiveView.as_view(), name='article-year-archive'),
    path('events/today/', EventTodayArchiveView.as_view(), name='event-today-archive'),
]