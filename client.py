import requests
import sys
import argparse

url = 'http://127.0.0.1:5000/home'

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--title', required=True, help='Inserimento del titolo')
parser.add_argument('-d', '--date', required=True, help='Inserimento della data')
parser.add_argument('-c', '--content', required=True, help='Inserimento del contenuto')
args = parser.parse_args()

requests.post(url, json={'title': args.title, 'date': args.date, 'content': args.content})
