from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def intro(request):
    return render(request,'api_auth/intro.html')



def welcome(request):
    return render (request, 'api_auth/welcome.html')


from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Token auth view already provided by DRF
# We will reuse obtain_auth_token for handling the login part

# View to return username for authenticated user
@api_view(['GET'])
def welcome_details(request):
    if request.user.is_authenticated:
        return Response({
            'username': request.user.username
        })
    else:
        return Response({'detail': 'Invalid credentials'}, status=401)