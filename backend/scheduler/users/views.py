from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

import logging
logger = logging.getLogger(__name__)







from .models import (
    DEO, Advisor, Department, Year,
    Batch, Section, Teacher, Room, Course,
    TeacherCourseAssignment, BatchCourseTeacherAssignment
)
from .serializers import (
    DEOLoginSerializer, AdvisorSerializer,
    DepartmentSerializer, YearSerializer, BatchSerializer,
    SectionSerializer, TeacherSerializer, RoomSerializer,
    CourseSerializer, TeacherCourseAssignmentSerializer,
    BatchCourseTeacherAssignmentSerializer, AdvisorLoginSerializer, AdvisorCreateSerializer
)

class AdvisorListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow DEO to see advisors that belong to their department.
        # Assumes that the DEO’s profile is accessible via request.user.deo.
        if self.request.user.role != 'deo':
            return Advisor.objects.none()
      
        return Advisor.objects.all()

    def get_serializer_class(self):
        # Use the read serializer for GET requests and the create serializer for POST.
        if self.request.method == "GET":
            return AdvisorSerializer  # This serializer returns 'id' and nested user data.
        return AdvisorCreateSerializer

    def perform_create(self, serializer):
        # Automatically assign the DEO based on the logged-in user
        deo = self.request.user.deo
        serializer.save(deo=deo)

class AdvisorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AdvisorCreateSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        if self.request.user.role != 'deo':
            return Advisor.objects.none()
        return Advisor.objects.all()

    def destroy(self, request, *args, **kwargs):
        # Get the advisor instance
        advisor = self.get_object()
        # Delete the associated CustomUser record
        advisor.user.delete()
        # The Advisor record will be deleted automatically due to cascade.
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AdvisorLoginView(generics.GenericAPIView):
    serializer_class = AdvisorLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)
        return Response({
            'refresh': str(refresh),
            'access': access,
            'username': user.username,
            'role': user.role
        }, status=status.HTTP_200_OK)
class DEOLoginView(generics.GenericAPIView):
    serializer_class = DEOLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

       
        if user.role != 'deo':
            return Response(
                {'error': 'Access denied. Only users with DEO role can log in.'},
                status=status.HTTP_403_FORBIDDEN
            )

        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)

        return Response({
            'refresh': str(refresh),
            'access': access,
            'username': user.username,
            'role': user.role
        }, status=status.HTTP_200_OK)

class AdvisorLogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh_token')
            if not refresh_token:
                return Response({"error": "Refresh token not provided."}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"success": "Successfully logged out."}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({"error": "Token is invalid or expired."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DEOLogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh_token')
            if not refresh_token:
                return Response({"error": "Refresh token not provided."}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"success": "Successfully logged out."}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({"error": "Token is invalid or expired."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class BaseListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

class BaseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]


class DepartmentListCreateView(BaseListCreateView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    

class DepartmentRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class YearListCreateView(BaseListCreateView):
    queryset = Year.objects.all()
    serializer_class = YearSerializer

class YearRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = Year.objects.all()
    serializer_class = YearSerializer



class BatchListCreateView(BaseListCreateView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class BatchRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer



class SectionListCreateView(BaseListCreateView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class SectionRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer



class TeacherListCreateView(BaseListCreateView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer



class RoomListCreateView(BaseListCreateView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer



class CourseListCreateView(BaseListCreateView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class TeacherCourseAssignmentListCreateView(BaseListCreateView):
    queryset = TeacherCourseAssignment.objects.all()
    serializer_class = TeacherCourseAssignmentSerializer

class TeacherCourseAssignmentRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = TeacherCourseAssignment.objects.all()
    serializer_class = TeacherCourseAssignmentSerializer


class BatchCourseTeacherAssignmentListCreateView(BaseListCreateView):
    queryset = BatchCourseTeacherAssignment.objects.all()
    serializer_class = BatchCourseTeacherAssignmentSerializer

class BatchCourseTeacherAssignmentRetrieveUpdateDestroyView(BaseRetrieveUpdateDestroyView):
    queryset = BatchCourseTeacherAssignment.objects.all()
    serializer_class = BatchCourseTeacherAssignmentSerializer
