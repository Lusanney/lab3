from rest_framework import serializers
from .models import *

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'sex', 'nationality', 'passport_no']

class VisitorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ['username', 'password', 'first_name', 'last_name', 'id']

    def create(self, validated_data):
        visitor = Visitor(username=validated_data['username'], first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        visitor.set_password(validated_data['password'])
        visitor.save()
        return visitor
class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'sex', 'license', 'workExp']

class HostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ['username', 'password']

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()
    class Meta:
        model = Room
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['date_checkin', 'date_checkout', 'main_guest', 'room', 'booking_code']

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"

# Functional analytics views

class BookingBillSerializer(serializers.ModelSerializer):
    bills = BillSerializer(many=True)
    main_guest = VisitorSerializer()
    room = RoomSerializer()

    class Meta:
        model = Booking
        fields = "__all__"

class BookingOfVisitorSerializer(serializers.ModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = Booking
        fields = ['id', 'booking_code', 'date_checkin', 'date_checkout', 'room']

class HotelInfoSerializer(serializers.ModelSerializer):
    owner = HostSerializer()
    class Meta:
        model = Hotel
        fields = "__all__"