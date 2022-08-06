from django.db import models
from django.db import connection
from django.utils.translation import gettext_lazy as _
from datetime import datetime

from pygame import init

INITIAL_TABLES = ["api_category", "api_product", "api_variant", "api_option"]
INITIAL_CATEGORIES = ["Drinks", "Breasfast", "Asian Food", "Kid", "Snack", "Dessert"]
        
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

INITIAL_VARIANTS_TEA = ["Earl Grey", "English", "Peppermint", "Green", "Lemongrass"]
INITIAL_VARIANTS_MILK_SHAKE = ["Chololate", "Strawberry", "Caramel", "Vanilla", "Hazelnut", "Peanut Butter"]
INITIAL_VARIANTS_SMOOTHIES = ["Strawberry", "Banan", "Mixed Berry", "Mango"]
INITIAL_VARIANTS_DICT = {
    'Tea': {'name': INITIAL_VARIANTS_TEA},
    'Milk Shake': {'name': INITIAL_VARIANTS_MILK_SHAKE},
    'Smoothies': {'name': INITIAL_VARIANTS_SMOOTHIES}
}

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


def create_categories(category_name=INITIAL_CATEGORIES):
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

def create_products(category_id=1, name = INITIAL_PRODUCTS_DRINKS, price = INITIAL_PRODUCTS_DRINKS_PRICE):
    products_drinks_dict = {}
    products_drinks_dict['name'] = name
    products_drinks_dict["price"] = price

    if isinstance(products_drinks_dict['name'], list):
        # create defaut product
        for i in range(len(products_drinks_dict['name'])):
            name = products_drinks_dict['name'][i]
            price = products_drinks_dict['price'][i]
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
    elif isinstance(products_drinks_dict['name'], str):
        # create user define product
        name = products_drinks_dict['name']
        price = products_drinks_dict['price']
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
def create_options():
    create_tempreature()
    create_size()
    create_milk()
        

# ADDON #############################
class Addon(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)


def db_table_exists(table_name):
    return table_name in connection.introspection.table_names()

def db_init_tables():
    for tb_name in INITIAL_TABLES:
        if db_table_exists(tb_name) is False:
            print(Manual_Exception.INITIAL_MSG)
            return True
    return False

def init_db():
    if db_init_tables() is True:
        return

    create_categories()
    create_products()
    create_variants()
    create_options()

