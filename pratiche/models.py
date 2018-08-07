from django.db import models
from django.db.models import Max


# Create your models here.
class Pratica(models.Model):
	PR_prot = models.IntegerField(null=False, blank=False)
	PR_timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	tipo = (
			(1, 'Penale'),
			(2, 'Civile'),
		)

	PR_tipologia = models.IntegerField(choices=tipo, null=False, blank=False)
	PR_agente = models.OneToOneField('Agente', on_delete=models.SET_NULL, null=True, blank=True)
	PR_magistrato = models.OneToOneField('Magistrato', on_delete=models.SET_NULL, null=True, blank=True)
	PR_rgnr = models.CharField(max_length=10)

	xfncr = (
			(1, 'Ignoti'),
			(2, 'FNCR'),
		)

	PR_fncr = models.IntegerField(choices=xfncr, null=False, blank=False)
	PR_data_delega = models.DateField(auto_now=False, auto_now_add=False)
	PR_indagati = models.ForeignKey('Indagato', on_delete=models.SET_NULL, null=True, blank=True)
	PR_attivita = models.TextField(max_length=1000, null=True, blank=True)
	PR_data_restituzione = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
	PR_note = models.TextField(max_length=1000, null=True, blank=True)

	def __str__(self):
		return	str(self.PR_prot)

	# def Max_penale(self):
	# 	Pratica.objects.all().filter(PR_tipologia=1).aggregate(Max('PR_prot'))

class Agente(models.Model):
	AG_nome = models.CharField(max_length=50, null=True, blank=True)
	AG_cognome = models.CharField(max_length=50, null=False, blank=False)
	AG_matricola = models.PositiveIntegerField(null=False, blank=False)

	def __str__(self):
		return self.AG_cognome


class Magistrato(models.Model):
	MA_cognome = models.CharField(max_length=10 , null=False, blank=False)

	def __str__(self):
		return self.MA_cognome


class Indagato (models.Model):
	IN_nome = models.CharField(max_length=50, null=False, blank=False)
	IN_cognome = models.CharField(max_length=50, null=False, blank=False)
	IN_data_nascita = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False)

	def __str__(self):
		return self.IN_cognome
