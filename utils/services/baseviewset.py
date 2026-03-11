from django.shortcuts import render
# Create your views here.
# views.py
from rest_framework import viewsets, permissions
from rest_framework import status, viewsets
from utils.services.responses import success_response, error_response


class BaseModelViewSet(viewsets.ModelViewSet):

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return success_response(
            message="List fetched successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return success_response(
            message="Record fetched successfully",
            data=serializer.data,
            status_code=status.HTTP_200_OK
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            serializer.save()
            return success_response(
                message="Record created successfully",
                data=serializer.data,
                status_code=status.HTTP_201_CREATED
            )
        return error_response(
            message="Validation error",
            errors=serializer.errors,
            status_code=status.HTTP_400_BAD_REQUEST
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)

        if serializer.is_valid():
            user = request.user
            serializer.save()
            return success_response(
                message="Record updated successfully",
                data=serializer.data,
                status_code=status.HTTP_200_OK
            )

        return error_response(
            message="Validation error",
            errors=serializer.errors,
            status_code=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return success_response(
            message="Record deleted successfully",
            status_code=status.HTTP_200_OK
        )

