from django.shortcuts import render
from config.models import *
from django.views.generic.dates import YearArchiveView, TodayArchiveView


# Create your views here.
class ArticleYearArchiveView(YearArchiveView):
    model = Cart
    date_field = 'published_date'
    make_object_list = True
    template_name = 'article_year_archive.html'
    context_object_name = 'articles'
    queryset = Cart.objects.all()


class EventTodayArchiveView(TodayArchiveView):
    model = Cart
    date_field = 'event_date'
    template_name = 'event_today_archive.html'
    context_object_name = 'events'