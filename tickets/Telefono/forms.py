from django import forms

class TelForm(forms.Form):
    telefono = forms.CharField(max_length=9, initial = 'Ingrese un numero')
    def clean(self):
        datos = super(TelForm, self).clean()
        tel = datos.get('telefono')
     #   sector = datos.get('sector')
        errores = []
        if tel:
            if not tel.isdigit():
                errores.append('El telefono tiene que ser solo numeros')
            if len(tel) != 9:
                errores.append('El telefono tiene que tener un largo de 9.')
            if errores:
                raise forms.ValidationError(errores)
            return datos
        
class PinField(forms.IntegerField):
    def to_python(self, value):
        try:
            value = int(value)
        except ValueError: 
            raise forms.ValidationError('Pin invalido ingrese solo digitos!')
        return value
    
    def validate(self, value):
        if value is None:
            return value 
        if len(str(value)) != 4: 
            raise forms.ValidationError('Largo ({0}) de PIN invalido'.format(len(str(value)))) 
    
    def clean(self, value):
        value = super(PinField,self).clean(value)
        from tickets.pin import Pin
        try:
            pin = Pin.objects.get(numero = value)
        except Pin.DoesNotExist:
            raise forms.ValidationError('PIN ({0}) no existe'.format(value))
        return value
    
class PinForm(forms.Form):
    pin = PinField()
    tel = forms.CharField(widget = forms.HiddenInput())
    
    def clean(self): 
        datos = super(PinForm, self).clean()
        return datos