from rest_framework import permissions

class GenrePermissionClass(permissions.BasePermission):

    message = "You don't have permission to make this action. \
Att. Moderator 😊"

    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return request.user.has_perm('genres.view_genre')

        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')
        
        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('genres.change_genre')
        
        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre')

        return False
    