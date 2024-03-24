from django.views.generic import ListView
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Document, Text
from .utils import (remove_punctuation, count_words,
                    create_list_from_dict, calculate_idf)


class Index(ListView):
    template_name = 'text_recognition/text_recognition.html'
    queryset = Document.objects.prefetch_related('texts').all()
    paginate_by = 5

    def post(self, request, *args, **kwargs):
        if request.FILES:
            uploaded_file = request.FILES['f']
            with uploaded_file as file:
                file_content = file.read().decode('utf-8')
                words = remove_punctuation(file_content)

                document_instance = Document.objects.create(
                    document_name=uploaded_file)
                words_count = count_words(words)
                words_list = create_list_from_dict(
                    words_count, document_instance)

                total_words = sum(words_count.values())

                Text.objects.bulk_create(words_list)

                for text_instance in Text.objects.filter(
                    doc_name=document_instance
                ):
                    text_instance.term_frequency = (text_instance.word_quantity
                                                    / total_words)
                    text_instance.save()

                document_instance.total_words = total_words
                document_instance.save()

                for text_instance in Text.objects.filter(
                    doc_name=document_instance
                ):
                    text_instance.inverse_document_frequency = calculate_idf(
                        text_instance.word)

                    text_instance.save()

            return HttpResponseRedirect(reverse('index'))
        return super(Index, self).get(request, *args, **kwargs)
