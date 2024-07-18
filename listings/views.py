from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing, Category
from .forms import ListingForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def listing_list(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    listings = Listing.objects.all()

    if query:
        listings = listings.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query)
        )

    if category_id:
        listings = listings.filter(category_id=category_id)

    if min_price:
        listings = listings.filter(price__gte=min_price)

    if max_price:
        listings = listings.filter(price__lte=max_price)

    paginator = Paginator(listings, 10)  # Show 10 listings per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Define your general categories here
    general_categories = [
        'Electronics', 'Furniture', 'Home Appliances', 'Vehicles', 'Clothing',
        'Books & Media', 'Sports & Outdoors', 'Toys & Games', 'Collectibles & Art',
        'Beauty & Personal Care', 'Pet Supplies', 'Instruments', 'Jobs & Services',
        'Real Estate', 'Office Supplies', 'Garden & Tools', 'Health & Supplements',
        'Crafts & Hobbies', 'Miscellaneous'
    ]

    return render(request, 'listings/listing_list.html', {
        'page_obj': page_obj,
        'categories': general_categories,
        'query': query,
        'category_id': category_id,
        'min_price': min_price,
        'max_price': max_price,
    })

def home(request):
    categories = Category.objects.order_by('name')  # Order categories alphabetically
    listings = Listing.objects.all()
    return render(request, 'home.html', {'categories': categories, 'listings': listings})

def listing_detail(request, slug):
    listing = get_object_or_404(Listing, slug=slug)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

@login_required
def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.seller = request.user  # Assign the current logged-in user
            listing.save()
            return redirect('listing_detail', slug=listing.slug)
    else:
        form = ListingForm()
    return render(request, 'listings/listing_form.html', {'form': form})

def category_listings(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    listings = Listing.objects.filter(category=category)
    context = {
        'category': category,
        'listings': listings,
    }
    return render(request, 'listings/category_listings.html', context)
