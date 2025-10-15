from rest_framework import serializers
from .models import Book, Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'rating', 'comment', 'created_at']


class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'created_at', 'avg_rating', 'reviews']

    def get_avg_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            return sum([r.rating for r in reviews]) / len(reviews)
        return 0
