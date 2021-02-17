from django.shortcuts import render
from django.http import HttpResponse
from .models import general_safety,Machinery_Safety,Management_of_change,Quality_Assurance,SOP,Enviroment,Electrical_Safety,Fire_Protection,Engineering_Design,Industrial_Hygine_personal_Health,Ergonomics,Mechanical_Integrity,Contractor_Safety,General_Process_Safety,Community_Awareness_Emergency_Response

# Create your views here.


def index(request):

    return render(request,"pssr/page1.html",)

def general(request):
    print('form submited!')
    
   # this is to send data to db
    General_Safety_Items = request.POST.get("General_Safety_Items")
    radio = request.POST.get("radio")
    Explanation_of_the_deviation=request.POST.get("Explanation_of_the_deviation")
    Action_Item_description=request.POST.get("Action_Item_description")
    Responsibility=request.POST.get("Responsibility")
    Plan_date_of_completion=request.POST.get("Plan_date_of_completion")
    Actual_date_of_completion=request.POST.get("Actual_date_of_completion")
    Sever=request.POST.get("Sever")

    print(General_Safety_Items)
    
    generalsafety = general_safety(General_Safety_Items=General_Safety_Items,radio=radio,Explanation_of_the_deviation=Explanation_of_the_deviation,Action_Item_description=Action_Item_description,Responsibility=Responsibility, Plan_date_of_completion=Plan_date_of_completion, Actual_date_of_completion=Actual_date_of_completion,Sever=Sever )   #  table name as taken from models.py
    if General_Safety_Items!= None : 
        generalsafety.save()  #this will save datato DB
    return render(request,"pssr/general.html")

def general_output(request):
    data=general_safety.objects.all()

    return render(request,"pssr/general_output.html",{'general_data':data})

def Machinery_Safety_A(request):
    print('form submited!')
    
   # this is to send data to db
    Machinery_Safety_Items = request.POST.get("Machinery_Safety_Items")
    radio = request.POST.get("radio")
    Explanation_of_the_deviation=request.POST.get("Explanation_of_the_deviation")
    Action_Item_description=request.POST.get("Action_Item_description")
    Responsibility=request.POST.get("Responsibility")
    Plan_date_of_completion=request.POST.get("Plan_date_of_completion")
    Actual_date_of_completion=request.POST.get("Actual_date_of_completion")
    Sever=request.POST.get("Sever")

    print(Machinery_Safety_Items)
    
    MachinerySafety = Machinery_Safety(Machinery_Safety_Items=Machinery_Safety_Items,radio=radio,Explanation_of_the_deviation=Explanation_of_the_deviation,Action_Item_description=Action_Item_description,Responsibility=Responsibility, Plan_date_of_completion=Plan_date_of_completion, Actual_date_of_completion=Actual_date_of_completion,Sever=Sever )   #  table name as taken from models.py
    if Machinery_Safety_Items!= None : 
        MachinerySafety.save()  #this will save datato DB
    return render(request,"pssr/Machinerysafety.html")

def Machinery_Safety_output(request):
    data=Machinery_Safety.objects.all()

    return render(request,"pssr/Machinerysafety_output.html",{'Machinerysafety_data':data})

def Management_of_change_A(request):
    print('form submited!')
    
   # this is to send data to db
    Management_of_change_Items = request.POST.get("Management_of_change_Items")
    radio = request.POST.get("radio")
    Explanation_of_the_deviation=request.POST.get("Explanation_of_the_deviation")
    Action_Item_description=request.POST.get("Action_Item_description")
    Responsibility=request.POST.get("Responsibility")
    Plan_date_of_completion=request.POST.get("Plan_date_of_completion")
    Actual_date_of_completion=request.POST.get("Actual_date_of_completion")
    Sever=request.POST.get("Sever")

    print(Management_of_change_Items)
    
    Management_of_change1 = Management_of_change(Management_of_change_Items=Management_of_change_Items,radio=radio,Explanation_of_the_deviation=Explanation_of_the_deviation,Action_Item_description=Action_Item_description,Responsibility=Responsibility, Plan_date_of_completion=Plan_date_of_completion, Actual_date_of_completion=Actual_date_of_completion,Sever=Sever )   #  table name as taken from models.py
    if Management_of_change_Items!= None : 
        Management_of_change1.save()  #this will save datato DB
    return render(request,"pssr/Managementofchange.html")

