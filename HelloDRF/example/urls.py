from django.urls import path
from rest_framework import routers
from .views import BookViewSet
# from .views import HelloAPI, bookAPI, booksAPI, BookAPI, BooksAPI, BooksAPIMixins, BookAPIMixins


router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls

"""
urlpatterns = [
    path('hello/', HelloAPI),
    path('fbv/books/', booksAPI),
    path('fbv/book/<int:ISBN>/', bookAPI),
    path('cbv/books/', BooksAPI.as_view()),
    path('cbv/book/<int:ISBN>/', BookAPI.as_view()),
    path('mixin/books/', BooksAPIMixins.as_view()),
    path('mixin/book/<int:ISBN>/', BookAPIMixins.as_view()),
]
"""