from django.db import models
from django.db import connection
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class Category_ID:
    DRINKS = 1
    BREAKFASTS = 2
    ASIANS = 3
    KIDS = 4
    SNACKS = 5
    DESSERTS = 6

INITIAL_TABLES = ["api_category", "api_product", "api_variant", "api_option"]
INITIAL_CATEGORIES = ["Drinks", "Breakfasts", "Asians", "Kids", "Snacks", "Desserts"]

# INIT - VARIANTS
INITIAL_VARIANTS_TEA = ["Earl Grey", "English", "Peppermint", "Green", "Lemongrass"]
INITIAL_VARIANTS_MILK_SHAKE = ["Chololate", "Strawberry", "Caramel", "Vanilla", "Hazelnut", "Peanut Butter"]
INITIAL_VARIANTS_SMOOTHIES = ["Strawberry", "Banan", "Mixed Berry", "Mango"]
INITIAL_VARIANTS_EGG_YOUR_WAY = ["Poach", "Scrambled", "Boiled", "Sunny"]
INITIAL_VARIANTS_PASTA = ["Bolognese", "Carbonara", "Pesto"]
INITIAL_VARIANTS_DICT = {
    'Tea': {'name': INITIAL_VARIANTS_TEA},
    'Milk Shake': {'name': INITIAL_VARIANTS_MILK_SHAKE},
    'Smoothies': {'name': INITIAL_VARIANTS_SMOOTHIES},
    'Egg Your Way': {'name': INITIAL_VARIANTS_EGG_YOUR_WAY},
    'Pasta': {'name': INITIAL_VARIANTS_PASTA},
}

# INIT - DRINKS #############
INITIAL_PRODUCTS_DRINKS = [
    "Latte", "Flat White", "Cappuccino", 
    "Espresso", "Long Black", "Short", 
    "Mocha", "Matcha", "Chai Latte", 
    "White Coffee", 
    "Macchiato", "Long Macchiato", 
    "Turmeric", 
    "Teh Tarik", 
    "Thai Milk Tea", 
    "Prana Chai Tea", 
    "Tea", # have variant
    "Iced Lemon Tea", 
    "Cola", "Sprite", "Pepsi", 
    "Sparkling Water", 
    "Fresh Juice", 
    "Milk Shake",  # have variant
    "Smoothies" # have variant
]

INITIAL_PRODUCTS_DRINKS_PRICE = [
    0.0, 0.0, 0.0,
    0.0, 0.0, 0.0,
    0.0, 0.0, 0.0,
    0.0,
    0.0, 0.0, 
    0.0,
    0.0, 
    0.0, 
    5.5,
    4.8,
    5.5,
    3.0,
    3.0, 3.0, 3.0, 
    8.0, 0.0, 0.0
]

# INIT - BREAKFASTS #############
INITIAL_PRODUCTS_BREAKFASTS = [
    "Egg Your Way", # have variant
    "Smashed Avo",
    "Egg Benedict",
    "Spicy Scramble Egg",
    "Big Breakfast",
    "Yogurt Bowl",
    "Burger", # have sub (burger_meat)
    "Corn & Zucchini",
    "Caesar Salad", # need addon +chicken $4
    "Garden Salad",
    "Pasta" # have variant
]

INITIAL_PRODUCTS_BREAKFASTS_PRICE = [
    9.0,
    16.9,
    16.9,
    15.8,
    19.8,
    16.0,
    17.8,
    17.8,
    16.0,
    15.0,
    16.0
]

# INIT - ASIANS #############
INITIAL_PRODUCTS_ASIANS = [
    "Nasi Lemak",
    "Roti Canai",
    "Curry Chicken",
    "Butter Chicken",
    "Thai Basil Pork",
    "Maggie Goreng",
    "Curry Laksa",
    "Pepper Salt Chicken",
    "Lemongrass Chicken",
    "Fried Rice Noddles",
    "Village Fired Rice", # have varia
    "Sausage Fired Rice",
    "Bacon Fired Rice",
    "Vegetables Fired Rice"
]

INITIAL_PRODUCTS_ASIANS_PRICE = [
    15.0,
    8.8,
    15.0,
    15.0,
    14.8,
    14.3,
    15.0,
    15.5,
    14.8,
    14.3,
    13.8,
    12.8,
    13.8,
    13.8
]

