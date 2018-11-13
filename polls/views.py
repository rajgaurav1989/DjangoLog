from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)

def index(request):
    logger.info('This is a manually logged INFO string.')
    logger.debug('This is a manually logged DEBUG string.')
    return HttpResponse("Hello, world. You're at the polls index.")