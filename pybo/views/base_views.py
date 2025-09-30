from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from ..models import Question


# def index(request):
#     page = request.GET.get('page', '1')  # 페이지
#     question_list = Question.objects.order_by('-create_date')
#     paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
#     page_obj = paginator.get_page(page)
#     context = {'question_list': page_obj}
#     return render(request, 'pybo/question_list.html', context)

def index(request):
    3/0  # 강제로 오류발생
    # page와 so(sort order) 파라미터 가져오기
    page = request.GET.get('page', '1')   # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'desc')  # 정렬 기준 (추가)

    # 정렬 기준에 따라 분기
    if so == 'asc': # 오름차순 (오래된 순)
        question_list = Question.objects.order_by('create_date')
    else: # 내림차순 (최신순)
        question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()

    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    # context에 so 추가
    context = {'question_list': page_obj, 'so': so, 'page': page, 'kw': kw}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

# Generic View
# class IndexView(generic.ListView):
#     def get_queryset(self):
#         return Question.objects.order_by('-create_date')


# class DetailView(generic.DetailView):
#     model = Question
