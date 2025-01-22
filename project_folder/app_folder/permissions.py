import copy
from rest_framework import permissions

class CustomDjangoModelPermissions(permissions.DjangoModelPermissions):
    
    def __init__(self):
        self.perms_map = copy.deepcopy(self.perms_map)
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
        self.perms_map['DELETE'] = ['%(app_label)s.delete_%(model_name)s']