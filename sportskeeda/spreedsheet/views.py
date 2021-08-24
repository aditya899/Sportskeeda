from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework import status

from rest_framework.decorators import api_view

@api_view(['GET'])
def column_number(request, string):
    if request.method == 'GET':
        res = 0
        for i in range(len(string)):
            res *= 26
            res += ord(string[i]) - ord('A') + 1
    d = {}
    d[string] = res
    return Response(d)