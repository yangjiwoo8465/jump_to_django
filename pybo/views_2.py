# from django.shortcuts import render, get_object_or_404, redirect
# from django.utils import timezone
# from .models import Question, Answer
# from django.contrib import messages
# # from django.http import HttpResponseNotAllowed
# from .forms import QuestionForm, AnswerForm
# from django.core.paginator import Paginator  
# from django.contrib.auth.decorators import login_required

# # def index(request):
# #     page = request.GET.get('page', '1')  # 페이지
# #     question_list = Question.objects.order_by('-create_date')
# #     paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
# #     page_obj = paginator.get_page(page)
# #     context = {'question_list': page_obj}
# #     return render(request, 'pybo/question_list.html', context)

# def index(request):
#     # page와 so(sort order) 파라미터 가져오기
#     page = request.GET.get('page', '1')   # 페이지
#     so = request.GET.get('so', 'desc')  # 정렬 기준 (추가)

#     # 정렬 기준에 따라 분기
#     if so == 'asc': # 오름차순 (오래된 순)
#         question_list = Question.objects.order_by('create_date')
#     else: # 내림차순 (최신순)
#         question_list = Question.objects.order_by('-create_date')

#     paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
#     page_obj = paginator.get_page(page)

#     # context에 so 추가
#     context = {'question_list': page_obj, 'so': so}
#     return render(request, 'pybo/question_list.html', context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'pybo/question_detail.html', context)

# # Generic View
# # class IndexView(generic.ListView):
# #     def get_queryset(self):
# #         return Question.objects.order_by('-create_date')


# # class DetailView(generic.DetailView):
# #     model = Question

# @login_required(login_url='common:login')
# def answer_create(request, question_id):
#     """
#     pybo 답변등록
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     if request.method == "POST":
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.author = request.user  # author 속성에 로그인 계정 저장
#             answer.create_date = timezone.now()
#             answer.question = question
#             answer.save()
#             return redirect('pybo:detail', question_id=question.id)
#     else:
#         form = AnswerForm()
#     context = {'question': question, 'form': form}
#     return render(request, 'pybo/question_detail.html', context)

# @login_required(login_url='common:login')
# def answer_modify(request, answer_id):
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.user != answer.author:
#         messages.error(request, '수정권한이 없습니다')
#         return redirect('pybo:detail', question_id=answer.question.id)
#     if request.method == "POST":
#         form = AnswerForm(request.POST, instance=answer)
#         if form.is_valid():
#             answer = form.save(commit=False)
#             answer.modify_date = timezone.now()
#             answer.save()
#             return redirect('pybo:detail', question_id=answer.question.id)
#     else:
#         form = AnswerForm(instance=answer)
#     context = {'answer': answer, 'form': form}
#     return render(request, 'pybo/answer_form.html', context)

# @login_required(login_url='common:login')
# def answer_delete(request, answer_id):
#     answer = get_object_or_404(Answer, pk=answer_id)
#     if request.user != answer.author:
#         messages.error(request, '삭제권한이 없습니다')
#     else:
#         answer.delete()
#     return redirect('pybo:detail', question_id=answer.question.id)

# @login_required(login_url='common:login')
# def question_create(request):
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.author = request.user  # author 속성에 로그인 계정 저장
#             question.create_date = timezone.now()
#             question.save()
#             return redirect('pybo:index')
#     else:
#         form = QuestionForm()
#     context = {'form': form}
#     return render(request, 'pybo/question_form.html', context)

# @login_required(login_url='common:login')
# def question_modify(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     if request.user != question.author:
#         messages.error(request, '수정권한이 없습니다')
#         return redirect('pybo:detail', question_id=question.id)
#     if request.method == "POST":
#         form = QuestionForm(request.POST, instance=question)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.modify_date = timezone.now()  # 수정일시 저장
#             question.save()
#             return redirect('pybo:detail', question_id=question.id)
#     else:
#         form = QuestionForm(instance=question)
#     context = {'form': form}
#     return render(request, 'pybo/question_form.html', context)

# @login_required(login_url='common:login')
# def question_delete(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     if request.user != question.author:
#         messages.error(request, '삭제권한이 없습니다')
#         return redirect('pybo:detail', question_id=question.id)
#     question.delete()
#     return redirect('pybo:index')