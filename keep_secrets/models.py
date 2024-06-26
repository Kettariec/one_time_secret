from django.db import models
from cryptography.fernet import Fernet
from django.core.validators import MinValueValidator, MaxValueValidator


class EncryptedTextField(models.TextField):
    """Custom field that encrypts text
     using the cryptography library"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cipher_suite = Fernet(Fernet.generate_key())

    def to_python(self, value: str):
        if not value:
            return value
        return self.cipher_suite.decrypt(value.encode()).decode()

    def from_db_value(self, value: str, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value: str):
        if not value:
            return value
        return self.cipher_suite.encrypt(value.encode()).decode()


class Secret(models.Model):
    text = EncryptedTextField()
    code = models.CharField(max_length=10, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    days = models.PositiveIntegerField(default=7,
                                       validators=[MinValueValidator(1),
                                                   MaxValueValidator(7)],
                                       verbose_name='secret lifetime (in days)')

    class Meta:
        verbose_name = 'secret'
        verbose_name_plural = 'secrets'
