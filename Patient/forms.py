from django import forms
from .models import Chest_Pain

ch = [('days','Days'),('months','Months'),('years','Years')]
ch2 = [('seconds','Seconds'), ('minutes','Minutes'),('hours','Hours'),('days','Days'),('months','Months'),('years','Years')]
d = [('<1','<1'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),
('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('>20','>20')]
q = (
        ('abrupt_onset','Abrupt Onset'),
        ('aching_dull','Aching/Dull'),
        ('burning','Burning'),
        ('continuous','Continuous'),
        ('gradual','Gradual'),
        ('intermittent','Intermittent'),
        ('pressure','Pressure'),
        ('ripping_or_tearing','Ripping or Tearing'),
        ('sharp','Sharp'),
        ('tightness','Tightness'),
    )

assc_symptoms = (
    ('chills','Chills'),
    ('cough','Cough'),
    ('diaphoresis','Diaphoresis'),
    ('difficulty_swallowing','Difficulty Swallowing'),
    ('fever','Fever'),
    ('focal_neurologic_sign','Focal Neurologic Sign'),
    ('hematochezia','Hematochezia'),
    ('immobilization','Immobilization (>= 3 days) or surgery in the previous four weeks'),
    ('leg_swelling','Leg Swelling'),
    ('nausea','Nausea'),
    ('numbness','Numbness'),
    ('hemoptysis','Presence of Hemoptysis'),
    ('rash','Rash'),
    ('trauma_exertion','Recent Trauma or Physical Exertion'),
    ('severe_angina','Severe angina (≥2 episodes in 24 hrs)'),
    ('shortness_breath','Shortness of Breath'),
    ('syncope','Syncope'),
    ('tingling','Tingling'),
    ('vomiting','Vomiting'),
    ('vomiting_blood','Vomiting Blood'),
    ('weakness','Weakness'),
)

s_to_p = (
    ('aortic_dissection','Aortic Dissection'),
    ('cancer','Cancer'),
    ('cardiac_tamponade','Cardiac Tamponade'),
    ('chest_wall_contusion_strain','Chest wall contusion/strain'),
    ('gastroesophageal_reflux','Gastroesophageal Reflux'),
    ('gi_bleed','GI Bleed'),
    ('herpes_zoster','Herpes Zoster'),
    ('medication_related','Medication Related'),
    ('muscle_strain','Muscle Strain'),
    ('myocardial_infaction','Myocardial Infaction'),
    ('myocarditis','Myocarditis'),
    ('pericarditis','Pericarditis'),
    ('pneumonia','Pneumonia'),
    ('pneumothorax','Pneumothorax'),
    ('pulmonary_embolism','Pulmonary Embolism'),
    ('toxin_related','Toxin Related'),

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
    ('marfan_syndrome','Marfan Syndrome'),
    ('presence_of_malignancy','Presence of Malignancy'),
    ('prior_history_of_dvt_or_pulmonary_embolism','Prior history of DVT or pulmonary embolism'),
    ('recent_aortic_manipulation','Recent Aortic Manipulation'),
)
mdctn = (
    ('aspirin','Aspirin'),
    ('beta_blocker','Beta Blocker'),
    ('birth_control_pills','Birth Control Pills'),
    ('calcium_channel_blocker','Calcium Channel Blocker'),
    ('cholestrol','Cholestrol'),
    ('diabetes','Diabetes'),
    ('gi_medication','GI Medication'),
    ('nitro','Nitro'),
    ('noacs','NOACs'),
    ('plavix','Plavix'),
    ('steroids','Steroids'),
    ('warfarin','Warfarin'),


)

fmly_n_social = (
    ('family_history_of_aortic_disease','Family History of Aortic Disease'),
    ('family_history_of_premature_cad','Family History of Premature CAD'),
    ('smoker','Smoker'),
)

p_exam = (
    ('decreased_breath_sounds','Decreased Breath Sounds'),
    ('evidence_of_perfusion_deficit',"Evidence of perfusion deficit (pulse deficit, systolic BP differential, or focal neurological deficit in conjunction with pain)"),
    ('hypotension_or_shockstate','Hypotension or Shock State'),
    ('irregular_heart_beat','Irregular Heart Beat'),
    ('murmur_of_aortic_insufficiency(with_pain)','New murmur of aortic insufficiency (with pain)'),
    ('pain_at_epigastric','Pain at Epigastric'),
    ('pericardial_friction_rub','Pericardial friction rub'),
    ('rales','Rales'),
    ('rash','Rash'),
    ('reproducible_chest_wall_tenderness','Reproducible chest wall tenderness'),
    ('rhonchi','Rhonchi'),
    ('unilateral_leg_swelling','Unilateral Leg Swelling'),
    ('wheezes','Wheezes'),
)

wor_with = (
    ('burping','Burping'),
    ('eating','Eating'),
    ('exertion','Exertion'),
    ('lying_down','Lying Down'),
    ('nitro','Nitro'),
    ('palpation','Palpation'),
    ('resting','Resting'),
    ('sitting_up','Sitting up'),
    ('spicy_food','Spicy Food'),
    ('taking_breath','Taking a deep breath'),
    ('walking','Walking'),

)

imp_with = (
    ('burping','Burping'),
    ('eating','Eating'),
    ('exertion','Exertion'),
    ('lying_down','Lying Down'),
    ('nitro','Nitro'),
    ('palpation','Palpation'),
    ('resting','Resting'),
    ('sitting_up','Sitting up'),
    ('spicy_food','Spicy Food'),
    ('taking_breath','Taking a deep breath'),
    ('walking','Walking'),

)




class ChestPainForm(forms.ModelForm):
    age = forms.CharField(label='Age',widget=forms.TextInput(attrs={'type':'number','min':1,'max':88}))
    t = forms.ChoiceField(label='time unit', choices=ch , widget=forms.Select(choices=ch, attrs={'name':'t'}))
    duration = forms.ChoiceField(label='Duration', choices=d, widget=forms.Select(choices=d))
    tt = forms.ChoiceField(label='time unit', choices=ch2, widget=forms.Select(choices=ch2,attrs={'name':'tt'}))
    quality = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=q,label="Quality") 
    associated_symptoms = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=assc_symptoms,label="Associated Symptoms",)
    similar_to_prior = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=s_to_p, label="Similar to Prior")
    past_medical_history_of = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=past_mhistory, label="Past medical history")
    medication = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=mdctn)
    family_and_social_hx = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=fmly_n_social)
    physical_exam = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=p_exam)
    worsens_with = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=wor_with)
    improves_with = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=imp_with)




    

    class Meta:
        model = Chest_Pain
        fields = ('age','t','race','sex','quality','intensity','duration','tt','associated_symptoms','similar_to_prior',
        'worsens_with','improves_with','past_medical_history_of','medication','family_and_social_hx',
        'pulse','systolic_blood_pressure','diastolic_blood_pressure','pulse_oximetry','temperature','physical_exam')
