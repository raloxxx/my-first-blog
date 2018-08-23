from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def post_list(request):
    template = loader.get_template('blog/post_list.html')
    context = {
        'name': "juan manuel",
    }
    return HttpResponse(template.render(context, request))