# INIT - SNACKS #############
INITIAL_PRODUCTS_SNACKS = [
    "Fired Chicken Fillet",
    "Dumpling",
    "Fried Fish Ball",
    "Spring Roll",
    "Nuggets",
    "Chips",
    "Fried Chicken with Chips",
    "Takoyaki",
    "Fried Chicken with House Sauce",
    "Fried Ham Chesses Crumbs"
]

INITIAL_PRODUCTS_SNACKS_PRICE = [
    9.5,
    9.5,
    8.8,
    8.8,
    8.8,
    8.8,
    15.0,
    10.8,
    9.5,
    9.5
]

# INIT - KIDS #############
INITIAL_PRODUCTS_KIDS = [
    "Pancakes",
    "French Toast",
    "Hong Kong Egg Waffle"
]

INITIAL_PRODUCTS_KIDS_PRICE = [
    16.8,
    11.8,
    11.8
]

# INIT - DESSERTS #############
INITIAL_PRODUCTS_DESSERTS = [
    "Nuggets wit Chips",
    "Pancake with Icecream",
    "Hashbrown",
    "Sausage"
]

INITIAL_PRODUCTS_DESSERT_PRICE = [
    12.0,
    11.0,
    8.0,
    9.0,
    8.0
]

# # INIT - SWANDWICHS #############
# INITIAL_PRODUCTS_KIDS = [
#     "Pancakes",
#     "French Toast",
#     "Hong Kong Egg Waffle"
# ]

# INITIAL_PRODUCTS_KID_PRICE = [
#     16.8,
#     11.8,
#     11.8
# ]

# INIT - OPTIONS ################################
TEMPREATURE_NAMES = ["Hot", "Ice", "Extra Hot"]
TEMPREATURE_PRICES = [0.0, 0.0, 0.0] # need to update product price accrodingly
INITIAL_OPTIONS_DRINK_TEMPREATURE = {
    "name": TEMPREATURE_NAMES,
    "price": TEMPREATURE_PRICES,
    "step" : 1
}

SIZE_NAME_KID = "Kid"
# SIZE_KID_PRICE is variant, go to create_option method to change it.
SIZE_NAMES = ["Regular", "Large"]
SIZE_PRICES = [0.0, 0.5]
INITIAL_OPTIONS_DRINK_SIZE = {
    "name": SIZE_NAMES,
    "price": SIZE_PRICES,
    "step" : 2
}

MILK_NAMES = ["Normal", "Lite", "Soy", "Lactose Free", "Almond", "Oat"]
MILK_PRICES = [0.0, 0.0, 0.5, 0.5, 0.5, 0.5, 0.5]
INITIAL_OPTIONS_DRINK_MILK = {
    "name": MILK_NAMES,
    "price": MILK_PRICES,
    "step" : 3
}

BURGER_MEAT_NAMES = ["Chicken", "Beef"]
BURGER_MEAT_PRICES = [0.0, 2.0]
INITIAL_OPTIONS_BREAKFAST_BURGER_MEAT = {
    "name": BURGER_MEAT_NAMES,
    "price": BURGER_MEAT_PRICES,
    "step" : 2
}

FIRERICE_MEAT_NAMES = ["Chicken", "Pork", "Beef"]
FIRERICE_MEAT_PRICES = [0.0, 0.0, 1.0]
INITIAL_OPTIONS_ASIAN_FIRERICE_MEAT = {
    "name": FIRERICE_MEAT_NAMES,
    "price": FIRERICE_MEAT_PRICES,
    "step" : 2
}

# TO BE TESTED / CONFIRM ############## -> possible move to edit session
# options_dict["coffee"] = {
#     "name": ["Normal", "Extra Shot", "Weak", "Decap"],
#     "price": [0.0, 0.0, 0.0], # need to update product price accrodingly
# }
# options_dict["sugar"] = {
#     "name": ["One Sugar", "Two Sugar", "One Equal", "Two Equal"],
#     "price": [0.0, 0.0, 0.0, 0.0]
# }
####################################

