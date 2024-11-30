
from django.shortcuts import render
from home.models import  resumeHome
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from home.serializers import resumeHomeSerializer


# class resumeViewSet(viewsets.ModelViewSet):
#     queryset = resume.objects.all()
#     serializer_class= resumeSerializer

class resumeHomeAPIVIEW(APIView):
    
    # GET request to fetch all resumeHome entries
    def get(self, request, format=None):
        res_obj = resumeHome.objects.all()  # Get all resumeHome objects
        serializer = resumeHomeSerializer(res_obj, many=True)  # Serialize the queryset
        return Response(serializer.data)  # Return the serialized data

    # POST request to create a new resumeHome entry
    def post(self, request, format=None):
        serializer = resumeHomeSerializer(data=request.data)  # Pass incoming data to the serializer
        if serializer.is_valid():  # Check if the data is valid
            serializer.save()  # Save the new resumeHome object
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the serialized data with a 201 status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid data

    # PUT request to update an existing resumeHome entry
    def put(self, request, pk, format=None):
        try:
            res_obj = resumeHome.objects.get(pk=pk)  # Get the resumeHome object by primary key (pk)
        except resumeHome.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)  # Return 404 if object not found
        
        serializer = resumeHomeSerializer(res_obj, data=request.data)  # Pass data for updating
        if serializer.is_valid():  # Check if the updated data is valid
            serializer.save()  # Save the changes
            return Response(serializer.data)  # Return the updated data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid data

    # DELETE request to delete a resumeHome entry
    def delete(self, request, pk, format=None):
        try:
            res_obj = resumeHome.objects.get(pk=pk)  # Get the resumeHome object by primary key (pk)
        except resumeHome.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)  # Return 404 if object not found
        
        res_obj.delete()  # Delete the object
        return Response({"detail": "Deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
