from django.core.management.base import BaseCommand
from listings.models import Category

class Command(BaseCommand):
    help = 'Populate the database with initial categories'

    def handle(self, *args, **kwargs):
        categories = [
            "Electronics", 
            "Mobile Phones", "Laptops", "Tablets", "Cameras", "Audio & Headphones", "Wearables", "Gaming Consoles",
            "Home Appliances", 
            "Refrigerators", "Washing Machines", "Microwaves", "Air Conditioners", "Vacuum Cleaners",
            "Furniture", 
            "Sofas", "Beds", "Dining Tables", "Chairs", "Wardrobes", "Desks",
            "Vehicles", 
            "Cars", "Motorcycles", "Bicycles", "Trucks",
            "Clothing & Accessories", 
            "Men’s Clothing", "Women’s Clothing", "Children’s Clothing", "Shoes", "Bags & Purses", "Jewelry", "Watches",
            "Sports & Outdoors", 
            "Exercise Equipment", "Outdoor Gear", "Sports Equipment",
            "Books & Media", 
            "Books", "Movies & DVDs", "Music CDs", "Video Games",
            "Toys & Games", 
            "Action Figures", "Board Games", "Dolls", "Educational Toys",
            "Health & Beauty", 
            "Skincare Products", "Haircare Products", "Makeup", "Personal Care Appliances",
            "Baby & Kids", 
            "Baby Gear", "Baby Clothing", "Kids' Furniture", "Toys",
            "Garden & Tools", 
            "Gardening Tools", "Power Tools", "Outdoor Furniture",
            "Office Supplies", 
            "Office Furniture", "Office Equipment", "Supplies",
            "Collectibles & Art", 
            "Antiques", "Paintings", "Sculptures", "Coins", "Stamps",
            "Musical Instruments", 
            "Guitars", "Pianos", "Drums", "Wind Instruments",
            "Pet Supplies", 
            "Pet Food", "Pet Toys", "Pet Accessories",
            "Real Estate", 
            "Houses", "Apartments", "Land", "Commercial Properties",
            "Services", 
            "Home Services", "Automotive Services", "Personal Services",
            "Health & Beauty", 
            "Fitness Equipment", "Health Supplements", "Beauty Treatments",
            "Jewelry & Accessories", 
            "Necklaces", "Bracelets", "Earrings", "Rings"
        ]

        for category_name in categories:
            Category.objects.get_or_create(name=category_name)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated categories'))

