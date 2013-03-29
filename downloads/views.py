from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    html_template="downloads/index.html"
    # Request context object is required for using TEMPLATE_CONTEXT_PROCESSORS, i.e using STATIC_URL etc in templates
    context=RequestContext(request)
    context_dict = {
      "current_version":"2.4", 
      "release_date":"2nd Feb 2013",
      "release_notes_page":"ReleaseNotes_2.4"
    }
    return render_to_response(html_template, dictionary=context_dict, 
                              context_instance=context)