from django.views import generic
from django.urls import reverse_lazy
from .models import Minutes
from .forms import MinutesForm


# Minutesの一覧表示機能
class MinutesListView(generic.ListView):
    model = Minutes
    paginate_by = 5


# Minutesの詳細表示機能
class MinutesDetailView(generic.DetailView):
    model = Minutes


# Minutesの作成機能
class MinutesCreateView(generic.CreateView):
    model = Minutes
    form_class = MinutesForm
    success_url = reverse_lazy('minutes:list')


# Minutesの編集機能
class MinutesUpdateView(generic.UpdateView):
    model = Minutes
    form_class = MinutesForm
    success_url = reverse_lazy('minutes:list')


# Minutesの削除機能
class MinutesDeleteView(generic.DeleteView):
    model = Minutes
    success_url = reverse_lazy('minutes:list')