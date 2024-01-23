from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from .models import Exams
from decimal import Decimal

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

        order_exams = Exams.objects.filter(
            id__in=exams_id
        )

        print(order_exams)

        exams_price = sum([exam.exam_price for exam in order_exams])
        
        total_amount_exams = f'{Decimal(round(exams_price, 2)):.2f}'

        # # TODO calculate price of data disponiveis

        return render(
            request=request, template_name='request_exam.html',
            context={'exams_type': exams_type, 'order_exams': order_exams,
            'total_amount': total_amount_exams}
        )
