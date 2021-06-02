from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import pandas as pd 
from orderapp.models import Products
class Command(BaseCommand):
    help = 'products and cosnsumers '

    def add_arguments(self, parser):
        parser.add_argument('products', type=str)  # ← no nargs='+'
        parser.add_argument('consumers', type=str)
        

    def handle(self, *args,  **options):
        product_data = str(options['products']) 
        consumer_data = str(options['consumers']) 
        df = pd.read_excel(product_data)
        file_data_products_compare = list(map(lambda x: x.lower(), list(df.columns)))
        file_data_products = list(map(lambda x: x, list(df.columns)))
        total_table = {}
        db_data_producta = [f.name for f in Products._meta.get_fields()]
        if any(x in file_data_products_compare for x in db_data_producta)== True:
            for value in file_data_products:
                total_table[value] = df[value].to_list()
                print(total_table)
            
        