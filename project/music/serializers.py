from rest_framework import serializers
from .models import Singer, Song, Tag, Image

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ['singer']


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'
        read_only_fields =['singer']

class SingerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only =True)
    
    songs = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)

    def get_images(self, instance):
        serializers = ImageSerializer(instance.images,many=True)
        return serializers.data

    def get_songs(self, instance):
        serializers = SongSerializer(instance.songs,many =True)
        return serializers.data

    tag = serializers.SerializerMethodField()
    def get_tag(self,instance):
        tags = instance.tag.all()
        return [tag.name for tag in tags]

    class Meta:
        model = Singer
        fields = '__all__'
        #['id','name','content','debut','songs','tag']
    image = serializers.ImageField(use_url=True, required = False)

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'
