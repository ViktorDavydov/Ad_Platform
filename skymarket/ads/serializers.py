from rest_framework import serializers


from .models import Ad


class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('pk', 'image', 'title', 'price', 'description')


class AdListSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source="author.phone")
    author_first_name = serializers.CharField(source="author.first_name")
    author_last_name = serializers.CharField(source="author.last_name")
    author_id = serializers.CharField(source="author.id")

    class Meta:
        model = Ad
        fields = (
            "pk",
            "image",
            "title",
            "price",
            "phone",
            "description",
            "author_first_name",
            "author_last_name",
            "author_id",
        )