# EXCEPTION HANDLING #####################
class Manual_Exception:
    INITIAL_MSG = "Tables just initialized, please run './manage.py migrate'."
    NAME_EXISTS = 1
    NAME_NOT_EXISTS = 2
    ID_EXISTS = 3
    ID_NOT_EXISTS = 4
    INVALID_COMPOSITE_KEY = 5

    def warning_msg(self, code):
        if code == self.NAME_EXISTS:
            return "{0} [Warning] Name already exists.".format(datetime.now().time())
        elif code == self.NAME_NOT_EXISTS:
            return "{0} [Warning] Name not exists.".format(datetime.now().time())
        elif code == self.ID_NOT_EXISTS:
            return "{0} [Warning] ID not exists.".format(datetime.now().time())
        elif code == self.INVALID_COMPOSITE_KEY:
            return "{0} [Warning] Composite key not unique.".format(datetime.now().time())

# QUERY ##################################
class Query:
    def get_product_id_by_name(name):
        product = Product.objects.filter(name=name)
        if product.exists():
            return Product.objects.get(name=name).id
        print(Manual_Exception.warning_msg(Manual_Exception, Manual_Exception.NAME_NOT_EXISTS))
        return None

    def get_products_by_price(price):
        products = Product.objects.filter(price=price)
        if products.exists():
            return products
        else:
            return None

# CATEGORY #############################
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def name_exists(self, tb_name):
        # check unique
        queryset = self.objects.filter(name=tb_name)
        return True if queryset.exists() else False

def create_category(name):
    if not Category.name_exists(Category, name): 
        category = Category(name=name)
        category.save()
    else:
        # category name must be unique
        raise ValueError("Category name: '{0}' already exists.".format(name), {'code': Manual_Exception.NAME_EXISTS})


def create_categories(category_name):
    if isinstance(category_name, list):
        for tb_name in category_name:
            try:
                create_category(tb_name)
            except ValueError as e:
                if e.args[1]['code'] != Manual_Exception.NAME_EXISTS:
                    raise (e)
    elif isinstance(category_name, str):
        try:
            create_category(tb_name)
        except ValueError as e:
            error_code = e.args[1]['code']
            if error_code == Manual_Exception.NAME_EXISTS:
                print(Manual_Exception.warning_msg(Manual_Exception, error_code))
            else:
                raise (e)

class ColorOption(models.TextChoices):
    RED = 'Red', _('Red')
    ORANGE = 'Orange', _('Orange')
    GREEN = 'Green', _('Green')
    BLUE = 'Blue', _('Blue')
    YELLOW = 'Yellow', _('Yellow')
    NORMAL = 'Normal', _('Normal')

# PRODUCT #############################
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    card_color = models.CharField(
        max_length=50,
        choices=ColorOption.choices,
        default=ColorOption.NORMAL,
    )
    image = models.ImageField()

    def name_exists(self, name):
        # check unique
        queryset = self.objects.filter(name=name)
        return True if queryset.exists() else False

def create_product(category_id , name, price):
    if not Product.name_exists(Product, name): 
        product = Product(name=name, price=price)
        product.category_id = category_id
        product.save()
    else:
        # category name must be unique
        raise ValueError("Product name: '{0}' already exists.".format(name), {'code': Manual_Exception.NAME_EXISTS})

def create_products(category_id, name, price):
    products_dict = {}
    products_dict['name'] = name
    products_dict["price"] = price

    if isinstance(products_dict['name'], list):
        for i in range(len(products_dict['name'])):
            name = products_dict['name'][i]
            price = products_dict['price'][i]
            try:
                create_product(category_id, name, price)
            except ValueError as e:
                try:
                    error_code = e.args[1]['code']
                except:
                    raise (e)
                if error_code == Manual_Exception.NAME_EXISTS:
                    print(Manual_Exception.warning_msg(Manual_Exception, error_code))
                else:
                    raise (e)
    elif isinstance(products_dict['name'], str):
        # create user define product
        name = products_dict['name']
        price = products_dict['price']
        try:
            create_product(category_id, name, price)
        except ValueError as e:
            try:
                error_code = e.args[1]['code']
            except:
                raise (e)
            if error_code == Manual_Exception.NAME_EXISTS:
                print(Manual_Exception.warning_msg(Manual_Exception, error_code))
            else:
                raise (e)

