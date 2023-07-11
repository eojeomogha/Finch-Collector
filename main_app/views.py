from django.shortcuts import render

finches = [
  {'name': 'The Finch', 'breed': 'grumpy', 'description': 'Steals finchmas', 'age': 3},
  {'name': 'Finnochio', 'breed': 'puppet', 'description': 'Wants to be a real finch', 'age': 2},
]
# Create your views here.
def home(request):
    # Include an .html file extension
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })