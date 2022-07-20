from xml.dom import ValidationErr
from rest_framework import serializers 
from contacts_api.models import Contact
from django.forms import ValidationError

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def validate(self, data):
        if  len(data['nickname']) < 5:
            raise ValidationError("Thats a bad nickname. Ensure nickname has a minimum of 5 characters")
        return data