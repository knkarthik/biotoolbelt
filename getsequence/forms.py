from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import FormActions, InlineCheckboxes

chromosomes = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7',
               'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14',
               'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21',
               'chr22', 'chrX', 'chrY']


class ChrForm(forms.Form):
    chr = forms.ChoiceField(choices=[(chr, chr) for chr in chromosomes], label="Chromosome")
    start = forms.IntegerField(min_value=1)
    end = forms.IntegerField(min_value=1)

    def __init__(self, *args, **kwargs):
        super(ChrForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-3'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
                'chr',
                'start',
                'end',
                FormActions(
                        Submit('submit', 'Submit', css_class='btn-primary')))
