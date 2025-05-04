from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from users.models import User, Patient, MedicalRecord
from rest_framework.authtoken.models import Token

class PatientRecordTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

       
        self.doctor1 = User.objects.create_user(username="doctor1", password="pass123", role = 'doctor')
        self.token1 = Token.objects.create(user=self.doctor1)

        
        self.doctor2 = User.objects.create_user(username="doctor2", password="pass456", role = 'doctor')
        self.token2 = Token.objects.create(user=self.doctor2)

    def test_doctor_can_create_and_view_own_patients(self):
       
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token1.key)

        
        response = self.client.post(reverse('create_patient'), {
            "name": "John",
            "age": 30,
            "gender": "MALE",
            "address": "123 Street"
        })
        self.assertEqual(response.status_code, 201)
        patient_id = response.data['id']

        response = self.client.get(reverse('get_patient_details'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'John')

       
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token2.key)

        
        response = self.client.get(reverse('get_patient_details'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

        
        response = self.client.get(reverse('get medical records by patient id', args=[patient_id]))
        self.assertEqual(response.status_code, 403)  

    def test_login(self):
        response = self.client.post(reverse('login'), {
            "username": "doctor1",
            "password": "pass123"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)