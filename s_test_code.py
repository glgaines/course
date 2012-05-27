# -*- coding: utf-8 -*-
import datetime


from django.shortcuts import get_object_or_404
from django.core.mail import  EmailMessage
from django.template import RequestContext
from django.template.loader import get_template, render_to_string
from django.conf import settings

from website.models import Settings
from s_test.models import (Test as ModelTest, TestAnswer, TestResult, )
from s_test.forms import (TestAnswerRadioForm, TestAnswerCheckBoxForm, TestEmailForm, )

def get_test_info(request):
    result = {'is_new' : False}
    test_detail = ModelTest.objects.all()[0]
    question_list = test_detail.questions.all().order_by('position')
    local_context = {'test_detail' : test_detail,
                     'question_list' : [i+1 for i, item in enumerate(question_list)]}
    
    try:
        q = int(request.GET.get('q', ''))
        request.session[test_detail.get_busy_name()]
    except (ValueError, KeyError):
        q = 1
        result['is_new'] = True
        request.session[test_detail.get_busy_name()] = {'prev_question' : 1,
                                                        'prev_post' : {},
                                                        'available_questions' : [1, ],
                                                        'passed_questions' : [0, ],
                                                        'score' : {},
                                                        'forms' : {},
                                                        'test_result' : '', }
    
    parameters = request.session[test_detail.get_busy_name()]
    available_questions = parameters['available_questions']
    passed_questions = parameters['passed_questions']
    
    if q not in available_questions or q-1 not in passed_questions:
        q = 1
    
    if len(available_questions)-1 == question_list.count():
        return get_test_result(test_detail, result, parameters, local_context, request, question_list, available_questions, q)
    if request.method == 'POST':
        parameters['prev_post'] = request.POST
        prev_question = parameters['prev_question']
        answer_list = request.POST.getlist('answer')
        if question_list[prev_question-1].is_multiple:
            answer_form = TestAnswerCheckBoxForm(queryset=question_list[prev_question-1].answers.all(), data=request.POST)
        else:
            answer_form = TestAnswerRadioForm(queryset=question_list[prev_question-1].answers.all(), data=request.POST)
        if answer_form.is_valid():
            forms = parameters['forms']
            forms[prev_question] = answer_form
            score = parameters['score']
            score[prev_question] = 0
            for answer in answer_list:
                score[prev_question] += TestAnswer.objects.get(id=answer).weight
            if prev_question+1 not in available_questions:
                available_questions.append(prev_question+1)
            if prev_question not in passed_questions:
                passed_questions.append(prev_question)
            available_questions.sort()
            if len(available_questions)-1 == question_list.count():
                return get_test_result(test_detail, result, parameters, local_context, request, question_list, available_questions, q)
            
            if q in parameters['forms'].keys():
                answer_form = parameters['forms'][q]
            else:
                if question_list[q-1].is_multiple:
                    answer_form = TestAnswerCheckBoxForm(queryset=question_list[q-1].answers.all())
                else:
                    answer_form = TestAnswerRadioForm(queryset=question_list[q-1].answers.all())
            parameters['prev_question'] = q
            current_question = q
            next_question = q+1
        else:
            current_question = prev_question
            next_question = q
    else:
        if q in parameters['forms'].keys():
            answer_form = parameters['forms'][q]
        else:
            if question_list[q-1].is_multiple:
                answer_form = TestAnswerCheckBoxForm(queryset=question_list[q-1].answers.all())
            else:
                answer_form = TestAnswerRadioForm(queryset=question_list[q-1].answers.all())
        current_question = q
        parameters['prev_question'] = q
        next_question = q+1
    try:
        progress = int((float(len(available_questions)-1))/float(question_list.count())*100)
    except ZeroDivisionError:
        progress = 0
    request.session[test_detail.get_busy_name()] = parameters
    local_context.update({'question_detail' : question_list[current_question-1],
                          'answer_form' : answer_form,
                          'next_question' : next_question,
                          'current_question' : current_question,
                          'available_questions' : available_questions,
                          'progress' : progress, })
    
    template = get_template('test_question.html').render(RequestContext(request, local_context))
    
    redirect = True if request.method == 'POST' else False
    result.update({'template' : template, 'redirect' : redirect, 'next' : q+1})
    return result

def get_test_result(test_detail, result, parameters, local_context, request, question_list, available_questions, q):
    score = parameters['score']
    score = sum([value for value in score.values()])
    try:
        comment = test_detail.scales.filter(start__lte=score, end__gte=score)[0].comment
    except IndexError:
        comment = ''
    if not parameters['test_result']:
        test_result = TestResult(test=test_detail, result=comment, date=datetime.datetime.now())
        test_result.save()
        request.session['test_result_id']= test_result.id
        parameters['test_result'] = True
        request.session[test_detail.get_busy_name()] = parameters
    profile = request.user.get_profile()
    form = TestEmailForm(initial={
        'fio': '%s %s' % (request.user.first_name, request.user.last_name),
        'group': '%s' % (profile.study_group),
    })
    if request.method == 'POST':
        parameters['prev_post'] = request.POST
        request.session[test_detail.get_busy_name()] = parameters
    else:
        if 'fio' in parameters['prev_post']:
            form = TestEmailForm(data=parameters['prev_post'])
        if form.is_valid():
            test_result = get_object_or_404(TestResult, id=request.session['test_result_id'])
            test_result.email = request.user.email
            test_result.fio = form.data['fio']
            test_result.group = form.data['group']
            test_result.save()
            message = render_to_string('messages/test_result.txt', {'test_name' : test_detail.name,
                            'test_result' : comment })

            msg = EmailMessage(u'Результаты теста %s' % (test_detail.name, ),
                      message,
                settings.DEFAULT_FROM_EMAIL,
                      (request.user.email, ))
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()
            message1 = render_to_string('messages/test_result_admin.txt', {'test_name' : test_detail.name,
                                                                    'test_result' : comment })
            msg = EmailMessage(u'Результаты теста %s. Группа: %s Студент: %s' % (test_detail.name, test_result.group, test_result.fio),
                message1,
                settings.DEFAULT_FROM_EMAIL,
                (Settings.objects.all()[0].email.split(',')[0], ))
            msg.content_subtype = "html"  # Main content is now text/html
            msg.send()
            local_context.update({ 'send' : True })
            
        else:
            local_context.update({ 'send' : False })
    try:
        progress = int((float(len(available_questions)-1))/float(question_list.count())*100)
    except ZeroDivisionError:
        progress = 0
    local_context.update({'score' : score, 'result' : comment,
                          'max_score' : test_detail.get_max_score(),
                          'available_questions' : available_questions,
                          'progress' : progress,
                          'form' : form, })
    template = get_template('test_end.html').render(RequestContext(request, local_context))
    redirect = True if request.method == 'POST' else False
    result.update({'template' : template, 'redirect' : redirect, 'next' : q})
    return result

