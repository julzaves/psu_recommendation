from django.db import models
import uuid

class College(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    dean = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='colleges/', blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=100)
    
    def __str__(self):
        return self.name

    def get_num_of_programs(self):
        return len(self.programs.filter(is_active=True))

class PSUProgram(models.Model):
    DEGREE_LEVELS = [
        ('B', "Bachelor of"),
        ('BS', 'Bachelor of Science'),
        ('BA', 'Bachelor of Arts'),
        ('BSED', 'Bachelor of Secondary Education'),
        ('BEED', 'Bachelor of Elementary Education'),
    ]
    
    DURATION_CHOICES = [
        (4, '4 Years'),
        (5, '5 Years'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    degree_level = models.CharField(max_length=10, choices=DEGREE_LEVELS)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='programs')
    description = models.TextField()
    duration_years = models.IntegerField(choices=DURATION_CHOICES)
    tuition_estimate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    required_hs_subjects = models.TextField(blank=True)
    career_paths = models.TextField()
    ideal_skills = models.TextField()  # Comma-separated: "math,programming,communication"
    ideal_interests = models.TextField()  # Comma-separated: "technology,business,innovation"
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['name']
        unique_together = ['name', 'college']
    
    def __str__(self):
        return f"{self.get_degree_level_display()} {self.name} ({self.college.abbreviation})"
    
    def get_skill_list(self):
        return [skill.strip() for skill in self.ideal_skills.split(',') if skill.strip()]
    
    def get_interest_list(self):
        return [interest.strip() for interest in self.ideal_interests.split(',') if interest.strip()]