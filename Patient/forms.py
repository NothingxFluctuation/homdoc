from django import forms
from .models import Chest_Pain

ch = [('days','Days'),('months','Months'),('years','Years')]
ch2 = [('seconds','Seconds'), ('minutes','Minutes'),('hours','Hours'),('days','Days'),('months','Months'),('years','Years')]
d = [('<1','<1'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),
('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('>20','>20')]
q = (
        ('Abrupt Onset','Abrupt Onset'),
        ('Aching/Dull','Aching/Dull'),
        ('Burning','Burning'),
        ('Continuous','Continuous'),
        ('Gradual','Gradual'),
        ('Intermittent','Intermittent'),
        ('Pressure','Pressure'),
        ('Ripping or Tearing','Ripping or Tearing'),
        ('Sharp','Sharp'),
        ('Tightness','Tightness'),
    )

assc_symptoms = (
    ('Chills','Chills'),
    ('Cough','Cough'),
    ('Diaphoresis','Diaphoresis'),
    ('Difficulty Swallowing','Difficulty Swallowing'),
    ('Fever','Fever'),
    ('Focal Neurologic Sign','Focal Neurologic Sign'),
    ('Hematochezia','Hematochezia'),
    ('Immobilization (>= 3 days) or surgery in the previous four weeks','Immobilization (>= 3 days) or surgery in the previous four weeks'),
    ('Leg Swelling','Leg Swelling'),
    ('Nausea','Nausea'),
    ('Numbness','Numbness'),
    ('Presence of Hemoptysis','Presence of Hemoptysis'),
    ('Rash','Rash'),
    ('Trauma Exertion','Recent Trauma or Physical Exertion'),
    ('Severe angina (≥2 episodes in 24 hrs)','Severe angina (≥2 episodes in 24 hrs)'),
    ('Shortness of Breath','Shortness of Breath'),
    ('Syncope','Syncope'),
    ('Tingling','Tingling'),
    ('Vomiting','Vomiting'),
    ('Vomiting Blood','Vomiting Blood'),
    ('Weakness','Weakness'),
)

s_to_p = (
    ('Aortic Dissection','Aortic Dissection'),
    ('Cancer','Cancer'),
    ('Cardiac Tamponade','Cardiac Tamponade'),
    ('Chest wall contusion/strain','Chest wall contusion/strain'),
    ('Gastroesophageal Reflux','Gastroesophageal Reflux'),
    ('GI Bleed','GI Bleed'),
    ('Herpes Zoster','Herpes Zoster'),
    ('Medication Related','Medication Related'),
    ('Muscle Strain','Muscle Strain'),
    ('Myocardial Infaction','Myocardial Infaction'),
    ('Myocarditis','Myocarditis'),
    ('Pericarditis','Pericarditis'),
    ('Pneumonia','Pneumonia'),
    ('Pneumothorax','Pneumothorax'),
    ('Pulmonary Embolism','Pulmonary Embolism'),
    ('Toxin Related','Toxin Related'),

)

past_mhistory = (
    ('asthma','Asthma'),
    ('autoimmune','Autoimmune'),
    ('COPD','COPD'),
    ('diabetes_mellitus','Diabetes Mellitus'),
    ('gastroesophageal_reflux_disease','Gastroesophageal Reflux Disease'),
    ('hypertension','Hypertension'),
    ('known_CAD(stenosis≥50%)','Known CAD (stenosis ≥50%)'),
    ('known_thoracic_aortic_aneurysm','Known thoracic aortic aneurysm'),
    ('liver_disease','Liver Disease'),
    ('low_hdl_cholestrol(<40mg/dl)','Low HDL Cholesterol (<40 mg/dl)'),
    ('Marfan Syndrome','Marfan Syndrome'),
    ('Presence of Malignancy','Presence of Malignancy'),
    ('Prior history of DVT or pulmonary embolism','Prior history of DVT or pulmonary embolism'),
    ('Recent Aortic Manipulation','Recent Aortic Manipulation'),
)
mdctn = (
    ('Aspirin','Aspirin'),
    ('Beta Blocker','Beta Blocker'),
    ('Birth Control Pills','Birth Control Pills'),
    ('Calcium Channel Blocker','Calcium Channel Blocker'),
    ('Cholestrol','Cholestrol'),
    ('Diabetes','Diabetes'),
    ('GI Medication','GI Medication'),
    ('Nitro','Nitro'),
    ('Noacs','NOACs'),
    ('Plavix','Plavix'),
    ('Steroids','Steroids'),
    ('Warfarin','Warfarin'),


)

fmly_n_social = (
    ('Family History of Aortic Disease','Family History of Aortic Disease'),
    ('Family History of Premature CAD','Family History of Premature CAD'),
    ('Smoker','Smoker'),
)

p_exam = (
    ('Decreased Breath Sounds','Decreased Breath Sounds'),
    ('Evidence of perfusion deficit (pulse deficit, systolic BP differential, or focal neurological deficit in conjunction with pain)',"Evidence of perfusion deficit (pulse deficit, systolic BP differential, or focal neurological deficit in conjunction with pain)"),
    ('Hypotension or Shock State','Hypotension or Shock State'),
    ('Irregular Heart Beat','Irregular Heart Beat'),
    ('New murmur of aortic insufficiency (with pain)','New murmur of aortic insufficiency (with pain)'),
    ('Pain at Epigastric','Pain at Epigastric'),
    ('Pericardial friction rub','Pericardial friction rub'),
    ('Rales','Rales'),
    ('Rash','Rash'),
    ('Reproducible chest wall tenderness','Reproducible chest wall tenderness'),
    ('Rhonchi','Rhonchi'),
    ('Unilateral Leg Swelling','Unilateral Leg Swelling'),
    ('Wheezes','Wheezes'),
)

wor_with = (
    ('Burping','Burping'),
    ('Eating','Eating'),
    ('Exertion','Exertion'),
    ('Lying Down','Lying Down'),
    ('Nitro','Nitro'),
    ('Palpation','Palpation'),
    ('Resting','Resting'),
    ('Sitting up','Sitting up'),
    ('Spicy Food','Spicy Food'),
    ('Taking a deep breath','Taking a deep breath'),
    ('Walking','Walking'),

)

imp_with = (
    ('Burping','Burping'),
    ('Eating','Eating'),
    ('Exertion','Exertion'),
    ('Lying Down','Lying Down'),
    ('Nitro','Nitro'),
    ('Palpation','Palpation'),
    ('Resting','Resting'),
    ('Sitting up','Sitting up'),
    ('Spicy Food','Spicy Food'),
    ('Taking a deep breath','Taking a deep breath'),
    ('Walking','Walking'),

)




class ChestPainForm(forms.ModelForm):
    age = forms.CharField(label='Age',widget=forms.TextInput(attrs={'type':'number','min':1,'max':88}))
    t = forms.ChoiceField(label='Age time unit', choices=ch , widget=forms.Select(choices=ch, attrs={'name':'t'}))
    duration = forms.ChoiceField(label='Duration', choices=d, widget=forms.Select(choices=d))
    tt = forms.ChoiceField(label='Duration time unit', choices=ch2, widget=forms.Select(choices=ch2,attrs={'name':'tt'}))
    quality = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=q,label="Quality") 
    associated_symptoms = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=assc_symptoms,label="Associated Symptoms",required=False)
    similar_to_prior = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=s_to_p, label="Similar to Prior",required=False)
    past_medical_history_of = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=past_mhistory, label="Past medical history",required=False)
    medication = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=mdctn,required=False)
    family_and_social_hx = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=fmly_n_social,required=False)
    physical_exam = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=p_exam,required=False)
    worsens_with = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=wor_with,required=False)
    improves_with = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=imp_with, required=False)





    

    class Meta:
        model = Chest_Pain
        fields = ('age','t','race','sex','quality','intensity','duration','tt','associated_symptoms','similar_to_prior',
        'worsens_with','improves_with','past_medical_history_of','medication','family_and_social_hx',
        'pulse','systolic_blood_pressure','diastolic_blood_pressure','pulse_oximetry','temperature','physical_exam')

        labels = {
            "temperature": ("Temperature °F (°C)"),
            "pulse_oximetry":("Pulse Oximetry %"),
            "systolic_blood_pressure":("Systolic Blood Pressure (mm Hg)(60-220)"),
            "diastolic_blood_pressure":("Diastolic Blood Pressure(mm Hg)(41-100)"),
        }
