from deploytodotaskerapp.models import ImageStore,User
from deploytodotaskerapp.forms import ImageUploadForm
from django.http import JsonResponse
from django.http import HttpResponse
from oauth2_provider.models import AccessToken
from rest_auth.models import TokenModel
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
@csrf_exempt
def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            
            
            try:
               access_token = TokenModel.objects.get(key = form.cleaned_data['token'])
            except TokenModel.DoesNotExist:
               access_token = AccessToken.objects.get(token = form.cleaned_data['token'],expires__gt = timezone.now())
            m = ImageStore()
            m.user=access_token.user
            m.image = form.cleaned_data['image']
            print(form.cleaned_data['token'])
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')
