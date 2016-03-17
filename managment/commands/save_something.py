from django.core.management.base import BaseCommand, CommandError
from upload.models import Upload
from upload.

class Command(BaseCommand):

    def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        pass
