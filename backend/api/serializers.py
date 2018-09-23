from rest_framework import serializers
from api.models import Dog, Breed, BREED_SIZES, RATING_VALUES

class BreedSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    size = serializers.ChoiceField(choices=BREED_SIZES)
    friendliness = serializers.ChoiceField(choices=RATING_VALUES)
    trainability = serializers.ChoiceField(choices=RATING_VALUES)
    sheddingamount = serializers.ChoiceField(choices=RATING_VALUES)
    exerciseneeds = serializers.ChoiceField(choices=RATING_VALUES)

    def create(self, validated_data):
        return Breed.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.size = validated_data.get('size', instance.size)
        instance.friendliness = validated_data.get('friendliness', instance.friendliness)
        instance.trainability = validated_data.get('trainability', instance.trainability)
        instance.sheddingamount = validated_data.get('sheddingamount', instance.sheddingamount)
        instance.exerciseneeds = validated_data.get('exerciseneeds', instance.exerciseneeds)
        instance.save()
        return instance
