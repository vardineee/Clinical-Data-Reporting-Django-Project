from django.shortcuts import render
from django.views import generic
from clinicalsApp import models
from django.urls import reverse_lazy
from django.shortcuts import redirect,render
from clinicalsApp import forms

# Create your views here.
class PatientListView(generic.ListView):
    model = models.Patient




class PatientCreateView(generic.CreateView):
    model = models.Patient
    fields = ('firstName', 'lastName', 'age')
    success_url = reverse_lazy("index")

class PatientUpdateView(generic.UpdateView):
    model =models.Patient
    fields = ('firstName', 'lastName', 'age')
    success_url = reverse_lazy("index")



class PatientDeleteView(generic.DeleteView):
    model = models.Patient
    fields = ('firstName',)
    success_url =reverse_lazy("index")

def addData(request, pk):
    form = forms.ClinicalDataForm()
    patient = models.Patient.objects.get(id=pk)
    if request.method == "POST":
        form=forms.ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'clinicalsApp/clinicaldata_form.html', {'form':form, 'patient':patient})



def analyze(request, pk):
    data = models.ClinicalData.objects.filter(patient_id=pk)
    responseData = []
    for eachEntry in data:
        if eachEntry.componentName == 'hw':
            heightAndWeight = eachEntry.componentValue.split('/')
            if len(heightAndWeight) > 0:
                heightToMeters = float(heightAndWeight[0]) * 0.01
                BMI = float(heightAndWeight[1])/heightToMeters**2
                bmiEntry = models.ClinicalData()
                bmiEntry.componentName = 'BMI'
                bmiEntry.componentValue = BMI
                responseData.append(bmiEntry)

        responseData.append(eachEntry)

    return render (request, 'clinicalsApp/generateReport.html', {'data':responseData})
