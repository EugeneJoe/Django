from rest_framework import viewsets
from rest_framework.response import Response
from . import models, serializer
from rest_framework.decorators import action


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializer.Question_Serializer
    lookup_field = 'id'

    @action(detail=True, methods=["GET"])
    def choices(self, request, id=None):
        """
        Return all the choices for a particular Question
        """
        question = self.get_object()
        choices = models.Choice.objects.filter(question=question)
        serial = serializer.Choice_Serializer(choices, many=True)
        return Response(serial.data, status=200)

    @action(detail=True, methods=["POST"])
    def choice(self, request, id=None):
        """
        Create a choice for a particular Question
        """
        question = self.get_object()
        data = request.data
        data["question"] = question.id
        serializer = serializer.Question_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = models.Choice.objects.all()
    serializer_class = serializer.Choice_Serializer
