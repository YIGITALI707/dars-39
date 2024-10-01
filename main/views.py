
from .models import Color,Car,Brand
from .serializers import BrandSerializers,CarSerializers,ColorSerializers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class BrandListCreateView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers
    permission_classes = [IsAuthenticated]



class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers
    permission_classes = [IsAdminUser]


class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers
    permission_classes = [IsAuthenticated]



class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializers
    permission_classes = [IsAdminUser]


class ColorListCreateView(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializers
    permission_classes = [IsAuthenticated]

class ColorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializers
    permission_classes = [IsAdminUser]
