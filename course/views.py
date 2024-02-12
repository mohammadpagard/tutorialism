from django.shortcuts import render
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin

from urllib.parse import unquote

from .models import Course
from video.models import CourseVideo


class CourseListView(View):
    def get(self, request):
        courses = Course.objects.all()
        courses_length = len(courses)
        # paginator
        page = request.GET.get('page', 1)
        paginator = Paginator(courses, 8)
        try:
            course_list = paginator.page(page)
        except PageNotAnInteger:
            course_list = paginator.page(1)
        except EmptyPage:
            course_list = paginator.page(paginator.num_pages)

        context = {
            'courses': course_list,
            'courses_length': courses_length
        }
        return render(request, 'course/course_list.html', context)


class CourseDetailView(View):
    def get(self, request, course_id=None, course_slug=None):
        course_slug = unquote(course_slug)
        course = Course.objects.prefetch_related('videos').filter(id=course_id, slug=unquote(course_slug)).first()
        introducing_video = course.videos.first()
        videos = CourseVideo.objects.filter(courses=course)[1:]

        context = {
            'introducing_video': introducing_video,
            'course': course,
            'videos': videos
        }
        return render(request, 'course/course_detail.html', context)


class CourseVideoListView(View):
    def get(self, request, course_id=None, course_slug=None):
        videos = CourseVideo.objects.filter(
            Q(courses__id=course_id) &
            Q(courses__slug=course_slug)
        )
        context = {'videos': videos}
        return render(request, 'course/course_video_list.html', context)


class CourseVideoView(LoginRequiredMixin, View):
    def get(self, request, video_id=None, video_slug=None):
        video = CourseVideo.objects.prefetch_related('courses').filter(id=video_id, slug=video_slug).first()
        # video = get_object_or_404(CourseVideo, id=video_id, slug=video_slug)
        course_paid = video.courses.filter(sold_to=request.user).iterator()

        context = {
            'video': video,
            'course_paid': course_paid
        }
        return render(request, 'course/video_course.html', context)
