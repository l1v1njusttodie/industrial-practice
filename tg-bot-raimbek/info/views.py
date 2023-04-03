from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from .models import AboutCompanyTable, AddressesTable
from .serializers import AboutCompanySerializer, AddressSerializer


class AboutCompanyDetails(APIView):
    def get(self, request):
        obj = AboutCompanyTable.objects.all()
        serializer = AboutCompanySerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AboutCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class AboutCompanyByQueryAPIView(generics.RetrieveAPIView):
    serializer_class = AboutCompanySerializer
    queryset = AboutCompanyTable.objects.all()

    def get_object(self):
        query_type = self.request.GET.get('type', None)
        query_value = self.request.GET.get('value', None)
        if not query_type or not query_value:
            return None
        try:
            if query_type == 'id':
                return AboutCompanyTable.objects.get(answer_id=query_value)
            if query_type == 'name_ru':
                return AboutCompanyTable.objects.get(name_ru=query_value)
        except AboutCompanyTable.DoesNotExist:
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


class AddressDetails(APIView):
    def get(self, request):
        obj = AddressesTable.objects.all()
        serializer = AddressSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class AddressByQueryAPIView(generics.RetrieveAPIView):
    serializer_class = AddressSerializer
    queryset = AddressesTable.objects.all()

    def get_object(self):
        query_type = self.request.GET.get('type', None)
        query_value = self.request.GET.get('value', None)
        if not query_type or not query_value:
            return None
        try:
            if query_type == 'id':
                return AddressesTable.objects.get(address_id=query_value)
        except AddressesTable.DoesNotExist:
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