from rest_framework import viewsets, permissions
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_pk'])

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, book_id=self.kwargs['book_pk'])

