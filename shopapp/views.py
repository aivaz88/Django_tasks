from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Main page started")
    return HttpResponse('Привет мир!')


def heads_or_tails(request):
    logger.info('Heads or Tails page started')
    return HttpResponse(choice(['Орел', 'Решка']))


def cube(request):
    logger.info('Cube page started')
    return HttpResponse(f'Выпало: {randint(1, 6)}')


def random_number(request):
    logger.info('Random Number page started')
    return HttpResponse(f'Случайное число: {randint(1, 100)}')
