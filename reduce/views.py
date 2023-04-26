from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse, Http404
from .models import UrlRedirect, LogUrl
from django.db.models.functions import TruncDate
from django.db.models import Count
from .generate_code_url import CodeUrl
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.conf import settings
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


def redirect_client(request: HttpRequest, uidb4) -> HttpResponse:
    try:
        url_id = force_str(urlsafe_base64_decode(uidb4))
        url_redirect = get_object_or_404(UrlRedirect , id=url_id)

        _ = LogUrl.objects.create(
                origin=request.META.get('HTTP_REFERER'),
                user_agent=request.META.get('HTTP_USER_AGENT'),
                host=request.META.get('HTTP_HOST'),
                ip=request.META.get('REMOTE_ADDR'),
                url_redirect=url_redirect
            )
        return redirect(url_redirect.destiny)
    except:
            raise Http404()
    

def generate_url(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
            return render(request, 'reduce/index.html')

    elif request.method == 'POST':
        url_content = request.POST.get('url-content', None)

        new_url = UrlRedirect.objects.create(
                destiny = url_content,
        )

        url_code = urlsafe_base64_encode(force_bytes(new_url.id))
        url_detail = f'{reverse("reduce:report_url", kwargs={"uidb4":url_code})}'
        code_url = CodeUrl(new_url)
        path = code_url._generate_url()      #MTM0
        new_url.shortened = path
        new_url.save()
        context = {
             'new_url': path,
             'url_detail':url_detail
        }

        return render(request, 'reduce/success.html', context=context)
    

def report_url(request: HttpRequest, uidb4) -> HttpResponse:
    url_id = force_str(urlsafe_base64_decode(uidb4))
    url_redirect = get_object_or_404(UrlRedirect , id=url_id)
    min_url = url_redirect.shortened

    redirects = list(
        UrlRedirect.objects.filter(
            id=url_id
        ).annotate(
            date=TruncDate('logs__created_at')
        ).annotate(
            clicks=Count('date')
        )
    )

    total_clicks = sum(i.clicks for i in redirects)

    context = {
        'fullpath': url_redirect.destiny,
        'min_url': min_url,
        'redirect_by_date': redirects,
        'total_clicks':total_clicks
        }
    
    return render(request, 'reduce/relatorio.html', context=context)