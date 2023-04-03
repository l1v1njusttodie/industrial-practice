from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from .models import Employees, Status
from .serializer import EmployeeSerializer, StatusSerializer
from django.contrib.auth.models import User


class EmployeeDetail(APIView):
    def get(self, request):
        obj = Employees.objects.all()
        serializer = EmployeeSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class EmployeeByQueryAPIView(generics.RetrieveAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employees.objects.all()

    def get_object(self):
        query_type = self.request.GET.get('type', None)
        query_value = self.request.GET.get('value', None)
        if not query_type or not query_value:
            return None
        try:
            if query_type == 'email':
                return Employees.objects.get(email=query_value)
            elif query_type == 'chat_id':
                return Employees.objects.get(chat_id=query_value)
            elif query_type == 'phone_number':
                query_value = '+' + query_value[1:]
                return Employees.objects.get(phone_number=query_value)
            elif query_type == 'id':
                return Employees.objects.get(employee_id=query_value)
            elif query_type == 'username':
                return Employees.objects.get(username=query_value)
        except Employees.DoesNotExist:
            pass
        return None

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class StatusDetail(APIView):
    def get(self, request):
        obj = Status.objects.all()
        serializer = StatusSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


