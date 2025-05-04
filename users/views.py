from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import User, Patient, MedicalRecord
from .serializers import UsersSerializer, PatientSerializer, MedicalRecordSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .permissions import IsDoctor


# Create your views here.
@api_view(['POST'])
def signup(request):
    data = request.data
    print (data)
    serializer = UsersSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password :
        return Response({'error':"username and password are mandatory"},status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username = username, password = password )
    if user is not None:
        token, created=Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user_id": user.id,
            "username": user.username,
            "email": user.email
        }, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)
    


@api_view(['POST'])
@permission_classes([IsDoctor])
def create_patient(request):
    name = request.data.get('name')
    age = request.data.get('age')
    gender = request.data.get('gender')
    address = request.data.get('address')
    if not name or not age  or not gender:
        return Response({'error':"name,age and gender are mandatory"}, status = status.HTTP_400_BAD_REQUEST)
    user = request.user.id
    data = {"name":name,"age":age,"gender":gender,"address":address,"created_by":user}
    serializer = PatientSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['GET'])
@permission_classes([IsDoctor])
def get_patient_details(request):
    patients = Patient.objects.filter(created_by = request.user)
    serializer = PatientSerializer(patients, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK )



@api_view(['POST'])
@permission_classes([IsDoctor])
def create_record(request):
    patient = request.data.get('patient')
    symptoms = request.data.get('symptoms')
    diagnosis = request.data.get('diagnosis')
    treatment = request.data.get('treatment')
    if not patient:
        return Response({'error':"patient is required"},status = status.HTTP_400_BAD_REQUEST)
    data = {"patient":patient,"symptoms":symptoms, "diagnosis":diagnosis, "treatment":treatment}
    serializer = MedicalRecordSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([IsDoctor])
def get_medicalrecords_by_patient_id(request,patient_id):
    try:
        patient = Patient.objects.get(id = patient_id)
    except Patient.DoesNotExist:
        return Response({'error':"patient with  not exist"}, status=status.HTTP_404_NOT_FOUND)
    if patient.created_by != request.user:
        return Response({'error': "Access forbideen - you can only access your patient records " },status= status.HTTP_403_FORBIDDEN)
    medicalrecords = MedicalRecord.objects.filter(patient=patient)
    serializer = MedicalRecordSerializer(medicalrecords, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)



    
            








    
    



