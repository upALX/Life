from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from .models import Exams

# Create your views here.
@login_required
def request_exams(request):
    print('User is: ', request.user)

    exams_type = Exams.objects.all()

    if request.method == 'GET':
        return render(request=request, template_name='request_exam.html', context={'exams_type': exams_type})
    elif request.method == 'POST':
        exams_id = request.POST.getlist('exams_selected')

        print(exams_id)

        return HttpResponse('Hello world')

        # order_exams = Exams.objects.filter(
        #     id__in=exams_id
        # )

        # total_amount_exam = sum([exam.price for exam in order_exams])
        # # TODO calculate price of data right

        # return render(
        #     request=request, template_name='request_exam.html',
        #     context={'exams_type': exams_type, 'order_exams': order_exams,
        #     'total_amount': total_amount_exam}
        # )
