from django import forms
from django.forms import ValidationError

def solo_caracteres(value):
    if any(char.isdigit() for char in value ):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                            code='Error1',
                            params={'valor':value})
        #raise ValidationError('El nombre no puede contener números.')


class ContactoForm(forms.Form):
    nombre = forms.CharField(
            label='Nombre',
            required=False,
            validators=(solo_caracteres,),
            widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese solo texto'})
            )
    email = forms.EmailField(
            label='Email',
            max_length=50,
            widget= forms.TextInput(attrs={'class':'form-control','type':'email'})
            )
    asunto = forms.CharField(
            label='Asunto',
            max_length=100,
            widget= forms.TextInput(attrs={'class':'form-control'})
        )
    mensaje = forms.CharField(
            label='Mensaje',
            max_length=500,
            widget=forms.Textarea(attrs={'class':'form-control','rows':5}))
    suscripcion = forms.BooleanField(
        label='Deseo suscribirme a las novedades de codo a codo',
        required=False,
        widget=forms.CheckboxInput(attrs={'class':'form-check-input','value':1})
    )

    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError("Debes especificar mejor el mensaje que nos envias")
        return data
    
    def clean(self):
        cleaned_data = super().clean()
        mensaje = cleaned_data.get("mensaje")
        asunto = cleaned_data.get("asunto")

        if "ayuda" not in asunto or "ayuda" not in mensaje:
            msg = "Debe agregar la palabara 'ayuda' en el campo."
            self.add_error('asunto', msg)
            self.add_error('mensaje', msg)


