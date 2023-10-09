
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle,UserRateThrottle
class StudentList(ListAPIView):
    queryset =Student.objects.all()
    serializer_class =StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope ='viewStu'
    
class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope ='modifyStu'

class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope ='modifyStu'
    
class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope ='modifyStu'


class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    throttle_classes=[ScopedRateThrottle]
   
    


