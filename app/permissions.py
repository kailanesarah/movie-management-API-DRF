from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        """Verifica se o usuário tem permissão para acessar a view."""
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )

        if not model_permission_codename:
            return False

        return request.user.has_perm(model_permission_codename)

    def __get_model_permission_codename(self, method, view):
        """Gera a string de permissão no formato 'app_name.action_model'."""
        try:
            model_name = view.queryset.model._meta.model_name
            app_name = view.queryset.model._meta.app_label
            action = self.__get_method_request(method)

            if not action:
                return None

            return f'{app_name}.{action}_{model_name}'
        except AttributeError:
            return None

    def __get_method_request(self, method):
        """Mapeia os métodos HTTP para as ações de permissão do Django."""
        request_methods = {
            'GET': 'view',
            'OPTIONS': 'view',
            'HEAD': 'view',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'POST': 'add'
        }
        return request_methods.get(method, None)
