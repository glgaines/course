# -*- coding: utf-8 -*-
# models.py
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.html import strip_tags
from tinymce import models as tinymce_models

class Test(models.Model):
    name = models.CharField(u'Название', max_length=255)
    comments = tinymce_models.HTMLField(u'Описание', blank=True, default='')
    test_result = tinymce_models.HTMLField(u'Текст на странице результатов', blank=True, default='')

    def get_busy_name(self):
        return '%s_busy' % (self.id, )

    def get_comments(self):
        return self.comments

    get_comments.allow_tags = True
    get_comments.short_description = u'Описание'

    def get_max_score(self):
        max_score = 0
        for question in self.questions.all():
            if question.is_multiple:
                max_score += sum([answer.weight for answer in question.answers.all()])
            else:
                max_score += max([answer.weight for answer in question.answers.all()])
        return max_score

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = u'тест'
        verbose_name_plural = u'тесты'

class TestQuestion(models.Model):
    test = models.ForeignKey(Test, verbose_name=u'Тест', related_name='questions')
    title = models.CharField(u'Заголовок', max_length=255)
    comment = tinymce_models.HTMLField(u'Описание', blank=True, default='')
    position = models.IntegerField(u'Порядок', default=0)
    is_multiple = models.BooleanField(u'Поддержка множественного выбора', default=False)

    def get_comments(self):
        return self.comment
    get_comments.allow_tags = True
    get_comments.short_description = u'Описание'

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('position', )
        verbose_name = u'вопрос теста'
        verbose_name_plural = u'тесты-вопросы'

class TestAnswer(models.Model):
    question = models.ForeignKey(TestQuestion, verbose_name=u'Вопрос', related_name='answers')
    content = tinymce_models.HTMLField(u'Ответ')
    weight = models.IntegerField(u'Баллы')

    def __unicode__(self):
        return mark_safe(strip_tags(u'%s' % (self.content )))

    class Meta:
        ordering = ('weight', )
        verbose_name = u'ответ'
        verbose_name_plural = u'ответы'

class TestScale(models.Model):
    test = models.ForeignKey(Test, verbose_name=u'Тест', related_name='scales')
    start = models.IntegerField(u'Начало диапозона')
    end = models.IntegerField(u'Конец диапозона')
    comment = tinymce_models.HTMLField(u'Описание')

    def __unicode__(self):
        return u'Диапозон %s %s' % (self.start, self.end)

    class Meta:
        verbose_name = u'шкалу теста'
        verbose_name_plural = u'шкалы для тестов'


class TestResult(models.Model):
    test = models.ForeignKey(Test, verbose_name=u'Тест')
    result = tinymce_models.HTMLField(u'Результат')
    date = models.DateTimeField(u'Дата прохождения теста')
    email = models.EmailField(u'E-mail участника', blank=True, default='')
    fio = models.CharField(u'ФИО студента', max_length=255)
    group =models.CharField(u'Группа студента', max_length=255)
    def __unicode__(self):
        return u'Результат теста "%s"' % (self.test, )

    class Meta:
        verbose_name = u'результат теста'
        verbose_name_plural = u'тесты-результаты'