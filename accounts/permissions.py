from rest_framework import permissions


class IsTeacherOrAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        
        return request.user and (request.user.is_staff or request.user.role.name == 'teacher')
    

class IsAssistantTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role.name == 'assistant'
    

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.role.name == 'student'
        return request.user and (request.user.is_staff or request.user.role.name in ('teacher', 'assistant'))