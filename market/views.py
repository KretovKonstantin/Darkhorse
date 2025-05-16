from django.http import Http404
from django.views.generic import DetailView, ListView
from django.db.models import Q

from market.models import Products
from market.utils import q_search


class CatalogView(ListView):
    model = Products
    
    template_name = "market/catalog.html"
    context_object_name = "market"
    paginate_by = 12
    allow_empty = True
    
    slug_url_kwarg = "category_slug"

    def get_queryset(self):
        category_slug = self.kwargs.get(self.slug_url_kwarg)
        on_sale = self.request.GET.get("on_sale")
        order_by = self.request.GET.get("order_by")
        query = self.request.GET.get("q")

        market = super().get_queryset()

        if category_slug and category_slug != "all":
            market = market.filter(category__slug=category_slug)

        if query:
            # query = query.capitalize()
            market = market.filter(Q(name__icontains=query) | Q(description__icontains=query))

        if on_sale:
            market = market.filter(discount__gt=0)

        if order_by and order_by != "default":
            market = market.order_by(order_by)

        if not market.exists():
            raise Http404("Продукты не найдены.")

        return market

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Dark horse - Каталог"
        context["slug_url"] = self.kwargs.get(self.slug_url_kwarg)
        return context


class ProductView(DetailView):
    template_name = "market/product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_object(self, queryset=None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        return context


