from rest_framework import serializers
from users.models import User,Patient,MedicalRecord




class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username','password', 'email', 'first_name', 'last_name', 'role' ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
            password = validated_data.pop('password')
            user = User(**validated_data)
            user.set_password(password)
            user.save()
            return user
    
class PatientSerializer(serializers.ModelSerializer):
     class Meta:
          model = Patient
          fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
     class Meta:
          model = MedicalRecord
          fields = '__all__'
          


        
