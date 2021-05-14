from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'books', views.BooksViewSet)
router.register(r'book_types', views.Book_typesViewSet)
router.register(r'book_authors', views.Book_authorsViewSet)
router.register(r'book_tags', views.Book_tagsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]