from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            	   'Uses HTTP methods as function',
                'Is similar to a traditional Django view',
                'Gives ypu the most control over you application logic',
                'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'That was a put method'})

    def patch(self,request,pk=None):
        """Only update the field requested"""
        return Response({'method':"This is a patch method"})

    def delete(self,request,pk=None):
        """Only update the field requested"""
        return Response({'method':"This is a delete method"})


class HelloViewSet(viewsets.ViewSet):
    """Test API View Set"""
    serializer_class= serializers.HelloSerializer

    def list(self,request):
        """Return a hello message"""
        a_viewset = [
            'User actions testing ViewSet',
            'Testing the server issue',
            'provide more functionality with less code',
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def retreive(self,request,pk=None):
        #handle getting an onject by id
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        #Update
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        #Partial Update
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        #Delete
        return Response({'http_method':'DELETE'})
