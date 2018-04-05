from django.shortcuts import render
from django.http import HttpResponse


def IndexView(request):
    """
    Tells the user about the project and how it works
    """
    return render(request, 'styletransfer/index.html')


def FormView(request):
    """
    Gets the selfie from the user
    """
    # display form
    return render(request, 'styletransfer/form.html')


def ResultView(request):
    """
    Displays the result of the style transfer
    """
    # receive inputs and run style transfer
    # display results
    return render(request, 'styletransfer/result.html')
