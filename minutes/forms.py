from django import forms
from .models import Minutes


class MinutesForm(forms.ModelForm):
    class Meta:
        model = Minutes
        # 入力項目から作成日時、更新日時を除外
        exclude = ('created_at', 'updated_at',)