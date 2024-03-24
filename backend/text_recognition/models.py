from django.db import models


class Document(models.Model):
    document_name = models.CharField(
        'Назнавние документа', max_length=150)
    total_words = models.IntegerField('Количество слов в документе', default=0)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Text(models.Model):
    word = models.CharField('Слово', max_length=150)
    word_quantity = models.IntegerField(
        'Количество раз слово встречается в тексте', default=0)
    doc_name = models.ForeignKey(
        Document, verbose_name='Название документа',
        related_name='texts', on_delete=models.CASCADE)
    term_frequency = models.DecimalField(
        'Частота слова или TF', default=0,
        max_digits=5, decimal_places=4)
    inverse_document_frequency = models.DecimalField(
        'Oбратная частота документа или IDF', default=0,
        max_digits=5, decimal_places=4)

    class Meta:
        verbose_name = 'Слова'
        verbose_name_plural = 'Слова'
        ordering = ('-inverse_document_frequency',)


class DocumentText(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    text = models.ForeignKey(Text, on_delete=models.CASCADE)
    term_frequency = models.IntegerField('Частота слова или TF', default=0)
    inverse_document_frequency = models.IntegerField(
        'Oбратная частота документа или IDF', default=0)

    class Meta:
        verbose_name = 'Документ и текст'
        verbose_name_plural = 'Документы и тексты'
