from .models import User_details, User_favorite, User_followers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import User_detailSerializer, User_followersSerializer, User_favouriteSerializer
from rest_framework import status



@api_view(['GET'])
def Routes(request):
    routes = [
        'create-account/<str:address>/',
        'update/<str:address>/',
        'create-followers/<str:user_id>/',
        'create-favorite',
        'get-user-favorite/<str:user_id>/',
        'get-or-delete-favorite/<str:User_id>/<str:NFT_id>/',
    ]
    return Response(routes, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_or_create_account(request, address):
    try:
        user = User_details.objects.get(address_id=address)
    except:
        user = User_details.objects.create(address_id=address)
    serializer = User_detailSerializer(user, many=False)
    return Response(serializer.data)



@api_view(['PUT','GET'])
def get_or_update(request, address):
    user = User_details.objects.get(address_id=address)
    if request.method == "PUT":
        serializer = User_detailSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    else:
        serializer = User_detailSerializer(user, many=False)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT'])
def get_or_create(request, user_id):
    if request.method == "GET":
        try:
            followers = User_followers.objects.get(address=user_id)
            serializer =  User_followersSerializer(followers, many=False)
            return Response(serializer.data)
        except:
            return Response("no response")

    elif request.method == "PUT":
        followers = User_followers.objects.get(id=user_id)
        serializer = User_detailSerializer(followers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

    else:
        serializer = User_followersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST', 'GET'])
def _create_fovorites(request):
    serializer = User_favouriteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_User_NFT_favorite(request, user_id):
    favorites = User_favorite.objects.filter(address=user_id)
    serializer = User_favouriteSerializer(favorites, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE'])
def get_or_delete_favorite(request, User_id, NFT_id):

    try:
        favorites = User_favorite.objects.get(address=User_id, favorites_id=NFT_id)
        print("i got here")
    except User_favorite.DoesNotExist:
        return Response("Data not found",status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "GET":
         serializer = User_favouriteSerializer(favorites, many=False)
         return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        favorites.delete()
        return Response("data has been deleted", status=status.HTTP_204_NO_CONTENT)

