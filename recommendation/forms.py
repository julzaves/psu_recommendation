from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML

# Star choices 1-5
STAR_CHOICES = [(i, str(i)) for i in range(1, 6)]

# Custom star widget
class StarRadioSelect(forms.RadioSelect):
    template_name = 'widgets/star_radio.html'
    option_template_name = 'widgets/star_option.html'

class RecommendationForm(forms.Form):
    # PERSONAL INFO
    full_name = forms.CharField(
        max_length=100,
        label="What's your full name? *",
        widget=forms.TextInput(attrs={'placeholder': 'e.g., Juan Dela Cruz'})
    )
    email = forms.EmailField(
        required=False,
        label="Your email (optional)",
        widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'})
    )
    high_school = forms.CharField(
        max_length=100,
        label="Senior High School *",
        widget=forms.TextInput(attrs={'placeholder': 'e.g., ACLC College of Puerto Princesa'})
    )
    high_school_gwa = forms.DecimalField(
        max_digits=3, decimal_places=0, min_value=70, max_value=100,
        label="Senior High School GWA *",
        widget=forms.NumberInput(attrs={'placeholder': 'e.g., 99'})
    )

    # SKILLS
    math_skill = forms.ChoiceField(choices=STAR_CHOICES, widget=StarRadioSelect, label="Math")
    science_skill = forms.ChoiceField(choices=STAR_CHOICES, widget=StarRadioSelect, label="Science")
    english_skill = forms.ChoiceField(choices=STAR_CHOICES, widget=StarRadioSelect, label="English")
    computer_skill = forms.ChoiceField(choices=STAR_CHOICES, widget=StarRadioSelect, label="Computer")
    analytical_skill = forms.ChoiceField(choices=STAR_CHOICES, widget=StarRadioSelect, label="Analytical")
    creative_skill = forms.ChoiceField(choices=STAR_CHOICES, widget=StarRadioSelect, label="Creativity")

    # INTERESTS
    technology_interest = forms.ChoiceField(choices=STAR_CHOICES, widget=StarRadioSelect, label="Technology")
    business_interest = forms.ChoiceField(choices=STAR_CHOICES, widget=StarRadioSelect, label="Business")
    healthcare_interest = forms.ChoiceField(choices=STAR_CHOICES, widget=StarRadioSelect, label="Healthcare")
    education_interest = forms.ChoiceField(choices=STAR_CHOICES, widget=StarRadioSelect, label="Education")
    arts_interest = forms.ChoiceField(choices=STAR_CHOICES, widget=StarRadioSelect, label="Arts")
    agriculture_interest = forms.ChoiceField(choices=STAR_CHOICES, widget=StarRadioSelect, label="Agriculture")
    hospitality_interest = forms.ChoiceField(choices=STAR_CHOICES, widget=StarRadioSelect, label="Hospitality")
    engineering_interest = forms.ChoiceField(choices=STAR_CHOICES, widget=StarRadioSelect, label="Engineering")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form'
        self.helper.label_class = 'form-label fw-bold'
        self.helper.field_class = 'form-control mb-3'

        self.helper.layout = Layout(
            HTML('<h4 class="mb-4 mt-0"><i class="fas fa-user-graduate text-primary"></i> Personal Info</h4>'),
            Row(
                Column('full_name', css_class='form-group col-md-4'),
                Column('email', css_class='form-group col-md-4'),
            ),
            Row(
                Column('high_school', css_class='form-group col-md-4'),
                Column('high_school_gwa', css_class='form-group col-md-4'),
            ),

            HTML('<h4 class="mb-3 mt-4"><i class="fas fa-brain text-success"></i> Academic Skills</h4>'),
            Row(
                Column('math_skill', css_class='col-md-2'),
                Column('science_skill', css_class='col-md-2'),
                Column('english_skill', css_class='col-md-2'),
                css_class='mb-3'
            ),
            Row(
                Column('computer_skill', css_class='col-md-2'),
                Column('analytical_skill', css_class='col-md-3'),
                Column('creative_skill', css_class='col-md-3'),
                css_class='mb-4'
            ),

            HTML('<h4 class="mb-3"><i class="fas fa-heart text-danger"></i> Interests</h4>'),
            Row(
                Column('technology_interest', css_class='col-md-2'),
                Column('business_interest', css_class='col-md-2'),
                Column('healthcare_interest', css_class='col-md-2'),
                Column('education_interest', css_class='col-md-2'),
                css_class='mb-3'
            ),
            Row(
                Column('arts_interest', css_class='col-md-2'),
                Column('agriculture_interest', css_class='col-md-2'),
                Column('hospitality_interest', css_class='col-md-2'),
                Column('engineering_interest', css_class='col-md-2'),
                css_class='mb-4'
            ),

            HTML('<hr class="my-4">'),
            Submit('submit', '🚀 Show My Recommendations',
                   css_class='btn btn-primary btn-lg w-100 fw-bold shadow-lg py-3',
                   style='background: linear-gradient(45deg, #2c5aa0, #f8b500); border: none; font-size: 1.2rem;')
        )