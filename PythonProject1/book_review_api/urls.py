from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from books.views import BookViewSet, ReviewViewSet

router = routers.SimpleRouter()
router.register(r'books', BookViewSet, basename='books')

books_router = routers.NestedSimpleRouter(router, r'books', lookup='book')
books_router.register(r'reviews', ReviewViewSet, basename='book-reviews')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include(books_router.urls)),
    path('api/auth/', include('rest_framework.urls')),
]
