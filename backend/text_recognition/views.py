from django.shortcuts import get_object_or_404
from django.views.generic import ListView, UpdateView, TemplateView
from django.contrib.auth import get_user_model

from .models import Text
from .utils import remove_punctuation, count_words, create_list_from_dict


User = get_user_model()


class Index(ListView):
    template_name = 'text_recognition/text_recognition.html'
    queryset = Text.objects.all()
    paginate_by = 30

    def post(self, request, *args, **kwargs):
        if request.FILES:
            uploaded_file = request.FILES['f']
            with uploaded_file as file:
                file_content = file.read().decode('utf-8')
                words = remove_punctuation(file_content)
                words_list = create_list_from_dict(count_words(words))
                Text.objects.bulk_create(words_list)
        return self.get(request, *args, **kwargs)
