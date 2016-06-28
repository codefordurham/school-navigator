from django.forms import ModelForm, TextInput, URLInput, Textarea
import schools.models as schools_models

class SchoolProfileForm(ModelForm):
    class Meta:
        model = schools_models.SchoolProfile
        exclude = ('school', 'created_at', 'submitted_at', )
        widgets = {
            'school_hours': TextInput,
            'phone_number': TextInput,
            'website_url': URLInput,
            'theme': TextInput,
            'mission_statement': Textarea(attrs={'rows': 8}),
            'transportation_explanation': TextInput,
            'before_care_hours': TextInput,
            'after_care_hours': TextInput,
            'points_of_pride1': Textarea(attrs={'rows': 4}),
            'points_of_pride2': Textarea(attrs={'rows': 4}),
            'points_of_pride3': Textarea(attrs={'rows': 4}),
            'extended_care_cost': TextInput,
            'extended_care_financial_assistance': Textarea(attrs={'rows': 4}),
            'breakfast_explanation': Textarea(attrs={'rows': 4}),
            'lunch_explanation': Textarea(attrs={'rows': 4}),
            'principal_name': TextInput,
            'principal_bio': Textarea(attrs={'rows': 8}),
            'admissions_policy_type': Textarea(attrs={'rows': 2}),
            'learn_more_link': URLInput,
            'english_language_learner': Textarea(attrs={'rows': 4}),
            'special_education': Textarea(attrs={'rows': 4}),
            'gifted_education': Textarea(attrs={'rows': 4}),
            'other_academic': Textarea(attrs={'rows': 4}),
            'academic': Textarea(attrs={'rows': 4}),
            'arts': Textarea(attrs={'rows': 4}),
            'sports': Textarea(attrs={'rows': 4}),
            'service_leadership': Textarea(attrs={'rows': 4}),
            'other': Textarea(attrs={'rows': 4}),
            'pta_website': URLInput,
            'parental_involvement_notes': Textarea(attrs={'rows': 4}),
            'feeder_school_info': Textarea(attrs={'rows': 4}),


        }

    _fieldsets = (
        ('Basic Facts', [
            'level', 'grade_min', 'grade_max', 'school_hours', 'phone_number',
            'website_url', 'year_opened', 'mission_statement',
            'theme', 'uniform_required',
        ]),
        ('Points of Pride', [
            'points_of_pride1', 'points_of_pride2', 'points_of_pride3',
        ]),
        ('School Services', [
            'transportation', 'transportation_explanation',
            'before_care_offered', 'before_care_hours',
            'after_care_offered', 'after_care_hours', 'extended_care_cost',
            'extended_care_financial_assistance',
            'breakfast_served', 'breakfast_free_and_reduced',
            'breakfast_explanation', 
            'lunch_served', 'lunch_free_and_reduced',
            'lunch_explanation',
        ]),
        ('School Leadership', [
            'principal_name', 'principal_start_year', 'principal_bio',
        ]),
        ('Admissions Policy', [
            'admissions_policy_type',
            'lottery_priority_1', 'lottery_priority_2', 'lottery_priority_3',
            'lottery_priority_4', 'lottery_priority_5',
            'lottery_deadline', 'learn_more_link', 'feeder_school_info',
        ]),
        ('Targeted Academic Offerings', [
            'other_academic',
            'english_language_learner',
            'special_education',
            'gifted_education',
        ]),
        ('Extracurricular Offerings', [
            'academic', 'arts', 'sports', 'service_leadership', 'other',
        ]),
        ('Parent Involvement', [
            'pta', 'pta_website', 'parental_involvement_notes',
        ]),
        ('Your Feedback', [
            'survey_feedback',
        ]),

    )

    @property
    def fieldsets(self):
        for description, fields in self._fieldsets:
            yield description, [self[field] for field in fields]

    # basic_facts

    # school_services

    # school_leadership

    # admissions_policy

    # targeted_admissions_policy

    # extracurricular_offerings

    # parent_involvement

    # feedback