def Management_of_change_output(request):
    data=Management_of_change.objects.all()

    return render(request,"pssr/Managementofchange_output.html",{'Managementofchange_data':data})

def Quality_Assurance_A(request):
    print('form submited!')
    
   # this is to send data to db
    Quality_Assurance_Items = request.POST.get("Quality_Assurance_Items")
    radio = request.POST.get("radio")
    Explanation_of_the_deviation=request.POST.get("Explanation_of_the_deviation")
    Action_Item_description=request.POST.get("Action_Item_description")
    Responsibility=request.POST.get("Responsibility")
    Plan_date_of_completion=request.POST.get("Plan_date_of_completion")
    Actual_date_of_completion=request.POST.get("Actual_date_of_completion")
    Sever=request.POST.get("Sever")

    print(Quality_Assurance_Items)
    
    Quality_Assurance1 = Quality_Assurance(Quality_Assurance_Items=Quality_Assurance_Items,radio=radio,Explanation_of_the_deviation=Explanation_of_the_deviation,Action_Item_description=Action_Item_description,Responsibility=Responsibility, Plan_date_of_completion=Plan_date_of_completion, Actual_date_of_completion=Actual_date_of_completion,Sever=Sever )   #  table name as taken from models.py
    if Quality_Assurance_Items!= None : 
        Quality_Assurance1.save()  #this will save datato DB
    return render(request,"pssr/QualityAssurance.html")

def Quality_Assurance_output(request):
    data=Quality_Assurance.objects.all()

    return render(request,"pssr/QualityAssurance_output.html",{'Quality_Assurance_data':data})

def SOP_A(request):
    print('form submited!')
    
   # this is to send data to db
    SOP_Items = request.POST.get("SOP_Items")
    radio = request.POST.get("radio")
    Explanation_of_the_deviation=request.POST.get("Explanation_of_the_deviation")
    Action_Item_description=request.POST.get("Action_Item_description")
    Responsibility=request.POST.get("Responsibility")
    Plan_date_of_completion=request.POST.get("Plan_date_of_completion")
    Actual_date_of_completion=request.POST.get("Actual_date_of_completion")
    Sever=request.POST.get("Sever")

    print(SOP_Items)
    
    SOP1 = SOP(SOP_Items=SOP_Items,radio=radio,Explanation_of_the_deviation=Explanation_of_the_deviation,Action_Item_description=Action_Item_description,Responsibility=Responsibility, Plan_date_of_completion=Plan_date_of_completion, Actual_date_of_completion=Actual_date_of_completion,Sever=Sever )   #  table name as taken from models.py
    if SOP_Items!= None : 
        SOP1.save()  #this will save datato DB
    return render(request,"pssr/SOP.html")

def SOP_output(request):
    data=SOP.objects.all()

    return render(request,"pssr/SOP_output.html",{'SOP_data':data})

def Enviroment_A(request):
    print('form submited!')
    
   # this is to send data to db
    Enviroment_Items = request.POST.get("Enviroment_Items")
    radio = request.POST.get("radio")
    Explanation_of_the_deviation=request.POST.get("Explanation_of_the_deviation")
    Action_Item_description=request.POST.get("Action_Item_description")
    Responsibility=request.POST.get("Responsibility")
    Plan_date_of_completion=request.POST.get("Plan_date_of_completion")
    Actual_date_of_completion=request.POST.get("Actual_date_of_completion")
    Sever=request.POST.get("Sever")

    print(Enviroment_Items)
    
    Enviroment1 = Enviroment(Enviroment_Items=Enviroment_Items,radio=radio,Explanation_of_the_deviation=Explanation_of_the_deviation,Action_Item_description=Action_Item_description,Responsibility=Responsibility, Plan_date_of_completion=Plan_date_of_completion, Actual_date_of_completion=Actual_date_of_completion,Sever=Sever )   #  table name as taken from models.py
    if Enviroment_Items!= None : 
        Enviroment1.save()  #this will save datato DB
    return render(request,"pssr/ENVIROMENT.html")

def Enviroment_output(request):
    data=Enviroment.objects.all()

    return render(request,"pssr/ENVIROMENT_output.html",{'ENVIROMENT_data':data})

