import openai
import json
import os
from django.conf import settings
from django.db.models import Q
from decimal import Decimal
from .models import PSUProgram, College

openai.api_key = getattr(settings, 'OPENAI_API_KEY', '')

def get_all_psu_programs_summary():
    """Get summary of all active PSU programs for AI context"""
    programs = PSUProgram.objects.filter(is_active=True).select_related('college')
    summary = []
    
    for program in programs:
        summary.append({
            'name': str(program),
            'college': program.college.name,
            'skills': program.ideal_skills,
            'interests': program.ideal_interests,
            'duration': program.duration_years,
            'description': program.description[:200] + '...'
        })
    
    return summary

def calculate_program_match_score(user_data, program):
    """Calculate match % for PSU programs using PH HS GWA (70–100%) system"""
    
    # Initialize total score and weight
    score = 0.0
    total_weight = 0.0

    # -----------------------
    # 1️⃣ Skills matching (40%)
    # -----------------------
    user_skills = {
        'math': user_data['math_skill'],
        'science': user_data['science_skill'],
        'computer': user_data['computer_skill'],
        'analytical': user_data['analytical_skill'],
        'english': user_data['english_skill'],
        'creative': user_data['creative_skill']
    }

    program_skills = program.get_skill_list()
    matched_skill_scores = []

    for skill_name, user_score in user_skills.items():
        if any(skill_name.lower() in skill.lower() for skill in program_skills):
            matched_skill_scores.append(float(user_score))

    if matched_skill_scores:
        avg_skill = sum(matched_skill_scores) / len(matched_skill_scores)
        # Normalize 0–1 then multiply by weight
        weight_skill = 40
        score += (avg_skill / 5) * weight_skill
        total_weight += weight_skill

    # -----------------------
    # 2️⃣ Interests matching (40%)
    # -----------------------
    user_interests = {
        'technology': user_data['technology_interest'],
        'business': user_data['business_interest'],
        'healthcare': user_data['healthcare_interest'],
        'education': user_data['education_interest'],
        'arts': user_data['arts_interest'],
        'agriculture': user_data['agriculture_interest'],
        'hospitality': user_data['hospitality_interest'],
        'engineering': user_data.get('engineering_interest', 3)
    }

    program_interests = program.get_interest_list()
    matched_interest_scores = []

    for interest_name, user_score in user_interests.items():
        if any(interest_name.lower() in interest.lower() for interest in program_interests):
            matched_interest_scores.append(float(user_score))

    if matched_interest_scores:
        avg_interest = sum(matched_interest_scores) / len(matched_interest_scores)
        weight_interest = 40
        score += (avg_interest / 5) * weight_interest
        total_weight += weight_interest

    # -----------------------
    # 3️⃣ GWA bonus (20%)
    # -----------------------
    gwa_percent = float(user_data['high_school_gwa'])  # 70–100%
    gwa_score = ((gwa_percent - 70) / 30) * 20.0
    gwa_score = max(0.0, min(20.0, gwa_score))  # clamp 0–20
    score += gwa_score
    total_weight += 20

    # -----------------------
    # 4️⃣ Final percentage
    # -----------------------
    final_score = (score / total_weight) * 100 if total_weight > 0 else 0
    return round(final_score, 1)

def get_program_recommendations(user_data):
    """Generate AI-powered recommendations using database programs"""
    
    # Get all active programs
    programs = PSUProgram.objects.filter(is_active=True).select_related('college')
    
    # Calculate match scores for all programs
    program_scores = []
    for program in programs:
        match_score = calculate_program_match_score(user_data, program)
        program_scores.append({
            'program': program,
            'score': match_score
        })
    
    # Sort by score (descending)
    program_scores.sort(key=lambda x: x['score'], reverse=True)
    
    recommendations = []
    for i, item in enumerate(program_scores[:3], 1): # Only show top 3
        program = item['program']
        recommendations.append({
            "rank": i,
            "program": program.name,
            "college": program.college.name,
            "match_score": item['score'],
            "reasons": [f"Strong skills match ({item['score']}%)", "$$ AI $$"],
            "skills_match": f"Score: {item['score']}%",
            "duration": program.duration_years,
            "careers": program.career_paths[:100],
            "program_obj": program
        })
    return recommendations