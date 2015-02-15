from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from serializers import UserSerializer, GroupSerializer, CustomerSerializer, ProjectSerializer, CompanySerializer, TimesheetSerializer, HourSerializer
from models import Customer, Project, Timesheet, Hour, Company
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import obtain_auth_token
from permissions import OwnerOrAdminPermission


@api_view(['POST'])
def token_view(request):
    '''
    API endpoint that allows users to get a token
    ---
    parameters:
        - name: username
          description: The username you want to get the token
        - name: password
          description: Password of the user
          type: password
    '''
    return obtain_auth_token(request)



@api_view(['GET'])
def me_view(request):
    '''
    API endpoint that gives the current user data
    ---
    serializer: UserSerializer
    '''
    serializer = UserSerializer(request.user,context={'request': request})
    return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class TimesheetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows timesheets to be viewed or edited.
    """
    permission_classes = (IsAuthenticated, OwnerOrAdminPermission)
    serializer_class = TimesheetSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = Timesheet.objects.filter(user=user.id)
        return queryset


class HourViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hours to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Hour.objects.all()
    serializer_class = HourSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customer to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