def Electrical_Safety_A(request):
    print('form submited!')
    
   # this is to send data to db
    Electrical_Safety_Items = request.POST.get("Electrical_Safety_Items")
    radio = request.POST.get("radio")
    Explanation_of_the_deviation=request.POST.get("Explanation_of_the_deviation")
    Action_Item_description=request.POST.get("Action_Item_description")
    Responsibility=request.POST.get("Responsibility")
    Plan_date_of_completion=request.POST.get("Plan_date_of_completion")
    Actual_date_of_completion=request.POST.get("Actual_date_of_completion")
    Sever=request.POST.get("Sever")

    print(Electrical_Safety_Items)
    
    Electrical_Safety1 = Electrical_Safety(Electrical_Safety_Items=Electrical_Safety_Items,radio=radio,Explanation_of_the_deviation=Explanation_of_the_deviation,Action_Item_description=Action_Item_description,Responsibility=Responsibility, Plan_date_of_completion=Plan_date_of_completion, Actual_date_of_completion=Actual_date_of_completion,Sever=Sever )   #  table name as taken from models.py
    if Electrical_Safety_Items!= None : 
        Electrical_Safety1.save()  #this will save datato DB
    return render(request,"pssr/ELECTRICALS.html")

def Electrical_Safety_output(request):
    data=Electrical_Safety.objects.all()

    return render(request,"pssr/ELECTRICALS_output.html",{'ELECTRICALS_data':data})

def Fire_Protection_A(request):
    print('form submited!')
    
   # this is to send data to db
    Fire_Protection_Items = request.POST.get("Fire_Protection_Items")
    radio = request.POST.get("radio")
    Explanation_of_the_deviation=request.POST.get("Explanation_of_the_deviation")
    Action_Item_description=request.POST.get("Action_Item_description")
    Responsibility=request.POST.get("Responsibility")
    Plan_date_of_completion=request.POST.get("Plan_date_of_completion")
    Actual_date_of_completion=request.POST.get("Actual_date_of_completion")
    Sever=request.POST.get("Sever")

    print(Fire_Protection_Items)
    
    Fire_Protection1 = Fire_Protection(Fire_Protection_Items=Fire_Protection_Items,radio=radio,Explanation_of_the_deviation=Explanation_of_the_deviation,Action_Item_description=Action_Item_description,Responsibility=Responsibility, Plan_date_of_completion=Plan_date_of_completion, Actual_date_of_completion=Actual_date_of_completion,Sever=Sever )   #  table name as taken from models.py
    if Fire_Protection_Items!= None : 
        Fire_Protection1.save()  #this will save datato DB
    return render(request,"pssr/FIREPROTECTION.html")

def Fire_Protection_output(request):
    data=Fire_Protection.objects.all()

    return render(request,"pssr/FIREPROTECTION_output.html",{'FIREPROTECTION_data':data})

def Engineering_Design_A(request):
    print('form submited!')
    
   # this is to send data to db
    Engineering_Design_Items = request.POST.get("Engineering_Design_Items")
    radio = request.POST.get("radio")
    Explanation_of_the_deviation=request.POST.get("Explanation_of_the_deviation")
    Action_Item_description=request.POST.get("Action_Item_description")
    Responsibility=request.POST.get("Responsibility")
    Plan_date_of_completion=request.POST.get("Plan_date_of_completion")
    Actual_date_of_completion=request.POST.get("Actual_date_of_completion")
    Sever=request.POST.get("Sever")

    print(Engineering_Design_Items)
    
    Engineering_Design1 = Engineering_Design(Engineering_Design_Items=Engineering_Design_Items,radio=radio,Explanation_of_the_deviation=Explanation_of_the_deviation,Action_Item_description=Action_Item_description,Responsibility=Responsibility, Plan_date_of_completion=Plan_date_of_completion, Actual_date_of_completion=Actual_date_of_completion,Sever=Sever )   #  table name as taken from models.py
    if Engineering_Design_Items!= None : 
        Engineering_Design1.save()  #this will save datato DB
    return render(request,"pssr/ENGINEERINGDESIGN.html")

def Engineering_Design_output(request):
    data=Engineering_Design.objects.all()

    return render(request,"pssr/ENGINEERINGDESIGN_output.html",{'ENGINEERINGDESIGN_data':data})

