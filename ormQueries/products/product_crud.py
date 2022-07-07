from .models import Product 
from django.db.models import Q, Avg, Max
from django.db.models.functions import Length


class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all() #query to return all objects

    @classmethod
    def find_by_model(cls, model_name):
        """finds the matching product by model name"""
        return Product.objects.get(model = model_name) #get method to find model 

    @classmethod
    def last_record(cls):
        """finds the last record inserted"""
        return Product.objects.last() #method to get last

    @classmethod
    def by_rating(cls, input_rating):
        """finds products by their rating"""
        return Product.objects.filter(rating = input_rating) #get method to find rating query set

    @classmethod
    def by_rating_range(cls, low, high):
        """finds products within a rating range"""
        return Product.objects.filter(rating__gte = low, rating__lte=high ) #greater than equal, less than equal


    @classmethod
    def by_rating_and_color(cls, input_rating, input_color):
        """finds products by rating & color value"""
        return Product.objects.filter(rating = input_rating, color = input_color) #and

    @classmethod
    def by_rating_or_color(cls, input_rating, input_color):
        """finds products by rating or color value"""
        return Product.objects.filter(Q(rating = input_rating) | Q(color = input_color)) #or need to import Q

    @classmethod
    def no_color_count(cls):
        """returns the count of products that have no color value"""
        return Product.objects.filter(color = None).count()

    @classmethod
    def below_price_or_above_rating(cls, below_price, above_rating):
        """returns products below a price or above a rating"""
        return Product.objects.filter(Q(price_cents__lte =  below_price) | Q(rating__gte = above_rating))

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending(cls):
        """returns products ordered by category alphabetical and decending price"""
        return Product.objects.order_by('category', '-price_cents') # - means decensing

    @classmethod
    def products_by_manufacturer_with_name_like(cls, input_name):
        """returns products made by manufacturers with names containing an input string"""
        return Product.objects.filter(manufacturer__icontains = input_name) #icontains is not case sentitive

    @classmethod
    def manufacturer_names_for_query(cls, input_query):
        """returns a list of manufacturer names that match query"""
        return Product.objects.filter(manufacturer__icontains = input_query).values_list('manufacturer', flat = True) #flat = False returns a list


    @classmethod
    def not_in_a_category(cls,category_name):
        """returns products that are not in a category"""
        return Product.objects.exclude(category = category_name)


    @classmethod
    def limited_not_in_a_category(cls, category_name, limit):
        """returns products that are not in a category up to a limit"""
        return Product.objects.exclude(category = category_name)[:limit] # slice it until limit

    @classmethod
    def category_manufacturers(cls, category_name):
        """returns an array of manufacturers for a category"""
        return Product.objects.filter(category = category_name).values_list('manufacturer', flat = True)

    @classmethod
    def average_category_rating(cls, category_name): 
        """returns the average"""
        return Product.objects.filter(category = category_name).aggregate(Avg('rating'))
        
    @classmethod
    def greatest_price(cls):
        """returns the highest price"""
        return Product.objects.aggregate(Max('price_cents'))
 
    @classmethod
    def longest_model_name(cls):
        """returns the id of the product with the longest model name"""
        return Product.objects.order_by(Length('model').desc()).values_list('id', flat = True)[0]
    
    @classmethod
    def ordered_by_model_length(cls):
        """returns products ordered by the length of their model name"""
        return Product.objects.order_by(Length('model'))
 

