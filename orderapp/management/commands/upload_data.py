from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import pandas as pd 
from sqlalchemy import create_engine

from django.conf import settings

from orderapp.models import Products
class Command(BaseCommand):
    help = 'products and cosnsumers '

    def add_arguments(self, parser):
        parser.add_argument('products', type=str)  # ← no nargs='+'
        parser.add_argument('consumers', type=str)
        

    def handle(self, *args,  **options):
        product_data = str(options['products']) 
        consumer_data = str(options['consumers']) 
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME'] 
        database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
        user=user,
        password=password,
        database_name=database_name,
        )
        engine = create_engine(database_url, echo=False)
        
        if product_data:
            df = pd.read_excel(product_data)
        # df.columns = ["name", "code", "price", "features", "inventory"]
        
            df.columns = list(map(lambda x: x.lower(), list(df.columns)))
        # df.set_index("id", inplace=True)
            print(df.dtypes)
        # df.columns = list(map(lambda x: x, list(df.columns)))
        # total_table = {}
        # db_data_producta = [f.name for f in Products._meta.get_fields()]
        # if any(x in file_data_products_compare for x in db_data_producta)== True:
        #     for value in file_data_products:
        #         total_table[value] = df[value].to_list()
        #         print(total_table)

       
            
            df.to_sql('orderapp_producer', con=engine,  if_exists='append',index=False)

        if consumer_data:

            df = pd.read_excel(consumer_data)
        # df.columns = ["name", "code", "price", "features", "inventory"]
        
            df.columns = list(map(lambda x: x.lower(), list(df.columns)))
        # df.set_index("id", inplace=True)
            print(df.dtypes)
        # df.columns = list(map(lambda x: x, list(df.columns)))
        # total_table = {}
        # db_data_producta = [f.name for f in Products._meta.get_fields()]
        # if any(x in file_data_products_compare for x in db_data_producta)== True:
        #     for value in file_data_products:
        #         total_table[value] = df[value].to_list()
        #         print(total_table)

       
            
            df.to_sql('orderapp_consumer', con=engine,  if_exists='append',index=False)
               