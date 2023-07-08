from django.urls import path
from catalog.views import ProductListView, ProductDetailView, contacts, BlogListView, BlogCreateView, \
    BlogUpdateView, BlogDeleteView, BlogDetailView

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='view'),
    path('contacts/', contacts),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('blog/', BlogListView.as_view(), name='blogs'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/edit/<slug:slug>', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/<slug:slug>', BlogDetailView.as_view(), name='blog'),
    path('blog/delete/<slug:slug>', BlogDeleteView.as_view(), name='blog_delete'),
]
