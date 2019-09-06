from django.db import models

# Create your models here.


class Chest_Pain(models.Model):
    t = (
        ('d','Days'),
        ('m','Months'),
        ('y','Years'),
    )

    rc = (
        ('white','White'),
        ('black','Black or African American'),
        ('american_indian','American Indian or Alaska Native'),
        ('asian','Asian'),
        ('native_hawaiian','Native Hawaiian or Other Pacific Islander'),
        ('some_other','Some Other Race'),
    )

    sx = (
        ('m','Male'),
        ('f','Female'),
    )


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

    l = (
        ('right','Right'),
        ('left','Left'),
        ('middle','Middle'),
        ('upper','Upper'),
        ('lower','Lower'),
        ('bilateral','Bilateral'),
        ('flank','Flank'),
        ('back','Back'),
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
        ('copd','COPD'),
        ('diabetes_mellitus','Diabetes Mellitus'),
        ('gastroesophageal_reflux_disease','Gastroesophageal Reflux Disease'),
        ('hypertension','Hypertension'),
        ('known_cad','Known CAD (stenosis ≥50%)'),
        ('known_thoracic_aortic_aneurysm','Known thoracic aortic aneurysm'),
        ('liver_disease','Liver Disease'),
        ('low_hdl_cholestrol','Low HDL Cholesterol (<40 mg/dl)'),
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
        ('aortic_disease','Family History of Aortic Disease'),
        ('premature_cad','Family History of Premature CAD'),
        ('smoker','Smoker'),
    )



    p_exam = (
        ('decreased_breath_sounds','Decreased Breath Sounds'),
        ('evidence_of_perfusion',"Evidence of perfusion deficit (pulse deficit, systolic BP differential, or focal neurological deficit in conjunction with pain)"),
        ('hypotension_or_shockstate','Hypotension or Shock State'),
        ('irregular_heart_beat','Irregular Heart Beat'),
        ('murmur_of_aortic','New murmur of aortic insufficiency (with pain)'),
        ('pain_at_epigastric','Pain at Epigastric'),
        ('pericardial_friction_rub','Pericardial friction rub'),
        ('rales','Rales'),
        ('rash','Rash'),
        ('chest_wall_tenderness','Reproducible chest wall tenderness'),
        ('rhonchi','Rhonchi'),
        ('unilateral_leg_swelling','Unilateral Leg Swelling'),
        ('wheezes','Wheezes'),
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

    intns = (
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),

    )
    pls = (
        ('<60','<60'),
        ('61-100','61-100'),
        ('101-120','101-120'),
        ('121-150','121-150'),
        ('>150','>150'),

    )

    bp_sys = (
        ('<60','<60'),
        ('60-89','60-89'),
        ('90-120','90-120'),
        ('121-139','121-139'),
        ('140-179','140-179'),
        ('180-220','180-220'),
        ('>220','>220'),
    )

    bp_dias = (
        ('<41','<41'),
        ('41-60','41-60'),
        ('61-80','61-80'),
        ('81-90','81-90'),
        ('91-100','91-100'),
        ('>100','>100'),
    )

    pls_ox = (
        ('<90','<90'),
        ('90-94','90-94'),
        ('94-100','94-100'),
    )

    tmp = (
        ('<=95(35)','<=95(35)'),
        ('95.1-97.7(35.1-36.5)','95.1 - 97.7 (35.1 - 36.5)'),
        ('97.8-99.4(36.5-37.4)','97.8 -99.4 (36.5-37.4)'),
        ('99.5-100.3(37.6-37.9)','99.5 - 100.3 (37.6 - 37.9)'),
        ('100.5-101.9(38.0-38.9)','100.5 - 101.9 (38.0 - 38.9)'),
        ('>=102(>=38.9)','>=102 (>=38.9)')

    )


    age = models.CharField(max_length=100)
    race = models.CharField(max_length=100, choices=rc, null=True, blank=True)
    sex = models.CharField(max_length=100, choices=sx)
    quality = models.CharField(max_length=1000, null=True, blank=True)
    intensity = models.CharField(max_length=200, choices=intns, null=True, blank=True)
    duration = models.CharField(max_length=200, null=True, blank=True)
    associated_symptoms = models.CharField(max_length=1000, null=True, blank=True)
    similar_to_prior = models.CharField(max_length=200, null=True, blank=True)
    worsens_with = models.CharField(max_length=2000, null=True, blank=True)
    improves_with = models.CharField(max_length=2000, null=True, blank=True)
    past_medical_history_of = models.CharField(max_length=200, null=True, blank=True)
    medication = models.CharField(max_length=200, null=True, blank=True)
    family_and_social_hx = models.CharField(max_length=200, null=True, blank=True)
    #vitals = models.CharField(max_length=1000)
    pulse = models.CharField(max_length=1000,choices=pls, null=True, blank=True)
    systolic_blood_pressure = models.CharField(max_length=1000,choices=bp_sys, null=True, blank=True)
    diastolic_blood_pressure = models.CharField(max_length=1000,choices=bp_dias, null=True, blank=True)
    pulse_oximetry = models.CharField(max_length=1000,choices=pls_ox, null=True, blank=True)
    temperature = models.CharField(max_length=1000,choices=tmp, null=True, blank=True)
    physical_exam = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.age


