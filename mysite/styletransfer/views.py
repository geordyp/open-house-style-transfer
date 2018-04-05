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
    if request.method == 'POST':
        if 'styleOption' not in request.POST:
            return render(request,
                          'styletransfer/form.html',
                          {
                            'errorStyle':"Please select a style"
                          },
                          status=400)
        else:
            request.session['styleSelected'] = request.POST['styleOption']

        if 'snapShot' in request.POST and request.POST['snapShot'] != "":
            imageData = re.search(r'base64,(.*)', request.POST['snapShot']).group(1)
            userImage = open('static/styletransfer/images/userImage.png', 'wb')
            userImage.write(base64.b64decode(imageData))
            userImage.close()
        elif 'fileUpload' in request.FILES and request.FILES['fileUpload'] is not None:
            userImage = open('static/styletransfer/images/userImage.png', 'wb')
            userImage.writelines(request.FILES['fileUpload'].readlines())
            userImage.close()
        else:
            return render(request,
                          'styletransfer/form.html',
                          {
                            'errorImage':"Please take a picture or upload an image"
                          },
                          status=400)

        #########################
        # TODO run style transfer, create result file
        #########################

        return HttpResponseRedirect(reverse('views.result', args=()))
    else:
        return render(request, 'styletransfer/form.html')


def ResultView(request):
    """
    Displays the result of the style transfer
    """
    # if there is a userImage, styleSelection, and resultImage
    if 'styleSelected' in request.session:
        return render(request,
                      'styletransfer/result.html',
                      {
                        'styleSelection':request.session['styleSelected'],
                        'result':'http://via.placeholder.com/200x280'
                      })
    else:
        return HttpResponseRedirect(reverse('views.form', args=()))
