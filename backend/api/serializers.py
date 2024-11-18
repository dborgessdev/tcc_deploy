from rest_framework import serializers
from .models import Pacient, Doctor, Queue, Reception, Consultation, Nurse


class PacientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = '__all__'

class ReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reception
        fields = '__all__'

class ConsultationSerializer(serializers.ModelSerializer):

    pacient = PacientSerializer()

    doctor = DoctorSerializer()

    queue = QueueSerializer()

    final_status_display = serializers.CharField(source='get_final_status_display', read_only=True)

    start_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    end_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Consultation
        fields = '__all__'

    def validate(self, data):
        if data['end_time'] and data['start_time'] and data['end_time'] < data['start_time']:
            raise serializers.ValidationError("End time must be after start time.")
        return data

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'


