from django.db import models

NATIONALITY = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
    ('FRANCE', 'França'),
    ('GERMANY', 'Alemanha'),
    ('MEXICO', 'México'),
    ('UK', 'Reino Unido')
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
                                max_length=100,
                                choices=NATIONALITY,
                                blank=True,
                                null=True,
                                )

    def __str__(self) -> str:
        return self.name