from django.core.management.base import BaseCommand
from recommendation.models import College, PSUProgram
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seed PSU Colleges and ALL Official Programs database'
    
    def handle(self, *args, **options):
        # Clear existing data
        PSUProgram.objects.all().delete()
        College.objects.all().delete()
        
        # 1. Create Colleges (Updated with correct names)
        colleges_data = [
            {'name': 'College of Arts and Humanities', 'abbr': 'CAH', 'dean': 'Dr. Elena Rivera'},
            {'name': 'College of Business and Accountancy', 'abbr': 'CBA', 'dean': 'Prof. Jose Reyes'},
            {'name': 'College of Criminal Justice Education', 'abbr': 'CCJE', 'dean': 'Prof. Miguel Santos'},
            {'name': 'College of Architecture and Design', 'abbr': 'CAD', 'dean': 'Ar. Sofia Garcia'},
            {'name': 'College of Engineering', 'abbr': 'COE', 'dean': 'Engr. Ana Lim'},
            {'name': 'College of Hospitality and Tourism Management', 'abbr': 'CHTM', 'dean': 'Prof. Carla Vega'},
            {'name': 'College of Nursing and Health Sciences', 'abbr': 'CNHS', 'dean': 'Dr. Liza Cruz'},
            {'name': 'College of Sciences', 'abbr': 'CS', 'dean': 'Dr. Marco Polo'},
            {'name': 'College of Teacher Education', 'abbr': 'CTE', 'dean': 'Prof. Pedro Gomez'},
        ]
        
        colleges = []
        for data in colleges_data:
            college = College.objects.create(
                name=data['name'],
                abbreviation=data['abbr'],
                dean=data['dean'],
                description=f"Palawan State University {data['name']} - Excellence in {data['abbr']} education and research.",
                slug=slugify(data['name'])
            )
            colleges.append(college)
            self.stdout.write(self.style.SUCCESS(f'✅ Created {college.abbreviation}: {college.name}'))
        
        # 2. Create ALL Official PSU Programs
        programs_data = [
            # College of Arts and Humanities (0)
            {
                'name': 'Communication', 'college': colleges[0], 'skills': 'communication,creative,english',
                'interests': 'arts,media,communication', 'duration': 4, 'degree': 'BA',
                'careers': 'Journalist, Media Producer, PR Specialist, Content Creator',
                'desc': 'Master mass communication, journalism, broadcasting, and digital media.'
            },
            {
                'name': 'Political Science', 'college': colleges[0], 'skills': 'analytical,communication',
                'interests': 'politics,government,social', 'duration': 4, 'degree': 'BA',
                'careers': 'Political Analyst, Government Official, Policy Advisor, Diplomat',
                'desc': 'Study political systems, governance, international relations, and public policy.'
            },
            {
                'name': 'Philippine Studies', 'college': colleges[0], 'skills': 'research,communication',
                'interests': 'culture,history,arts', 'duration': 4, 'degree': 'BA',
                'careers': 'Cultural Researcher, Museum Curator, Heritage Officer, Writer',
                'desc': 'Explore Philippine history, culture, literature, and social traditions.'
            },
            {
                'name': 'Social Work', 'college': colleges[0], 'skills': 'communication,analytical',
                'interests': 'social,helping,community', 'duration': 4, 'degree': 'BS',
                'careers': 'Social Worker, Community Organizer, Counselor, NGO Manager',
                'desc': 'Learn social welfare, community development, and counseling skills.'
            },
            {
                'name': 'Psychology', 'college': colleges[0], 'skills': 'analytical,science,communication',
                'interests': 'healthcare,psychology,social', 'duration': 4, 'degree': 'BS',
                'careers': 'Psychologist, HR Specialist, Counselor, Researcher',
                'desc': 'Study human behavior, mental health, and psychological research.'
            },
            
            # College of Business and Accountancy (1)
            {
                'name': 'Accountancy', 'college': colleges[1], 'skills': 'math,analytical',
                'interests': 'business,finance', 'duration': 5, 'degree': 'BS',
                'careers': 'CPA, Auditor, Financial Controller, Tax Consultant',
                'desc': 'Comprehensive accounting, auditing, taxation, and financial reporting.'
            },
            {
                'name': 'Management Accounting', 'college': colleges[1], 'skills': 'math,analytical,business',
                'interests': 'business,finance', 'duration': 4, 'degree': 'BS',
                'careers': 'Cost Accountant, Budget Analyst, Management Consultant',
                'desc': 'Focus on cost management, budgeting, and business decision-making.'
            },
            {
                'name': 'Business Administration - Human Resource Management', 'college': colleges[1], 'skills': 'communication,business',
                'interests': 'business,management', 'duration': 4, 'degree': 'BS',
                'careers': 'HR Manager, Recruiter, Training Specialist, Labor Relations',
                'desc': 'Specialize in human resources, talent management, and organizational behavior.'
            },
            {
                'name': 'Business Administration - Financial Management', 'college': colleges[1], 'skills': 'math,business',
                'interests': 'business,finance', 'duration': 4, 'degree': 'BS',
                'careers': 'Financial Manager, Investment Analyst, Corporate Treasurer',
                'desc': 'Master corporate finance, investments, and risk management.'
            },
            {
                'name': 'Business Administration - Marketing Management', 'college': colleges[1], 'skills': 'communication,creative,business',
                'interests': 'business,marketing', 'duration': 4, 'degree': 'BS',
                'careers': 'Marketing Manager, Brand Manager, Digital Marketer, Sales Director',
                'desc': 'Learn marketing strategy, consumer behavior, and digital marketing.'
            },
            {
                'name': 'Entrepreneurship - Innovation and Technology', 'college': colleges[1], 'skills': 'creative,business,computer',
                'interests': 'business,technology,entrepreneurship', 'duration': 4, 'degree': 'BS',
                'careers': 'Startup Founder, Tech Entrepreneur, Innovation Manager',
                'desc': 'Build startups with focus on technology and innovation.'
            },
            {
                'name': 'Public Administration', 'college': colleges[1], 'skills': 'communication,analytical',
                'interests': 'government,public service', 'duration': 4, 'degree': 'BS',
                'careers': 'Government Administrator, Policy Analyst, Public Manager',
                'desc': 'Prepare for leadership roles in government and public sector.'
            },
            
            # College of Criminal Justice Education (2)
            {
                'name': 'Criminology', 'college': colleges[2], 'skills': 'analytical,communication',
                'interests': 'law,justice,social', 'duration': 4, 'degree': 'BS',
                'careers': 'Criminologist, Police Officer, Forensic Investigator, Lawyer',
                'desc': 'Study crime prevention, criminal justice system, and law enforcement.'
            },
            
            # College of Architecture and Design (3)
            {
                'name': 'Architecture', 'college': colleges[3], 'skills': 'creative,analytical,math',
                'interests': 'design,arts,engineering', 'duration': 5, 'degree': 'BS',
                'careers': 'Architect, Urban Planner, Interior Designer',
                'desc': 'Design buildings, spaces, and sustainable urban environments.'
            },
            
            # College of Engineering (4)
            {
                'name': 'Civil Engineering', 'college': colleges[4], 'skills': 'math,science,analytical',
                'interests': 'engineering,infrastructure', 'duration': 5, 'degree': 'BS',
                'careers': 'Civil Engineer, Structural Engineer, Project Manager',
                'desc': 'Design infrastructure: bridges, roads, buildings, water systems.'
            },
            {
                'name': 'Electrical Engineering', 'college': colleges[4], 'skills': 'math,science,computer',
                'interests': 'engineering,technology', 'duration': 5, 'degree': 'BS',
                'careers': 'Electrical Engineer, Power Systems Engineer, Electronics Designer',
                'desc': 'Power systems, electronics, renewable energy, automation.'
            },
            {
                'name': 'Mechanical Engineering', 'college': colleges[4], 'skills': 'math,science,analytical',
                'interests': 'engineering,technology', 'duration': 5, 'degree': 'BS',
                'careers': 'Mechanical Engineer, Automotive Engineer, Manufacturing Engineer',
                'desc': 'Design machines, vehicles, HVAC systems, and manufacturing processes.'
            },
            {
                'name': 'Petroleum Engineering', 'college': colleges[4], 'skills': 'math,science',
                'interests': 'engineering,energy', 'duration': 5, 'degree': 'BS',
                'careers': 'Petroleum Engineer, Drilling Engineer, Reservoir Engineer',
                'desc': 'Oil & gas exploration, drilling, production, and energy systems.'
            },
            
            # College of Hospitality and Tourism Management (5)
            {
                'name': 'Hospitality Management - Culinary Arts', 'college': colleges[5], 'skills': 'creative,communication',
                'interests': 'hospitality,culinary', 'duration': 4, 'degree': 'BS',
                'careers': 'Chef, Restaurant Manager, Food & Beverage Director',
                'desc': 'Master culinary arts, kitchen management, and food production.'
            },
            {
                'name': 'Tourism Management', 'college': colleges[5], 'skills': 'communication,business',
                'interests': 'tourism,hospitality', 'duration': 4, 'degree': 'BS',
                'careers': 'Tour Operator, Travel Consultant, Destination Manager',
                'desc': 'Develop tourism products, manage travel operations, promote destinations.'
            },
            
            # College of Nursing and Health Sciences (6)
            {
                'name': 'Nursing', 'college': colleges[6], 'skills': 'science,communication',
                'interests': 'healthcare,helping', 'duration': 4, 'degree': 'BS',
                'careers': 'Registered Nurse, Nurse Practitioner, Clinical Nurse',
                'desc': 'Patient care, medical procedures, community health nursing.'
            },
            {
                'name': 'Midwifery', 'college': colleges[6], 'skills': 'science,communication',
                'interests': 'healthcare,maternal', 'duration': 4, 'degree': 'BS',
                'careers': 'Midwife, Maternal Health Specialist, Birth Attendant',
                'desc': 'Maternal and child health, prenatal care, delivery assistance.'
            },
            
            # College of Sciences (7)
            {
                'name': 'Biology - Medical Biology', 'college': colleges[7], 'skills': 'science,analytical',
                'interests': 'science,healthcare', 'duration': 4, 'degree': 'BS',
                'careers': 'Medical Researcher, Lab Technician, Biotech Specialist',
                'desc': 'Focus on human biology, medical research, and biotechnology.'
            },
            {
                'name': 'Marine Biology', 'college': colleges[7], 'skills': 'science',
                'interests': 'science,environment,marine', 'duration': 4, 'degree': 'BS',
                'careers': 'Marine Biologist, Conservationist, Aquaculture Specialist',
                'desc': 'Study marine ecosystems, coral reefs, fisheries, and ocean conservation.'
            },
            {
                'name': 'Computer Science', 'college': colleges[7], 'skills': 'math,programming,computer,analytical',
                'interests': 'technology,innovation', 'duration': 4, 'degree': 'BS',
                'careers': 'Software Engineer, Data Scientist, AI Developer, Systems Architect',
                'desc': 'Algorithms, AI, software engineering, cybersecurity, data science.'
            },
            {
                'name': 'Environmental Science', 'college': colleges[7], 'skills': 'science,analytical',
                'interests': 'environment,sustainability', 'duration': 4, 'degree': 'BS',
                'careers': 'Environmental Consultant, Conservation Officer, Sustainability Manager',
                'desc': 'Environmental protection, climate change, natural resource management.'
            },
            {
                'name': 'Information Technology', 'college': colleges[7], 'skills': 'computer,analytical',
                'interests': 'technology,business', 'duration': 4, 'degree': 'BS',
                'careers': 'IT Specialist, Network Engineer, Web Developer, Cybersecurity Analyst',
                'desc': 'Networking, web development, database systems, IT infrastructure.'
            },
            
            # College of Teacher Education (8)
            {
                'name': 'Elementary Education', 'college': colleges[8], 'skills': 'communication,creative',
                'interests': 'education,children', 'duration': 4, 'degree': 'BEED',
                'careers': 'Elementary Teacher, School Principal, Education Specialist',
                'desc': 'Teach children ages 6-12 across all basic subjects.'
            },
            {
                'name': 'Secondary Education - Mathematics', 'college': colleges[8], 'skills': 'math,communication',
                'interests': 'education,math', 'duration': 4, 'degree': 'BSED',
                'careers': 'High School Math Teacher, Math Coordinator, Tutor',
                'desc': 'Teach mathematics to secondary students with pedagogy expertise.'
            },
            {
                'name': 'Secondary Education - Science', 'college': colleges[8], 'skills': 'science,communication',
                'interests': 'education,science', 'duration': 4, 'degree': 'BSED',
                'careers': 'Science Teacher, Lab Instructor, STEM Coordinator',
                'desc': 'Teach biology, chemistry, physics to high school students.'
            },
            {
                'name': 'Physical Education', 'college': colleges[8], 'skills': 'communication,creative',
                'interests': 'education,sports', 'duration': 4, 'degree': 'BPE',
                'careers': 'PE Teacher, Sports Coach, Fitness Instructor, Athletic Director',
                'desc': 'Sports coaching, physical fitness, health education, recreation.'
            },
        ]
        
        created_count = 0
        for data in programs_data:
            program = PSUProgram.objects.create(
                name=data['name'],
                college=data['college'],
                degree_level=data['degree'],
                ideal_skills=data['skills'],
                ideal_interests=data['interests'],
                duration_years=data['duration'],
                description=data['desc'],
                career_paths=data['careers'],
                tuition_estimate=28000.00  # Updated average PSU tuition
            )
            created_count += 1
            self.stdout.write(self.style.SUCCESS(f'✅ [{program.college.abbreviation}] {program.name}'))
        
        # Summary
        total_programs = PSUProgram.objects.count()
        total_colleges = College.objects.count()
        self.stdout.write(
            self.style.SUCCESS(
                f'\n🎉 COMPLETE! Seeded {total_colleges} colleges & {total_programs} OFFICIAL PSU programs!\n'
                f'📊 Ready for AI recommendations! Run: python manage.py runserver'
            )
        )