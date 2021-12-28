import sys
from rest_framework import generics
from rest_framework.views import APIView, Response
import shortuuid

from .serializers import *
from .models import *

# Visitors
class VisitorListView(generics.ListAPIView):
    serializer_class = VisitorSerializer
    queryset = Visitor.objects.all()

class VisitorSingleCreateView(generics.CreateAPIView):
    serializer_class = VisitorCreateSerializer

class VisitorSingleRetrieveView(generics.RetrieveAPIView):
    serializer_class = VisitorSerializer
    queryset = Visitor.objects.all()

class VisitorSingleUpdateView(generics.UpdateAPIView):
    serializer_class = VisitorSerializer
    queryset = Visitor.objects.all()

class VisitorSingleDestroyView(generics.DestroyAPIView):
    serializer_class = VisitorSerializer
    queryset = Visitor.objects.all()

# ----------------

# Hosts
class HostListView(generics.ListAPIView):
    serializer_class = HostSerializer
    queryset = Host.objects.all()

class HostSingleCreateView(generics.CreateAPIView):
    serializer_class = HostCreateSerializer

class HostSingleRetrieveView(generics.RetrieveAPIView):
    serializer_class = HostSerializer
    queryset = Host.objects.all()

class HostSingleUpdateView(generics.UpdateAPIView):
    serializer_class = HostSerializer
    queryset = Host.objects.all()

class HostSingleDestroyView(generics.DestroyAPIView):
    serializer_class = HostSerializer
    queryset = Host.objects.all()

# ---------------

# Hotel
class HotelListView(generics.ListAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

class HotelSingleCreateView(generics.CreateAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

class HotelSingleRetrieveView(generics.RetrieveAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

class HotelSingleUpdateView(generics.UpdateAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

class HotelSingleDestroyView(generics.DestroyAPIView):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

# ---------------

# Room
class RoomListView(generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class RoomSingleCreateView(generics.CreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class RoomSingleRetrieveView(generics.RetrieveAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class RoomSingleUpdateView(generics.UpdateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

class RoomSingleDestroyView(generics.DestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
# ---------------

# Booking
class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

class BookingSingleCreateView(APIView):
    def post(self, request):
        rawBooking = {}
        rawBooking['booking_code'] = shortuuid.ShortUUID().random(length=7)
        rawBooking['date_checkin'] = request.data.get('date_checkin')
        rawBooking['date_checkout'] = request.data.get('date_checkout')
        rawBooking['main_guest'] = request.data.get('main_guest')
        rawBooking['room'] = request.data.get('room')

        bookingSerializer = BookingCreateSerializer(data=rawBooking)

        if bookingSerializer.is_valid(raise_exception=True):
            booking = bookingSerializer.save()
            serializedBooking = BookingSerializer(booking)

            # initialize bill
            rawBill = {}
            rawBill['service_name'] = 'Stay'
            rawBill['description'] = 'stay cost'
            room = Room.objects.get(pk=booking.room.id)
            rawBill['total'] = room.price
            rawBill['booking'] = booking.id

            billSerializer = BillSerializer(data=rawBill)
            if billSerializer.is_valid(raise_exception=True):
                bill = billSerializer.save()
            
            
        return Response(serializedBooking.data)
        

class BookingSingleRetrieveView(generics.RetrieveAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

class BookingSingleUpdateView(generics.UpdateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

class BookingSingleDestroyView(generics.DestroyAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
# ---------------

# Bill
class BillListView(generics.ListAPIView):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()

class BillSingleCreateView(generics.CreateAPIView):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()

class BillSingleRetrieveView(generics.RetrieveAPIView):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()

class BillSingleUpdateView(generics.UpdateAPIView):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()

class BillSingleDestroyView(generics.DestroyAPIView):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()

# ---------------

# Functional Analytics
class BookingReportView(APIView):
    def get(self, request, pk):
        try:
            booking = Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            return Response({"details": "Not found."})
            
        bills = booking.bills.all()

        total_price = 0
        for bill in bills:
            total_price += bill.total

        total_days = booking.date_checkout - booking.date_checkin

        bookingSerializer = BookingBillSerializer(booking)
        return Response({"Booking": bookingSerializer.data, "Report": { "total_price": total_price, "total_days": total_days.days + 1}})

class HotelInfoView(APIView):
    def get(self, request, pk):
        try:
            hotel = Hotel.objects.get(pk=pk)
        except Hotel.DoesNotExist:
            return Response({"details": "Not found."})

        rooms = hotel.rooms.all()

        total_room = len(rooms)
        available_rooms = 0
        min_price = sys.maxsize
        max_price = 0
        for room in rooms:
            if room.state == 'AV':
                available_rooms += 1
            
            if room.price > max_price:
                max_price = room.price

            if room.price < min_price:
                min_price = room.price

        hotelSerializer = HotelInfoSerializer(hotel)
        return Response(
            {
                "Hotel": hotelSerializer.data, 
                "Info": { 
                    "total_rooms": total_room,
                    "available_rooms": available_rooms, 
                    "min_price": min_price,
                    "max_price": max_price,
                    "average_price":  round((max_price + min_price) / 2)
                }
            }
        )

class HotelRoomListView(APIView):
    def get(self, request, pk):
        try:
            rooms = Room.objects.filter(hotel=pk)
        except Room.DoesNotExist:
            return Response({"details": "Not found."})

        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

class HotelAvailableRoomListView(APIView):
    def get(self, request, pk):
        try:
            rooms = Room.objects.filter(hotel=pk, state="AV")
        except Room.DoesNotExist:
            return Response({"details": "Not found."})

        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

class VisitorBookingListView(APIView):
    def get(self, request, pk):
        try:
            bookings = Booking.objects.filter(main_guest=pk)
        except Booking.DoesNotExist:
            return Response({"details": "Not found."})

        serializer = BookingOfVisitorSerializer(bookings, many=True)
        return Response(serializer.data)

# ---------------
