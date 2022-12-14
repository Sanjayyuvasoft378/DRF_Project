from rest_framework import serializers
from drf_app.models import Movie

def name_length(value):
    if len(value)<2:
        raise serializers.ValidationError("name is too short")
    else:
        return value
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators = [name_length])
    description = serializers.CharField(max_length=100)
    active = serializers.BooleanField(default=True)
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance
    
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description should be diffrent")
        else:
            return data
    
    def validate_name(self,value):
        if len(value)<2:
            raise serializers.ValidationError("name is too short")
        else:
            return value
        
    
   
        