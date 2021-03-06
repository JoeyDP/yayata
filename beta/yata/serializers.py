from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import Customer, Project, Timesheet, Hour, Company

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups', 'is_staff')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')

class CustomerSerializer(serializers.ModelSerializer):
    country =  serializers.CharField()
    class Meta:
        model = Customer
        fields = ('id', 'short_name', 'name', 'country')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'short_name', 'name', 'customer')

class TimesheetSerializer(serializers.ModelSerializer):
    project_name = serializers.StringRelatedField(source='project')
    user_name = serializers.StringRelatedField(source='user')
    company_name = serializers.StringRelatedField(source='company')
    group_name = serializers.StringRelatedField(source='group')
    customer_name = serializers.StringRelatedField(source='project.customer')

    class Meta:
        model = Timesheet
        fields = ('id',
                'month', 'year',
                'project', 'project_name', 'customer_name',
                'company', 'company_name',
                'group', 'group_name',
                'user', 'user_name', 'locked',
                'max_days', 'first_day')

class HourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hour
        fields = ('id', 'task', 'hours', 'hours150', 'hours200', 'hourstravel', 'day')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name',)

