# views.py

from django.shortcuts import render, redirect  
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .helping import send_otp_to_phone

@api_view(['POST'])
def send_otp(request):

  phone = request.data['phone']

  otp = send_otp_to_phone(phone)
  
  if not otp:
    return Response({'error': 'Failed to generate OTP'})  

  request.session['phone'] = phone
  request.session['otp'] = otp

  return Response({'status': 'success'})


@api_view(['POST']) 
def verify_otp(request):

  phone = request.session['phone']
  otp = request.session['otp']

  if request.data['otp'] != otp:
    return Response({'error':'Invalid OTP'})

  return Response({'status':'success'})