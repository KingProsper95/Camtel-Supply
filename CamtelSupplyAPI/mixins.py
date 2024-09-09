from rest_framework import permissions

class AdminEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser]

