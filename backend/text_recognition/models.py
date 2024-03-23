from django.db import models


class Text(models.Model):
    word = models.CharField('Слово', max_length=150)
    term_frequency = models.IntegerField('Частота слова или TF')
    inverse_document_frequency = models.IntegerField(
        'Oбратная частота документа или IDF', default=0)

    class Meta:
        verbose_name = 'Слова'
        verbose_name_plural = 'Слова'
        ordering = ('-inverse_document_frequency',)
