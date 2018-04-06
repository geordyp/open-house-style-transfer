from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

import re
import base64
import os.path
from PIL import Image
from .util import pipeline, makeCopyOfOutput


def indexView(request):
    """
    Tells the user about the project and how it works
    """
    return render(request, 'styletransfer/index.html')


def formView(request):
    """
    Displays the form for user input
    """
    if request.method == 'POST':
        if 'styleOption' not in request.POST:
            return render(request,
                          'styletransfer/form.html',
                          {
                            'errorStyle':"Error: Please select a style"
                          },
                          status=400)
        else:
            request.session['styleSelected'] = request.POST['styleOption']

        if 'snapShot' in request.POST and request.POST['snapShot'] != "":
            imageData = re.search(r'base64,(.*)', request.POST['snapShot']).group(1)
            with open('static/styletransfer/images/input.jpg', 'wb') as f:
                f.write(base64.b64decode(imageData))
        elif 'fileUpload' in request.FILES and request.FILES['fileUpload'] is not None:
            with open('static/styletransfer/images/input.jpg', 'wb') as f:
                f.writelines(request.FILES['fileUpload'].readlines())
        else:
            return render(request,
                          'styletransfer/form.html',
                          {
                            'errorImage':"Error: Please take a picture or upload an image"
                          },
                          status=400)

        # convert image to RGB
        content_rgb_image = Image.open('static/styletransfer/images/input.jpg').convert('RGB')
        content_rgb_image.save('static/styletransfer/images/input.jpg')

        # run style transfer, create output file
        pipeline("python3 styletransfer/nn/neural_style.py eval --content-image static/styletransfer/images/input.jpg --model static/styletransfer/models/%s.pth --output-image static/styletransfer/images/output.jpg --cuda 0" % request.POST['styleOption'])
        makeCopyOfOutput()

        return HttpResponseRedirect(reverse('views.result', args=()))
    else:
        return render(request, 'styletransfer/form.html')


def resultView(request):
    """
    Displays the result of the style transfer
    """
    style = str(request.session['styleSelected'])
    if request.method == 'POST' and request.POST['styleOption'] != style:
        # run style transfer, create output file
        style = request.session['styleSelected'] = request.POST['styleOption']
        pipeline("python3 styletransfer/nn/neural_style.py eval --content-image static/styletransfer/images/input.jpg --model static/styletransfer/models/%s.pth --output-image static/styletransfer/images/output.jpg --cuda 0" % style)

    p = "static/styletransfer/images/"
    if style is not None and os.path.isfile(p + "input.jpg") and os.path.isfile(p + "output.jpg"):
        return render(request,
                      'styletransfer/result.html',
                      {
                        'style':style
                      })
    else:
        return HttpResponseRedirect(reverse('views.form', args=()))
