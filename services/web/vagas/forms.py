from django import forms

class CadastroVagasForm(forms.Form):
    """Form for submitting job opportunities."""
    empresa_nome = forms.CharField(label='Nome da empresa')
    empresa_endereco = forms.CharField(label='Endereço da empresa')
    empresa_email = forms.EmailField(label='Email da empresa')
    empresa_site = forms.URLField(label='Site da empresa')
    empresa_telefone_celular = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}), label='Telefone celular')
    empresa_telefone_comercial = forms.CharField(widget=forms.TextInput(attrs={'type': 'tel'}), label='Telefone comercial')
    cargo_titulo = forms.CharField(label='Título do cargo')
    cargo_descricao = forms.CharField(widget=forms.Textarea, label='Descrição do cargo')
    site_referencia = forms.URLField(label='Site de referência')
    data_hora_entrevista = forms.CharField(widget=forms.DateTimeInput(attrs={'type': 'datetime'}), label='Entrevista em')