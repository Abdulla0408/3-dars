from django.urls import path
from .views import new_url_view, ProductDeleteView, ContactFormView
from django.views.generic.base import RedirectView


urlpatterns = [
    path('old-url/', RedirectView.as_view(url='/new-url/'), name='redirect-to-new-url'),
    path('new-url/', new_url_view, name='new-url'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    ]