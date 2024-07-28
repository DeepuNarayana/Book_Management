from django.urls import path
from .views import (
    BookListCreateView,
    BookRetrieveUpdateDestroyView,
    ReviewListCreateView,
    ReviewListView,
    BookSummaryView,
    BookRecommendationsView,
    GenerateSummaryView
)

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
    path('books/<int:pk>/reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('books/<int:pk>/reviews/list/', ReviewListView.as_view(), name='review-list'),
    path('books/<int:pk>/summary/', BookSummaryView.as_view(), name='book-summary'),
    path('recommendations/', BookRecommendationsView.as_view(), name='book-recommendations'),
    path('generate-summary/', GenerateSummaryView.as_view(), name='generate-summary'),
]
