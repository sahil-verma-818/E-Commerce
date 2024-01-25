import random, string
from django.core.management.base import BaseCommand
import sass

class Command(BaseCommand):
    help = "Compiling is in process, converting SCSS to CSS!"

    def handle(self, *args, **kwargs):
        result = sass.compile(filename='static/assets/css/styles.scss')
        result_file = open('static/assets/css/style.css', "a")
        result_file.write(result)
        result_file.close()
