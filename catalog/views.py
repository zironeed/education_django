from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify

from catalog.models import Product, Blog
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


# Create your views here.
class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Вам письмо, вот. От {name} ({phone}): \n{message}')
    return render(request, 'catalog/contacts.html')


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        """if is_published == True"""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)

        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        """view count"""
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()

        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview',)
    success_url = reverse_lazy('catalog:blogs')

    def form_valid(self, form):
        """slugify"""
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'preview',)
    #success_url = reverse_lazy('catalog:blogs')

    def form_valid(self, form):
        """slugify"""
        if form.is_valid():
            edited_post = form.save()
            edited_post.slug = slugify(edited_post.title)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:blog', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blogs')
11