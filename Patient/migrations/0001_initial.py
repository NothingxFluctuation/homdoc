# Generated by Django 2.2.3 on 2019-08-31 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chest_Pain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=100)),
                ('race', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('quality', models.CharField(choices=[('abrupt_onset', 'Abrupt Onset'), ('aching_dull', 'Aching/Dull'), ('burning', 'Burning'), ('continuous', 'Continuous'), ('gradual', 'Gradual'), ('intermittent', 'Intermittent'), ('pressure', 'Pressure'), ('ripping_or_tearing', 'Ripping or Tearing'), ('sharp', 'Sharp'), ('tightness', 'Tightness')], max_length=100)),
                ('intensity', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
                ('associated_symptoms', models.CharField(max_length=1000)),
                ('similar_to_prior', models.CharField(choices=[('aortic_dissection', 'Aortic Dissection'), ('cancer', 'Cancer'), ('cardiac_tamponade', 'Cardiac Tamponade'), ('chest_wall_contusion_strain', 'Chest wall contusion/strain'), ('gastroesophageal_reflux', 'Gastroesophageal Reflux'), ('gi_bleed', 'GI Bleed'), ('herpes_zoster', 'Herpes Zoster'), ('medication_related', 'Medication Related'), ('muscle_strain', 'Muscle Strain'), ('myocardial_infaction', 'Myocardial Infaction'), ('myocarditis', 'Myocarditis'), ('pericarditis', 'Pericarditis'), ('pneumonia', 'Pneumonia'), ('pneumothorax', 'Pneumothorax'), ('pulmonary_embolism', 'Pulmonary Embolism'), ('toxin_related', 'Toxin Related')], max_length=200)),
                ('worsens_with', models.CharField(max_length=2000)),
                ('improves_with', models.CharField(max_length=2000)),
                ('past_medical_history_of', models.CharField(choices=[('asthma', 'Asthma'), ('autoimmune', 'Autoimmune'), ('copd', 'COPD'), ('diabetes_mellitus', 'Diabetes Mellitus'), ('gastroesophageal_reflux_disease', 'Gastroesophageal Reflux Disease'), ('hypertension', 'Hypertension'), ('known_cad', 'Known CAD (stenosis ≥50%)'), ('known_thoracic_aortic_aneurysm', 'Known thoracic aortic aneurysm'), ('liver_disease', 'Liver Disease'), ('low_hdl_cholestrol', 'Low HDL Cholesterol (<40 mg/dl)'), ('marfan_syndrome', 'Marfan Syndrome'), ('presence_of_malignancy', 'Presence of Malignancy'), ('prior_history_of_dvt_or_pulmonary_embolism', 'Prior history of DVT or pulmonary embolism'), ('recent_aortic_manipulation', 'Recent Aortic Manipulation')], max_length=200)),
                ('medication', models.CharField(choices=[('aspirin', 'Aspirin'), ('beta_blocker', 'Beta Blocker'), ('birth_control_pills', 'Birth Control Pills'), ('calcium_channel_blocker', 'Calcium Channel Blocker'), ('cholestrol', 'Cholestrol'), ('diabetes', 'Diabetes'), ('gi_medication', 'GI Medication'), ('nitro', 'Nitro'), ('noacs', 'NOACs'), ('plavix', 'Plavix'), ('steroids', 'Steroids'), ('warfarin', 'Warfarin')], max_length=200)),
                ('family_and_social_hx', models.CharField(choices=[('aortic_disease', 'Family History of Aortic Disease'), ('premature_cad', 'Family History of Premature CAD'), ('smoker', 'Smoker')], max_length=200)),
                ('vitals', models.CharField(max_length=1000)),
                ('pulse', models.CharField(max_length=1000)),
                ('systolic_blood_pressure', models.CharField(max_length=1000)),
                ('diastolic_blood_pressure', models.CharField(max_length=1000)),
                ('pulse_oximetry', models.CharField(max_length=1000)),
                ('temperature', models.CharField(max_length=1000)),
                ('physical_exam', models.CharField(choices=[('decreased_breath_sounds', 'Decreased Breath Sounds'), ('evidence_of_perfusion', 'Evidence of perfusion deficit (pulse deficit, systolic BP differential, or focal neurological deficit in conjunction with pain)'), ('hypotension_or_shockstate', 'Hypotension or Shock State'), ('irregular_heart_beat', 'Irregular Heart Beat'), ('murmur_of_aortic', 'New murmur of aortic insufficiency (with pain)'), ('pain_at_epigastric', 'Pain at Epigastric'), ('pericardial_friction_rub', 'Pericardial friction rub'), ('rales', 'Rales'), ('rash', 'Rash'), ('chest_wall_tenderness', 'Reproducible chest wall tenderness'), ('rhonchi', 'Rhonchi'), ('unilateral_leg_swelling', 'Unilateral Leg Swelling'), ('wheezes', 'Wheezes')], max_length=1000)),
            ],
        ),
    ]