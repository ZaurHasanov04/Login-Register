from django.db import models
from django.contrib.auth.models import AbstractUser
import jwt
from datetime import datetime, timedelta
from django.core.management import settings
# Create your models here.


class User(AbstractUser):
    phone=models.IntegerField(blank=True, null=True)
    



class UserVerify(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    token=models.CharField(blank=True, null=True, max_length=280)
    date=models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.token

    def save(self, *args, **kwargs):
        self.token = ''

        if not self.token:
            self.token=self._creates_verify()

        if not self.date:
            self.date= datetime.now() + timedelta(minutes=1)

        super().save(*args, **kwargs)

    def _creates_verify(self):
        dt=datetime.now() + timedelta(days=60)
        hashing=jwt.encode(
            {
                'id':self.id,
                'exp' : int(dt.timestamp())
            }, key=settings.SECRET_KEY, algorithm="HS256"
        )

        return hashing
                
    

