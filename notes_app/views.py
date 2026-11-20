from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from notes_app.serializers import RegisterSerializer,NotesSerializer,TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from notes_app.models import NotesDb,TaskDb

# Create your views here.
class RegistrationView(APIView):
    def post(self,request):
        serializer_instance=RegisterSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data={
                "Message":"Registration Succesfull..!!"
            })
        else:
            return Response(data=serializer_instance.errors)

class NotesListCreateView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        notes=NotesDb.objects.filter(user=request.user)
        serializer_instance=NotesSerializer(notes,many=True)
        return Response(serializer_instance.data)

    def post(self,request):
        serializer_instance=NotesSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class NotesRetriveUpdateDeleteView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request,pk):
        notes_obj=get_object_or_404(NotesDb,id=pk,user=request.user)
        serializer_instance=NotesSerializer(notes_obj)
        return Response(serializer_instance.data)

    def put(self,request,pk):
        notes_obj=get_object_or_404(NotesDb,id=pk,user=request.user)
        serializer_instance=NotesSerializer(notes_obj,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        return Response(serializer_instance.errors)

    def delete(self,request,pk):
        notes_obj=get_object_or_404(NotesDb,id=pk,user=request.user)
        notes_obj.delete()
        return Response({
            "Message":"Deleted Successfully.."
        })
    #API LOGOUT

class LOGOUTVIEW(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        request.user.auth_token.delete()
        return Response({
            "Message":"Logout Successfully..!"
        })



#TASK MANAGEMENT
class TaskListCreateView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        task_obj=TaskDb.objects.filter(user=request.user)
        serializer_instance=TaskSerializer(task_obj,many=True)
        return Response(serializer_instance.data)

    def post(self,request):
        serializer_instance=TaskSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
        
    
class TaskRetrieveDeleteView(APIView):
    permission=[IsAuthenticated]
    def get(self,request,pk):
        task_obj=get_object_or_404(TaskDb,id=pk,user=request.user)
        serializer_instance=TaskSerializer(task_obj)
        return Response(serializer_instance.data)

    def put(self,request,pk):
        task_obj=get_object_or_404(TaskDb,id=pk,user=request.user)
        serializer_instance=TaskSerializer(task_obj,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

    def delete(self,request,pk):
        task_obj=get_object_or_404(TaskDb,id=pk,user=request.user)
        task_obj.delete()
        return Response(
            {
                "Message":"Deleted Succesfully"
            }
        )









