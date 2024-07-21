from django.urls import path
from .views import HomeView, ProductListView, CategoryDetailView, ProductAddView
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('products/', ProductListView.as_view(), name='products_page'),
    path('product_add/', ProductAddView.as_view(), name='products_add_page'),
    path('category-detail/<int:pk>', CategoryDetailView.as_view(), name='category_detail_page'),
    path('old-url/', RedirectView.as_view(url='/new-url/'), name='redirect-to-new-url'),
    ]