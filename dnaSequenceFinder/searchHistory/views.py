from django.shortcuts import render
from searchHistory.models import Search

def searchHistoryIndex(request):
    searches = Search.objects.all()
    context = {
        'searches':searches
    }
    return render(request, 'searchHistoryIndex.html', context)


