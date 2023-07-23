from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductDeleteView, ProductUpdateView, \
    contacts, \
    BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView, ResetPassword

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='view'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path("password_reset/generate_password", ResetPassword.as_view(), name="generate_password"),

    path('contacts/', contacts),

    path('blog/', BlogListView.as_view(), name='blogs'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/edit/<slug:slug>', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/<slug:slug>', BlogDetailView.as_view(), name='blog'),
    path('blog/delete/<slug:slug>', BlogDeleteView.as_view(), name='blog_delete'),
]
