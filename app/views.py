from django.shortcuts import render
from app.forms import RegisterForm

# Create your views here.
def registro(request):
    data={}
    data['form']=RegisterForm(request.POST or None)
    if data['form'].is_valid():
        data['form'].save()

    return render(request, 'registro.html', data)