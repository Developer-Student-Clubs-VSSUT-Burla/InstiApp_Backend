from src.serializers import *
from src.models import *
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .permissions import UserPermission
from src.serializers import UserSerializer, UserSerializerWithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
import pdb


class EventViewset(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [UserPermission]

    def list(self, request):
        events = event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        try:
            eventobj = event.objects.get(_id=pk)
        except event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EventSerializer(eventobj)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        newEvent = event.objects.create(
            name=data['name'],
            description=data['description'],
            guestdetails=data['guestdetails'],
            expected_no_of_participants=data['expected_no_of_participants'],
            date=data['date'],
            venue=data['venue'],
            club_name=data['club_name'],
            event_time=data['event_time'],
            event_type=data['event_type'],
            link=data['link'])

        newEvent.save()
        serializer = EventSerializer(newEvent)
        return Response(serializer.data)

    def get_queryset(self):
        return event.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    # permission_classes=[UserPermission]

    def list(self, request):
        projects = project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        try:
            project_obj = project.objects.get(_id=pk)
        except project.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = ProjectSerializer(project_obj)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        user = request.user
        # pdb.set_trace()
        NewProjectObj = project.objects.create(name=data['name'],
                                               description=data['description'],
                                               tags=data['tags'],
                                               contributor=user,
                                               link=data['link'])

        print(type(data['team_members']))
        team_members_list = data['team_members'].split(',')
        print(team_members_list)
        for reg in team_members_list:
            member = User.objects.get(regno=reg)
            # print("reg=>",reg)
            print(member)
            NewProjectObj.team_members.add(member)

        # pdb.set_trace()
        NewProjectObj.save()
        serializer = ProjectSerializer(NewProjectObj)
        return Response(serializer.data)

    def get_queryset(self):
        return project.objects.all()


class FeedViewSet(viewsets.ModelViewSet):
    serializer_class = FeedSerializer

    # permission_classes=[UserPermission]

    def list(self, request):
        query = request.query_params.get('keyword')

        queryset = feed.objects.all()

        if (query is not None):
            queryset = queryset.filter(title__icontains=query)
            print(queryset)
        else:
            print("QuerySet not none")
        serializer = FeedSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        try:
            feed_obj = feed.objects.get(_id=pk)
        except feed.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = FeedSerializer(feed_obj)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        user = request.user
        # pdb.set_trace()
        NewFeedObj = feed.objects.create(title=data['title'],
                                         description=data['description'],
                                         contributor=user,
                                         category='category')
        team_members_list = data['team_members'].split(',')
        print(data)
        # print(team_members_list)
        for reg in team_members_list:
            member = User.objects.get(regno=reg)
            # print("reg=>",reg)
            print(member)
            NewFeedObj.team_members.add(member)

        # `choice=data['choices']
        # pdb.set_trace()

        # pdb.set_trace()
        NewFeedObj.save()
        serializer = FeedSerializer(NewFeedObj)
        return Response(serializer.data)

    def get_queryset(self):
        return project.objects.all()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        print("attrs=>", attrs)

        return data


class MyTokenObtainPairView(TokenObtainPairView):

    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):
    data = request.data
    print((data['name']))
    user = User.objects.create(name=data['name'],
                               username=data['emailid'],
                               branch=data['branch'],
                               regno=data['regno'],
                               about=data['about'],
                               fa=data['fa'],
                               password=make_password(data['password']))

    serializer = UserSerializerWithToken(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
