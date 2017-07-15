from __future__ import absolute_import
from urllib.request import urlopen, HTTPError
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import ChrForm


def index(request):
    if request.method == 'POST':
        form = ChrForm(request.POST)
        if form.is_valid():
            chr_no = form.cleaned_data['chr']
            start = form.cleaned_data['start']
            end = form.cleaned_data['end']
            res = getseq(chr_no, start, end)
            request.session['seq'] = res
            return HttpResponseRedirect(reverse('getsequence:sequence'))
    else:
        form = ChrForm()

    return render(request, 'getsequence/index.html', {'form': form})


def sequence(request):
    try:
        my_seq = request.session['seq']
    except KeyError:
        return HttpResponseRedirect(reverse('getsequence:index'))
    request.session.clear()
    return render(request, 'getsequence/sequence.html', {'seq': my_seq})


def getseq(chr_no, start, end):
    """
    Return the sequence for a region from UCSC MySQL server using the TOGOWS
    API.
    """
    db = 'hg38'
    url = "http://togows.org/api/ucsc/{0}/{1}:{2}-{3}.fasta".format(db, chr_no, start, end)

    try:
        res = urlopen(url).read().decode()
    except HTTPError:
        return "Website under maintenance. Please check back after some time :)"
    if res and start > end:
        return "Value of start co-ordinate greater than the End coordinate. " \
               "Showing you the sequence in Reverse strand \n\n {0}".format(
                res)
    elif res and start < end:
        return res
    else:
        return "Check your input!"
