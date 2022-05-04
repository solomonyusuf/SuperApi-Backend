from rest_framework import serializers

from .models import Contact, Sermon,Post, Video

class SupernaturalContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('id','fullname', 'phoneNumber','email','message')

class SupernaturalPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id','image', 'title','body','date')

class SupernaturalSermonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sermon
        fields = ('id','image','artist', 'name', 'audio','date')


class SupernaturalVideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ('id','image','artist', 'name','video','date')


