from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LessonPlan, Quiz
from .ai_services import generate_lesson_plan_content, generate_quiz_questions

class LessonPlanGenerator(APIView):
    """
    API endpoint for generating lesson plans using AI.
    """
    def post(self, request):
        instrument = request.data.get('instrument')
        topic = request.data.get('topic')
        level = request.data.get('level')
        content = generate_lesson_plan_content(instrument, topic, level)
        return Response({'content': content}, status=status.HTTP_200_OK)

class QuizGenerator(APIView):
    """
    API endpoint for generating quiz questions using AI.
    """
    def post(self, request):
        topic = request.data.get('topic')
        num_questions = request.data.get('num_questions', 5)
        questions = generate_quiz_questions(topic, num_questions)
        return Response({'questions': questions}, status=status.HTTP_200_OK)

# Other views for managing students, assignments, payments, etc. would be defined here.
