from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import UserAnswer
from .serializers import UserAnswerSerializer

class UserAnswerListView(generics.ListAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer

class UserAnswerCreateView(generics.CreateAPIView):
    serializer_class = UserAnswerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User answer created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAnswersByTestView(generics.ListAPIView):
    serializer_class = UserAnswerSerializer

    def get_queryset(self):
        test_id = self.kwargs['test_id']
        return UserAnswer.objects.filter(test_id=test_id)

class UserAnswersByUserView(generics.ListAPIView):
    serializer_class = UserAnswerSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return UserAnswer.objects.filter(user_id=user_id)

class SubmitResultsView(APIView):
    def post(self, request):
        return Response({'message': 'Results submitted successfully'}, status=status.HTTP_200_OK)