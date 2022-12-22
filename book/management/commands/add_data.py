import pandas as pd
from django.core.management.base  import BaseCommand
from book.models import Book

class Command(BaseCommand):
    help = "A command to add data from an Excel file to the database"

    def handle(self, *args, **options):

        excel_file = "books.xlsx"
        df = pd.read_excel(excel_file)
        print(df)