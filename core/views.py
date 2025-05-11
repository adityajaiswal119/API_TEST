from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DataProcessingView(APIView):
    def post(self, request):
        input_data = request.data.get("data", [])

        even_numbers = []
        odd_numbers = []
        alphabets = []

        for item in input_data:
            if str(item).isdigit():
                if int(item) % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
            elif str(item).isalpha():
                alphabets.append(str(item).upper())

        result = {
            "is_success": True,
            "user_id": "aditya_jaiswal_0827CY221005",
            "email": "adityajaiswal221123@acropolis.in",
            "roll_number": "0827CY221005",
            "even_numbers": even_numbers,
            "odd_numbers": odd_numbers,
            "alphabets": alphabets 
        }

        return Response(result, status=status.HTTP_200_OK)

# Create your views here.
