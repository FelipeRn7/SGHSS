from rest_framework.permissions import BasePermission

class IsAdminUserType(BasePermission):
    """
    Permite acesso apenas a usuários com o tipo de usuário 'admin'.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.tipo == 'admin'