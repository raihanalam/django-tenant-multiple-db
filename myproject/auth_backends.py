# from django.contrib.auth.backends import ModelBackend

# class MultiDBModelBackend(ModelBackend):
#     def get_user(self, user_id):
#         try:
#             return self.user_class.objects.using('user_db').get(pk=user_id)
#         except self.user_class.DoesNotExist:
#             return None


# myapp/auth_backends.py

# from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth import get_user_model

# class AdminDatabaseBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         User = get_user_model()
#         try:
#             user = User.objects.using('admin_db').get(username=username)
#             if user.check_password(password):
#                 return user
#         except User.DoesNotExist:
#             return None

#     def get_user(self, user_id):
#         User = get_user_model()
#         try:
#             return User.objects.using('admin_db').get(pk=user_id)
#         except User.DoesNotExist:
#             return None

