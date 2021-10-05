from django.contrib.auth.backends import ModelBackend
from accounts.models import ManagerModel

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = ManagerModel.objects.get(email__iexact=email)
        except ManagerModel.DoesNotExist:
            ManagerModel().set_password(password)
            return
        except ManagerModel.MultipleObjectsReturned:
            user = ManagerModel.objects.filter(email__iexact=email).order_by('id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user