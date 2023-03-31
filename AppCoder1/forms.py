from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField(min_length=2, max_length=50)
    camada = forms.IntegerField(min_value=1000)

class BusqCursoForm(forms.Form):
    nombre = forms.CharField(min_length=2, max_length=50)

class EstudianteForm(forms.Form):
    apellido = forms.CharField(max_length=50,)
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()

class BusqEstudianteForm(forms.Form):
    apellido = forms.CharField(min_length=2, max_length=50)


class ProfesorForm(forms.Form):
    profesion = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=50)
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()

class BusqProfesorForm(forms.Form):
    profesion = forms.CharField(min_length=2, max_length=50)
