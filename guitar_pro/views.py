from django.shortcuts import render

# Create your views here.

# a view to render the guitar pro page
def guitar_pro(request):
    
    return render(request, 'guitar_pro/score_player.html')