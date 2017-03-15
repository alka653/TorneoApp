from datetime import datetime
from django.db import models

CHOICE_LEVEL = (
	('NP', 'Nivel principiante'),
	('NA', 'Nivel aficionado'),
	('NS', 'Nivel semiprofesional'),
	('NPL', 'Nivel profesional')
)

class Inscritos(models.Model):
	fullname = models.CharField(max_length = 80)
	email = models.EmailField()
	nivel = models.CharField(max_length = 3, choices = CHOICE_LEVEL, default = 'NP')
	date_registry = models.DateField(default = datetime.now)

	def __str__(self):
		return self.fullname