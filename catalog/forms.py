from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):
    forbidden_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == "category":
                field.widget.attrs.update({
                    "class": "form-select"
                })
            else:
                field.widget.attrs.update({
                    "class": "form-control"
                })

                
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data["name"].casefold()

        for word in self.forbidden_words:
            if word.casefold() in name:
                raise ValidationError(
                    f"Название содержит запрещённое слово: {word}"
                )

        return self.cleaned_data["name"]

    def clean_description(self):
        description = self.cleaned_data["description"].casefold()

        for word in self.forbidden_words:
            if word.casefold() in description:
                raise ValidationError(
                    f"Описание содержит запрещённое слово: {word}"
                )

        return self.cleaned_data["description"]

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной.")
        return price