from django.http import JsonResponse
from .models import Drink
from .serializer import DrinkSerialzer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status as status

# it is prefer to use rest_framework Response as response

@api_view(["GET", "POST"])
def drink_list(request):
    # 1. get all drinks
    # 2. serialize drink datas
    # 3. return as JSON format

    if request.method == "GET":
        drinks = Drink.objects.all()
        serializer = DrinkSerialzer(drinks, many=True)
        # return JsonResponse(serializer.data, safe=False)
        # or wrap with {} to specify as object array
        return JsonResponse({"drinks": serializer.data})

    if request.method == "POST":
        serializer = DrinkSerialzer(data=request.data)
        # print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("server error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DrinkSerialzer(drink)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # similar to post api above
        serializer = DrinkSerialzer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)