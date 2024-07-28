from rest_framework import generics
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(book_id=self.kwargs['pk'])

class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['pk'])

class BookSummaryView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        reviews = instance.reviews.all()
        total_reviews = reviews.count()
        if total_reviews > 0:
            average_rating = sum(review.rating for review in reviews) / total_reviews
        else:
            average_rating = 0
        summary = {
            'book': instance.title,
            'total_reviews': total_reviews,
            'average_rating': average_rating,
            'reviews': ReviewSerializer(reviews, many=True).data
        }
        return Response(summary)

class BookRecommendationsView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):       
        return Book.objects.all()

class GenerateSummaryView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        content = request.data.get('content', '')
        summary = generate_summary(content)  
        return Response({'summary': summary})

def generate_summary(content):
    return "Generated summary for the given content."