# VARIANT ###########################
class Variant(models.Model):
    name = models.CharField(max_length=50, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def name_exists(self, name):
        queryset = self.objects.filter(name=name)
        return True if queryset.exists() else False

def create_variant(product_id, name):
    if product_id is not None:
        if not Variant.name_exists(Variant, name): 
            variant = Variant(name=name)
            variant.product_id = product_id
            variant.save()
        else:
            raise ValueError("Variant name: '{0}' already exists.".format(name), {'code': Manual_Exception.NAME_EXISTS})
    else:
        raise ValueError("Product ID: '{0}' not exists.".format(product_id), {'code': Manual_Exception.ID_NOT_EXISTS})

def create_variants():
    for k, v in INITIAL_VARIANTS_DICT.items():
        for names in v.values():
            for name in names:
                variant = Variant.objects.filter(name=name)
                if not variant.exists():
                    try:
                        create_variant(Query.get_product_id_by_name(k), name)
                    except ValueError as e:
                        try:
                            error_code = e.args[1]['code']
                        except:
                            raise (e)
                        if error_code == Manual_Exception.NAME_EXISTS or error_code == Manual_Exception.ID_NOT_EXISTS:
                            print(Manual_Exception.warning_msg(Manual_Exception, error_code))
                        else:
                            raise (e)


# OPTION ##############################
class Option(models.Model):
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    card_color = models.CharField(
        max_length=50,
        choices=ColorOption.choices,
        default=ColorOption.NORMAL,
    )
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    step = models.IntegerField()
    image = models.ImageField()

    def name_exists(self, name):
        queryset = self.objects.filter(name=name)
        return True if queryset.exists() else False

def create_option(product_id, name, price, step):
    if product_id is not None:
        option = Option.objects.filter(name=name, product_id=product_id)
        if not option.exists(): # composite key
            option = Option(name=name, price=price, step=step)
            option.product_id = product_id
            option.save()
        else:
            print("Product ID: '{0}' and Name '{1}' already exists.".format(product_id, name))
            raise ValueError("Product ID: '{0}' and Name '{1}' already exists.".format(product_id, name), {'code': Manual_Exception.INVALID_COMPOSITE_KEY})
    else:
        raise ValueError("Product ID: '{0}' not exists.".format(product_id), {'code': Manual_Exception.ID_NOT_EXISTS})

def create_tempreature():
    member_counts = [3, 3, 3, 1, 2, 1, 1, 1]
    price_groups = [
        [4.3, 5.5],
        [3.8, 5.0],
        [5.0, 6.5],
        [4.8, 5.5],
        [4.3, 5.5],
        [4.8, 6.5],
        [4.8, 5.5],
        [5.5, 6.5]
    ]
    extra_hot_map = [
        True, True, True,
        False, False, False,
        True, True, True,
        True,
        True, True,
        True,
        True,
        True
    ]

    index = 0
    price_group_index = 0
    for i in member_counts:
        for _ in range(i):
            product_id = Query.get_product_id_by_name(INITIAL_PRODUCTS_DRINKS[index])
            for k in range(len(INITIAL_OPTIONS_DRINK_TEMPREATURE["name"])):
                if k == 2:
                    if extra_hot_map[index] is True:
                        # Extra Hot
                        try:
                            create_option(product_id, INITIAL_OPTIONS_DRINK_TEMPREATURE["name"][k], 0.0, INITIAL_OPTIONS_DRINK_TEMPREATURE["step"])
                        except ValueError as e:
                            try:
                                error_code = e.args[1]['code']
                            except:
                                raise (e)
                            if error_code == Manual_Exception.NAME_EXISTS or error_code == Manual_Exception.INVALID_COMPOSITE_KEY:
                                print(Manual_Exception.warning_msg(Manual_Exception, error_code))
                            else:
                                raise (e)

                else:
                    # Hot, Ice
                    price = price_groups[price_group_index][k]
                    try:
                        create_option(
                            product_id, 
                            INITIAL_OPTIONS_DRINK_TEMPREATURE["name"][k], 
                            price, 
                            INITIAL_OPTIONS_DRINK_TEMPREATURE["step"]
                        )
                    except ValueError as e:
                        try:
                            error_code = e.args[1]['code']
                        except:
                            raise (e)
                        if error_code == Manual_Exception.NAME_EXISTS or error_code == Manual_Exception.INVALID_COMPOSITE_KEY:
                            print(Manual_Exception.warning_msg(Manual_Exception, error_code))
                        else:
                            raise (e)
            index += 1
        price_group_index += 1


def create_size():
    large_size_map = [
        True, True, True,
        False, True, False,
        True, True, True,
        False,
        False, False,
        True,
        False,
        False,
        False,
        False,
        False,
        False, False, False,
        False,
        False,
        False,
        False
    ]

    # exlcuded Milk Shake, Smoothies
    for i in range(len(INITIAL_PRODUCTS_DRINKS) - 2):
        if large_size_map[i] is True:
            # Large
            try:
                create_option(
                    Query.get_product_id_by_name(INITIAL_PRODUCTS_DRINKS[i]), 
                    INITIAL_OPTIONS_DRINK_SIZE["name"][1], 
                    INITIAL_OPTIONS_DRINK_SIZE['price'][1], 
                    INITIAL_OPTIONS_DRINK_SIZE['step']
                )
            except ValueError as e:
                try:
                    error_code = e.args[1]['code']
                except:
                    raise (e)
                if error_code == Manual_Exception.NAME_EXISTS or error_code == Manual_Exception.INVALID_COMPOSITE_KEY:
                    print(Manual_Exception.warning_msg(Manual_Exception, error_code))
                else:
                    raise (e)
        try:
            create_option(
                # Regular
                Query.get_product_id_by_name(INITIAL_PRODUCTS_DRINKS[i]), 
                INITIAL_OPTIONS_DRINK_SIZE["name"][0], 
                INITIAL_OPTIONS_DRINK_SIZE['price'][0], 
                INITIAL_OPTIONS_DRINK_SIZE['step']
            )
        except ValueError as e:
            try:
                error_code = e.args[1]['code']
            except:
                raise (e)
            if error_code == Manual_Exception.NAME_EXISTS or error_code == Manual_Exception.INVALID_COMPOSITE_KEY:
                print(Manual_Exception.warning_msg(Manual_Exception, error_code))
            else:
                raise (e)

    try:
        # Milk Shake
        create_option(
            Query.get_product_id_by_name(INITIAL_PRODUCTS_DRINKS[23]), 
            SIZE_NAME_KID, 
            4.5, 
            INITIAL_OPTIONS_DRINK_SIZE['step']
        )
        create_option(
            Query.get_product_id_by_name(INITIAL_PRODUCTS_DRINKS[23]), 
            SIZE_NAMES[0], # regular
            7.5, 
            INITIAL_OPTIONS_DRINK_SIZE['step']
        )

        # Smoothies
        create_option(
            Query.get_product_id_by_name(INITIAL_PRODUCTS_DRINKS[24]), 
            SIZE_NAME_KID, 
            4.8, 
            INITIAL_OPTIONS_DRINK_SIZE['step']
        )

        create_option(
            Query.get_product_id_by_name(INITIAL_PRODUCTS_DRINKS[24]), 
            SIZE_NAMES[0], 
            8.0, 
            INITIAL_OPTIONS_DRINK_SIZE['step']
        )
    except ValueError as e:
        try:
            error_code = e.args[1]['code']
        except:
            raise (e)
        if error_code == Manual_Exception.NAME_EXISTS or error_code == Manual_Exception.INVALID_COMPOSITE_KEY:
            print(Manual_Exception.warning_msg(Manual_Exception, error_code))
        else:
            raise (e)

def create_milk():
    milk_option_map = [
        True, True, True,
        False, False, False,
        True, True, True,
        False,
        True, True,
        True,
        False,
        False,
        True,
        True,
        True,
        True, True, True,
        True,
        True,
        True,
        True
    ]

    for i in range(len(INITIAL_PRODUCTS_DRINKS)):
        if milk_option_map[i] is True:
            for j in range(len(INITIAL_OPTIONS_DRINK_MILK["name"])):
                try:
                    create_option(
                        Query.get_product_id_by_name(INITIAL_PRODUCTS_DRINKS[i]),
                        INITIAL_OPTIONS_DRINK_MILK["name"][j],
                        INITIAL_OPTIONS_DRINK_MILK["price"][j],
                        INITIAL_OPTIONS_DRINK_MILK["step"]
                    )
                except ValueError as e:
                    try:
                        error_code = e.args[1]['code']
                    except:
                        raise (e)
                    if error_code == Manual_Exception.NAME_EXISTS or error_code == Manual_Exception.INVALID_COMPOSITE_KEY:
                        print(Manual_Exception.warning_msg(Manual_Exception, error_code))
                    else:
                        raise (e)

def create_burger_meat():
    products_name = ["Burger"]
    for product in products_name:
        for i in range(len(INITIAL_OPTIONS_BREAKFAST_BURGER_MEAT["name"])):
            try:
                create_option(
                    Query.get_product_id_by_name(product),
                    INITIAL_OPTIONS_BREAKFAST_BURGER_MEAT["name"][i],
                    INITIAL_OPTIONS_BREAKFAST_BURGER_MEAT["price"][i],
                    INITIAL_OPTIONS_BREAKFAST_BURGER_MEAT["step"]
                )
            except ValueError as e:
                try:
                    error_code = e.args[1]['code']
                except:
                    raise (e)
                if error_code == Manual_Exception.NAME_EXISTS or error_code == Manual_Exception.INVALID_COMPOSITE_KEY:
                    print(Manual_Exception.warning_msg(Manual_Exception, error_code))
                else:
                    raise (e)

def create_firerice_meat():
    products_name = ["Village Fired Rice"]
    for product in products_name:
        for i in range(len(INITIAL_OPTIONS_ASIAN_FIRERICE_MEAT["name"])):
            try:
                create_option(
                    Query.get_product_id_by_name(product),
                    INITIAL_OPTIONS_ASIAN_FIRERICE_MEAT["name"][i],
                    INITIAL_OPTIONS_ASIAN_FIRERICE_MEAT["price"][i],
                    INITIAL_OPTIONS_ASIAN_FIRERICE_MEAT["step"]
                )
            except ValueError as e:
                try:
                    error_code = e.args[1]['code']
                except:
                    raise (e)
                if error_code == Manual_Exception.NAME_EXISTS or error_code == Manual_Exception.INVALID_COMPOSITE_KEY:
                    print(Manual_Exception.warning_msg(Manual_Exception, error_code))
                else:
                    raise (e)

def create_options():
    create_tempreature()
    create_size()
    create_milk()
    create_burger_meat()
    create_firerice_meat()
        

# ADDON #############################
class Addon(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)


def db_table_exists(table_name):
    return table_name in connection.introspection.table_names()

def is_db_initialized():
    for tb_name in INITIAL_TABLES:
        if db_table_exists(tb_name) is False:
            print(Manual_Exception.INITIAL_MSG)
            return True
    return False

# INIT DB
def init_db():
    if is_db_initialized() is True:
        return "DB Already Initialized."
    
    create_categories(category_name=INITIAL_CATEGORIES)
    create_products(category_id=Category_ID.DRINKS, name = INITIAL_PRODUCTS_DRINKS, price = INITIAL_PRODUCTS_DRINKS_PRICE)
    create_products(category_id=Category_ID.BREAKFASTS, name = INITIAL_PRODUCTS_BREAKFASTS, price = INITIAL_PRODUCTS_BREAKFASTS_PRICE)
    create_products(category_id=Category_ID.ASIANS, name = INITIAL_PRODUCTS_ASIANS, price = INITIAL_PRODUCTS_ASIANS_PRICE)
    create_products(category_id=Category_ID.KIDS, name = INITIAL_PRODUCTS_KIDS, price = INITIAL_PRODUCTS_KIDS_PRICE)
    create_products(category_id=Category_ID.SNACKS, name = INITIAL_PRODUCTS_SNACKS, price = INITIAL_PRODUCTS_SNACKS_PRICE)
    create_products(category_id=Category_ID.DESSERTS, name = INITIAL_PRODUCTS_DESSERTS, price = INITIAL_PRODUCTS_DESSERT_PRICE)
    create_variants()
    create_options()
    return "DB Initialization SUCCESS."

