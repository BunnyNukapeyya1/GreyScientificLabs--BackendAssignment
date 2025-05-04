from django.urls import path
from users.views import signup,login,create_patient,get_patient_details,create_record,get_medicalrecords_by_patient_id


urlpatterns = [ 
    path('signup', signup, name = "sigmup"),
    path('login', login, name = "login"),
    path('patients',create_patient, name = "create_patient"),
    path('patients/all', get_patient_details,name = "get_patient_details"),
    path('patients/records/add', create_record, name = "create_record"),
    path('patients/<int:patient_id>/records',get_medicalrecords_by_patient_id, name = "get medical records by patient id")


]