def Industrial_Hygine_personal_Health_A(request):
    print('form submited!')
    
   # this is to send data to db
    Industrial_Hygine_personal_Health_Items = request.POST.get("Industrial_Hygine_personal_Health_Items")
    radio = request.POST.get("radio")
    Explanation_of_the_deviation=request.POST.get("Explanation_of_the_deviation")
    Action_Item_description=request.POST.get("Action_Item_description")
    Responsibility=request.POST.get("Responsibility")
    Plan_date_of_completion=request.POST.get("Plan_date_of_completion")
    Actual_date_of_completion=request.POST.get("Actual_date_of_completion")
    Sever=request.POST.get("Sever")

    print(Industrial_Hygine_personal_Health_Items)
    
    Industrial_Hygine_personal_Health1 = Industrial_Hygine_personal_Health(Industrial_Hygine_personal_Health_Items=Industrial_Hygine_personal_Health_Items,radio=radio,Explanation_of_the_deviation=Explanation_of_the_deviation,Action_Item_description=Action_Item_description,Responsibility=Responsibility, Plan_date_of_completion=Plan_date_of_completion, Actual_date_of_completion=Actual_date_of_completion,Sever=Sever )   #  table name as taken from models.py
    if Industrial_Hygine_personal_Health_Items!= None : 
        Industrial_Hygine_personal_Health1.save()  #this will save datato DB
    return render(request,"pssr/INDUSTRIALHYGIENE.html")

def Industrial_Hygine_personal_Health_output(request):
    data=Industrial_Hygine_personal_Health.objects.all()

    return render(request,"pssr/INDUSTRIALHYGIENE_output.html",{'INDUSTRIALHYGIENE_data':data})

def Ergonomics_A(request):
    print('form submited!')
    
   # this is to send data to db
    Ergonomics_Items = request.POST.get("Ergonomics_Items")
    radio = request.POST.get("radio")
    Explanation_of_the_deviation=request.POST.get("Explanation_of_the_deviation")
    Action_Item_description=request.POST.get("Action_Item_description")
    Responsibility=request.POST.get("Responsibility")
    Plan_date_of_completion=request.POST.get("Plan_date_of_completion")
    Actual_date_of_completion=request.POST.get("Actual_date_of_completion")
    Sever=request.POST.get("Sever")

    print(Ergonomics_Items)
    
    Ergonomics1 = Ergonomics(Ergonomics_Items=Ergonomics_Items,radio=radio,Explanation_of_the_deviation=Explanation_of_the_deviation,Action_Item_description=Action_Item_description,Responsibility=Responsibility, Plan_date_of_completion=Plan_date_of_completion, Actual_date_of_completion=Actual_date_of_completion,Sever=Sever )   #  table name as taken from models.py
    if Ergonomics_Items!= None : 
        Ergonomics1.save()  #this will save datato DB
    return render(request,"pssr/ERGONOMICS.html")

def Ergonomics_output(request):
    data=Ergonomics.objects.all()

    return render(request,"pssr/ERGONOMICS_output.html",{'ERGONOMICS_data':data})

def Mechanical_Integrity_A(request):
    print('form submited!')
    
   # this is to send data to db
    Mechanical_Integrity_Items = request.POST.get("Mechanical_Integrity_Items")
    radio = request.POST.get("radio")
    Explanation_of_the_deviation=request.POST.get("Explanation_of_the_deviation")
    Action_Item_description=request.POST.get("Action_Item_description")
    Responsibility=request.POST.get("Responsibility")
    Plan_date_of_completion=request.POST.get("Plan_date_of_completion")
    Actual_date_of_completion=request.POST.get("Actual_date_of_completion")
    Sever=request.POST.get("Sever")

    print(Mechanical_Integrity_Items)
    
    Mechanical_Integrity1 = Mechanical_Integrity(Mechanical_Integrity_Items=Mechanical_Integrity_Items,radio=radio,Explanation_of_the_deviation=Explanation_of_the_deviation,Action_Item_description=Action_Item_description,Responsibility=Responsibility, Plan_date_of_completion=Plan_date_of_completion, Actual_date_of_completion=Actual_date_of_completion,Sever=Sever )   #  table name as taken from models.py
    if Mechanical_Integrity_Items!= None : 
        Mechanical_Integrity1.save()  #this will save datato DB
    return render(request,"pssr/MECHANICALINTEGRITY.html")

def Mechanical_Integrity_output(request):
    data=Mechanical_Integrity.objects.all()

    return render(request,"pssr/MECHANICALINTEGRITY_output.html",{'MECHANICALINTEGRITY_data':data})

