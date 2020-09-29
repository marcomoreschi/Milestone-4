from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Review
from django.db.models.functions import Lower

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    if request.method == "POST":
        rating = int(request.POST["Rating"])
        description = request.POST["Description"]
        product = Product.objects.get(id = product_id)
        author = request.user
        Review.objects.create(rating=rating, description=description, product=product, author=author)

    product = get_object_or_404(Product, pk=product_id)

    ratings = [review.rating for review in product.reviews.all()]

    if len(ratings) == 0:
        avarage = None
    else:
        avarage = sum (ratings) / len(ratings)
        avarage = round(avarage, 1)

    context = {
        'product': product,
        'avarage': avarage,
    }

    return render(request, 'products/product_detail.html', context)
