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
    if request.method == 'POST':
        if 'styleOption' not in request.POST:
            # TODO add error message
            return HttpResponseRedirect(reverse('views.form', args=()))

        if 'snapshot' in request.POST and request.POST['snapshot'] != "":
            imageData = re.search(r'base64,(.*)', request.POST['snapshot']).group(1)
            userImage = open('static/styletransfer/images/userImage.png', 'wb')
            userImage.write(base64.b64decode(imageData))
            userImage.close()
        elif 'fileupload' in request.FILES and request.FILES['fileupload'] is not None:
            userImage = open('static/styletransfer/images/userImage.png', 'wb')
            userImage.writelines(request.FILES['fileupload'].readlines())
            userImage.close()
        else:
            # TODO add error message
            return HttpResponseRedirect(reverse('views.form', args=()))

        #########################
        # TODO run style transfer
        #########################

        return render(request,
                      'styletransfer/result.html',
                      {
                        'styleSelection':request.POST['styleOption'],
                        'result':'http://via.placeholder.com/200x280'
                      })
    else:
        return HttpResponseRedirect(reverse('views.form', args=()))
