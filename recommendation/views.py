from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json
from .forms import RecommendationForm
from .services import get_program_recommendations
from .models import College, PSUProgram

def home(request):
    """Home page showing colleges and stats"""
    colleges = College.objects.all()
    total_colleges = College.objects.all().count()
    total_programs = PSUProgram.objects.filter(is_active=True).count()
    context = {
        'colleges': colleges,
        'total_colleges': total_colleges,
        'total_programs': total_programs
    }
    return render(request, 'recommendation/home.html', context)

def recommend_form(request):
    """Recommendation form and results"""
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            recommendations = get_program_recommendations(user_data)
            
            context = {
                'form': form,
                'recommendations': recommendations,
                'show_results': True,
                'user_data': user_data,
                'all_colleges': College.objects.all(),
                'gwa_display': f"{user_data['high_school_gwa']:.0f}%"
            }
            return render(request, 'recommendation/recommend.html', context)
    else:
        form = RecommendationForm()
    
    context = {
        'form': form,
        'show_results': False
    }
    return render(request, 'recommendation/recommend.html', context)

def college_programs(request, college_slug):
    """Show all programs in a college"""
    college = get_object_or_404(College, slug=college_slug)
    programs = college.programs.filter(is_active=True)
    context = {
        'college': college,
        'programs': programs
    }
    return render(request, 'recommendation/college_programs.html', context)

def program_detail(request, program_id):
    """Detailed view of a single program"""
    program = get_object_or_404(PSUProgram, id=program_id)
    context = {
        'program': program
    }
    return render(request, 'recommendation/program_detail.html', context)