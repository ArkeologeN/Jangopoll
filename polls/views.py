# Create your views here.
from django.template import Context, loader
from polls.models import Poll
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.core.urlresolvers import reverse

def index(request):
    latest_poll_list = Poll.objects.all()
    return render_to_response('polls/index.html', {'latest_poll_list' : latest_poll_list})
def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll' : p},
                              context_instance = RequestContext(request))

def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response("polls/results.html", {"poll" : p})

def vote(request, poll_id):
    #return HttpResponse("You're voting on poll %s." % poll_id)
    p = get_object_or_404(Poll,pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render_to_response("poll/vote.html", {
                                'poll': p,
                                'error_message' : "You didn't selected the choice!"
                }, context_instance = RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
    