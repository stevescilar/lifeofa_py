import pandas as pd
from django.core.management.base  import BaseCommand
from book.models import Book
from sqlalchemy import create_engine

class Command(BaseCommand):
    help = "A command to add data from an Excel file to the database"

    def handle(self, *args, **options):

        excel_file = "books.xlsx"
        df = pd.read_excel(excel_file)
        
        engine = create_engine('sqlite:///db.sqlite3')


        df.to_sql(Book._meta.db_table, if_exists='replace', con=engine, index=True)

        



