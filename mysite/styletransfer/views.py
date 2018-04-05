from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

import re
import base64


def IndexView(request):
    """
    Tells the user about the project and how it works
    """
    return render(request, 'styletransfer/index.html')


def FormView(request):
    """
    Displays the form for user input
    """
    return render(request, 'styletransfer/form.html')


def ResultView(request):
    """
    Displays the result of the style transfer
    """
    if request.method == "POST":
        # TODO further validate input
        if "styleOption" not in request.POST or "snapshot" not in request.POST and "fileUpload" not in request.POST:
           return HttpResponseRedirect(reverse('views.form', args=()))

        imgstr = re.search(r'base64,(.*)', request.POST['snapshot']).group(1)
        output = open('static/styletransfer/images/userImage.png', 'wb')
        output.write(base64.b64decode(imgstr))
        output.close()

        # TODO run style transfer

        # userImage = request.POST['snapshot'] if "snapshot" in request.POST else request.POST['fileUpload']
        return render(request,
                      'styletransfer/result.html',
                      {
                        'styleSelection':request.POST['styleOption'],
                        'result':'http://via.placeholder.com/200x280'
                      })
    else:
        return HttpResponseRedirect(reverse('views.form', args=()))
