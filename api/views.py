from django.shortcuts import render
from django.http import HttpResponse
from .models import Ministry, Fundings
from .serializers import MinistrySerializer, FundingsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

# Create your views here.


# get all the list of fundings and post a new funding to insert
@api_view(['GET', 'POST'])
def fundings_list(request):

    # handling fundings --> GET
    if request.method == "GET":
        fundings = Fundings.objects.all()
        serializers = FundingsSerializer(fundings, many=True)
        return Response(serializers.data)

    # handling the post request with request body to insert a new funding
    elif request.method == "POST":
        serializers = FundingsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# handle single funding detail read, update and delete request


@api_view(['GET', 'PUT', 'DELETE'])
def funding_details(request, param):
    # get the funding of param id
    try:
        funding = Fundings.objects.get(pk=param)

    except Fundings.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # handle funding/:param --> GET
    if request.method == "GET":
        serializer = FundingsSerializer(funding)
        return Response(serializer.data)

    # handle funding/:param --> PUT
    elif request.method == "PUT":
        serializer = FundingsSerializer(funding, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # handle funding/:param --> Delete
    elif request.method == "DELETE":
        funding.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# get all the list of Ministry and post a new ministry to insert
@api_view(['GET', 'POST'])
def ministry_list(request):

    # handling ministry list --> GET
    if request.method == "GET":
        ministry = Ministry.objects.all()
        serializers = MinistrySerializer(ministry, many=True)
        return Response(serializers.data)

    # handling the post request with request body to insert a new ministry
    elif request.method == "POST":
        serializers = MinistrySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def ministry_details(request, param):
    # get the funding of param id
    try:
        ministry = Ministry.objects.get(name=param)

    except Ministry.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # handle ministry/:param --> GET
    if request.method == "GET":
        serializer = MinistrySerializer(ministry)
        fundings = Fundings.objects.filter(ministry=serializer.data['id'])
        fundingsData = FundingsSerializer(fundings, many=True)

        res = {
            "ministry": serializer.data,
            "fundings": fundingsData.data
        }
        return Response(res)

    # handle ministry/:param --> PUT
    elif request.method == "PUT":
        serializer = MinistrySerializer(ministry, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # handle ministry/:param --> Delete
    elif request.method == "DELETE":
        ministry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