def Contractor_Safety_A(request):
    print('form submited!')
    
   # this is to send data to db
    Contractor_Safety_Items = request.POST.get("Contractor_Safety_Items")
    radio = request.POST.get("radio")
    Explanation_of_the_deviation=request.POST.get("Explanation_of_the_deviation")
    Action_Item_description=request.POST.get("Action_Item_description")
    Responsibility=request.POST.get("Responsibility")
    Plan_date_of_completion=request.POST.get("Plan_date_of_completion")
    Actual_date_of_completion=request.POST.get("Actual_date_of_completion")
    Sever=request.POST.get("Sever")

    print(Contractor_Safety_Items)
    
    Contractor_Safety1 = Contractor_Safety(Contractor_Safety_Items=Contractor_Safety_Items,radio=radio,Explanation_of_the_deviation=Explanation_of_the_deviation,Action_Item_description=Action_Item_description,Responsibility=Responsibility, Plan_date_of_completion=Plan_date_of_completion, Actual_date_of_completion=Actual_date_of_completion,Sever=Sever )   #  table name as taken from models.py
    if Contractor_Safety_Items!= None : 
        Contractor_Safety1.save()  #this will save datato DB
    return render(request,"pssr/CONTRACTORSAFETY.html")

def Contractor_Safety_output(request):
    data=Contractor_Safety.objects.all()

    return render(request,"pssr/CONTRACTORSAFETY_output.html",{'CONTRACTORSAFETY_data':data})

def General_Process_Safety_A(request):
    print('form submited!')
    
   # this is to send data to db
    General_Process_Safety_Items = request.POST.get("General_Process_Safety_Items")
    radio = request.POST.get("radio")
    Explanation_of_the_deviation=request.POST.get("Explanation_of_the_deviation")
    Action_Item_description=request.POST.get("Action_Item_description")
    Responsibility=request.POST.get("Responsibility")
    Plan_date_of_completion=request.POST.get("Plan_date_of_completion")
    Actual_date_of_completion=request.POST.get("Actual_date_of_completion")
    Sever=request.POST.get("Sever")

    print(General_Process_Safety_Items)
    
    General_Process_Safety1 = General_Process_Safety(General_Process_Safety_Items=General_Process_Safety_Items,radio=radio,Explanation_of_the_deviation=Explanation_of_the_deviation,Action_Item_description=Action_Item_description,Responsibility=Responsibility, Plan_date_of_completion=Plan_date_of_completion, Actual_date_of_completion=Actual_date_of_completion,Sever=Sever )   #  table name as taken from models.py
    if General_Process_Safety_Items!= None : 
        General_Process_Safety1.save()  #this will save datato DB
    return render(request,"pssr/GENERALPROCESSSAFETY.html")

def General_Process_Safety_output(request):
    data=General_Process_Safety.objects.all()

    return render(request,"pssr/GENERALPROCESSSAFETY_output.html",{'GENERALPROCESSSAFETY_data':data})

def Community_Awareness_Emergency_Response_A(request):
    print('form submited!')
    
   # this is to send data to db
    Community_Awareness_Emergency_Response_Items = request.POST.get("Community_Awareness_Emergency_Response_Items")
    radio = request.POST.get("radio")
    Explanation_of_the_deviation=request.POST.get("Explanation_of_the_deviation")
    Action_Item_description=request.POST.get("Action_Item_description")
    Responsibility=request.POST.get("Responsibility")
    Plan_date_of_completion=request.POST.get("Plan_date_of_completion")
    Actual_date_of_completion=request.POST.get("Actual_date_of_completion")
    Sever=request.POST.get("Sever")

    print(Community_Awareness_Emergency_Response_Items)
    
    Community_Awareness_Emergency_Response1 = Community_Awareness_Emergency_Response(Community_Awareness_Emergency_Response_Items=Community_Awareness_Emergency_Response_Items,radio=radio,Explanation_of_the_deviation=Explanation_of_the_deviation,Action_Item_description=Action_Item_description,Responsibility=Responsibility, Plan_date_of_completion=Plan_date_of_completion, Actual_date_of_completion=Actual_date_of_completion,Sever=Sever )   #  table name as taken from models.py
    if Community_Awareness_Emergency_Response_Items!= None : 
        Community_Awareness_Emergency_Response1.save()  #this will save datato DB
    return render(request,"pssr/COMMUNITYAWARENESS.html")

def Community_Awareness_Emergency_Response_output(request):
    data=Community_Awareness_Emergency_Response.objects.all()

    return render(request,"pssr/COMMUNITYAWARENESS_output.html",{'COMMUNITYAWARENESS_data':data})
