from rest_framework import  permissions

class UpdateOwnProfile(permissions.BasePermission):
    #Allow user to edit their own profiles

    def has_object_permission(self,request,view,obj):
        #Check user is trying to edit their own profile
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    #Allow users to update their own status_test
    def has_object_permission(self,request,view,obj):
        #check the user is trying to update their own status_text
        if request.status in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
