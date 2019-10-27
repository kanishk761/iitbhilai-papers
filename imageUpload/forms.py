from django import forms
from .models import paperModel
from .models import courseModel

class addPaper(forms.ModelForm):
    def clean_course_code(self):
        code = self.cleaned_data['course_code']
        q = courseModel.objects.filter(course_code = code)
        if len(q) == 0:
            raise forms.ValidationError("no such course")
        return code
    def clean_tierce(self):
        tierce = self.cleaned_data['tierce']

        if tierce > 3 or tierce <1:
            raise forms.ValidationError("no tierce")
        return tierce
    def clean_year(self):
        year = self.cleaned_data['year']

        if year < 2016:
            raise forms.ValidationError("no such year")
        return year
    def clean_paper(self):
        paper = self.cleaned_data['paper']

        x = paper.name
        type = x[len(x)-4:len(x)]
        if type != '.pdf':
            raise forms.ValidationError("only pdf files allowed")
        return paper
    class Meta:
        model = paperModel
        fields = '__all__'
