from django.http import HttpResponse
from django.shortcuts import render


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from todoapp.myapp.models import MyModel
from todoapp.myapp.serializers import MyModelSerializer


class MyModelListCreateAPIView(ListCreateAPIView):
    serializer_class = MyModelSerializer

    def get_queryset(self):
        return MyModel.objects.filter()

    def perform_create(self, serializer):
        serializer.save()


class MyModelDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MyModelSerializer
    queryset = MyModel.objects.all()


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def index(request):
    return HttpResponse("hello")


def index(request):
    latest_question_list = MyModel.objects.order_by('-date_created')[:5]
    output = ', '.join([q.first_name for q in latest_question_list])
    context = {'latest_question_list': latest_question_list}
    # return HttpResponse(output)
    return render(request, 'index.html', context)
