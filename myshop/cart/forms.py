from django import forms

QUANTIDADE_PRODUTOS_ESCOLHA = [(i,str(i)) for i in range(1,21)]

class AddProdutoCarrinhoForm(forms.Form):
    quantidade = forms.TypedChoiceField(
        choices=QUANTIDADE_PRODUTOS_ESCOLHA,
        coerce=int
    )
    sobrepor = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)