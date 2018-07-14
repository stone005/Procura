from django import forms
from .models import Pratica

class Praticaform(forms.ModelForm):
	class Meta:
		model = Pratica
		fields = [
			'PR_prot',
			'PR_tipologia',
			'PR_agente',
			'PR_magistrato',
			'PR_rgnr',
			'PR_fncr',
			'PR_data_delega',
			'PR_indagati',
			'PR_attivita',
			'PR_data_restituzione',
			'PR_note'
		]
