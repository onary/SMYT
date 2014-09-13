from django import forms

def create_form(model, field_names):
    class Meta:
        pass
    setattr(Meta, 'model', model)
    setattr(Meta, 'include', field_names)

    return type('DynamicForm', (forms.ModelForm,), {'Meta': Meta})

