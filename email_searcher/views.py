import json

from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings
from email_searcher.forms import nameSearcher
from rapportive_extension.rapportive import get_oauth, name2email, checkEmailExistance


def home(request):
    return render(request, 'email_searcher/base.html', {'form':nameSearcher()})

def check(request):

    def beautiful_data(data):

        html = ""

        for i in data :
            if i[1] != 0:
                color = "#2ecc71" if i[1] == 1 else "#f39c12"
                html += '<p><a style="color:'+color+';" href="'+i[2]+'">'+i[0]+'</a></p>'
            else:
                html += "<p style='color:#e74c3c'>"+i[0]+"</p>"

        return html

    if request.method == 'POST':

        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        domain = request.POST.get('company_domain')

        if True:

            o_auth = get_oauth(settings.LI_AT)

            if o_auth != "":

                possible_emails = name2email(fn,ln,domain)
                check_emails = checkEmailExistance(o_auth,possible_emails,fn,ln)

                return HttpResponse(beautiful_data(check_emails))
            else:
                return HttpResponse("<p>Impossible to Obtain Oauth</p>")

        else:
            return HttpResponse("<p>Invalid Form</p>")

