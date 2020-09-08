from django.shortcuts import render

projects=[
    {
        'name':'Jack',
        'user_role':'Corrector',
        'version':'2',
        'stage':'verifier',
        'turn_in':'05 September,2020'
    },
    {
        'name': 'Ryan',
        'user_role': 'Corrector',
        'version': '1',
        'stage': 'verifier',
        'turn_in': '06 September, 2020'
    }
]
def home(request):
    context = {
        'projects': projects
    }
    return render(request,'IIT_OpenOCR/home.html',context)

def about(request):
    return render(request, 'IIT_OpenOCR/about.html', {'title':'About'})
