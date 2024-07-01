from rest_framework import serializers
from .models import Singer, Song


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields ='__all__'
        read_only_fields =['singer']

class SingerSerializer(serializers.ModelSerializer):
    id =serializers.CharField(read_only=True)

    songs = serializers.SerializerMethodField(read_only=True)

    def get_songs(self,instance):
        serializers = SongSerializer(instance.songs,many=True)
        return serializers.data
    
    class Meta:
        model = Singer
        fields = ['id','content','debut','songs']

