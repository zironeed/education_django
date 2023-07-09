from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.forms import inlineformset_factory

from catalog.models import Product, Blog, Version
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from catalog.forms import ProductForm, VersionForm


# Create your views here.
class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Product Information"
        context["product"] = self.get_object()
        product_version = self.get_object()

        context["product_version"] = product_version.active_version
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:view',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Update Product"
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == "POST":
            context["formset"] = SubjectFormset(self.request.POST)
        else:
            context["formset"] = SubjectFormset()
        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Update Product"

        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context["formset"] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context["formset"] = SubjectFormset(instance=self.object)

        return context

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            versions = Version.objects.all()

            for version in versions:
                version.is_published = False
                version.save()

            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:view')


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
        """Перенаправление на обновленный пост"""
        return reverse('catalog:blog', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blogs')
