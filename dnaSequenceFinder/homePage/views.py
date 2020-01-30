from django.shortcuts import render
from homePage.forms import inputForm
from searchHistory.models import Search
from homePage.proteinFinder import findProtein


def homePage(request):
    sequence = Search.objects
    form = inputForm()
    if request.method == "POST":
        form = inputForm(request.POST)
        if form.is_valid():
            seq = findProtein(form.cleaned_data["sequence"]);
            seq.save()
            context = {"sequenceName": seq.sequence,"proteinName":seq.proteinName,"proteinIndex":seq.proteinIndex, "form": form}
            return render(request, "homePage.html", context)

    context = {"sequence": sequence, "form": form}
    return render(request, "homePage.html", context)
