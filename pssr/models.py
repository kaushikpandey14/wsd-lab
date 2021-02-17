from django.db import models

# Create your models here.
class general_safety(models.Model):
    General_Safety_Items = models.CharField(max_length=900, default=' ',null=True)
    radio = models.CharField(max_length=300, default=' ',null=True)
    Explanation_of_the_deviation = models.CharField(max_length=400, default=' ',null=True)
    Action_Item_description = models.CharField(max_length=400, default=' ',null=True)
    Responsibility = models.CharField(max_length=300, default=' ',null=True)
    Plan_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Actual_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Sever = models.CharField(max_length=300, default=' ',null=True)

    def __str__(self):
        return str(self.General_Safety_Items)

class Machinery_Safety(models.Model):
    Machinery_Safety_Items = models.CharField(max_length=900, default=' ',null=True)
    radio = models.CharField(max_length=300, default=' ',null=True)
    Explanation_of_the_deviation = models.CharField(max_length=400, default=' ',null=True)
    Action_Item_description = models.CharField(max_length=400, default=' ',null=True)
    Responsibility = models.CharField(max_length=300, default=' ',null=True)
    Plan_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Actual_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Sever = models.CharField(max_length=300, default=' ',null=True)

    def __str__(self):
        return str(self.Machinery_Safety_Items)

class Management_of_change(models.Model):
    Management_of_change_Items = models.CharField(max_length=900, default=' ',null=True)
    radio = models.CharField(max_length=300, default=' ',null=True)
    Explanation_of_the_deviation = models.CharField(max_length=400, default=' ',null=True)
    Action_Item_description = models.CharField(max_length=400, default=' ',null=True)
    Responsibility = models.CharField(max_length=300, default=' ',null=True)
    Plan_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Actual_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Sever = models.CharField(max_length=300, default=' ',null=True)

    def __str__(self):
        return str(self.Management_of_change_Items)

class Quality_Assurance(models.Model):
    Quality_Assurance_Items = models.CharField(max_length=900, default=' ',null=True)
    radio = models.CharField(max_length=300, default=' ',null=True)
    Explanation_of_the_deviation = models.CharField(max_length=400, default=' ',null=True)
    Action_Item_description = models.CharField(max_length=400, default=' ',null=True)
    Responsibility = models.CharField(max_length=300, default=' ',null=True)
    Plan_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Actual_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Sever = models.CharField(max_length=300, default=' ',null=True)

    def __str__(self):
        return str(self.Quality_Assurance_Items)

class SOP(models.Model):
    SOP_Items = models.CharField(max_length=900, default=' ',null=True)
    radio = models.CharField(max_length=300, default=' ',null=True)
    Explanation_of_the_deviation = models.CharField(max_length=400, default=' ',null=True)
    Action_Item_description = models.CharField(max_length=400, default=' ',null=True)
    Responsibility = models.CharField(max_length=300, default=' ',null=True)
    Plan_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Actual_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Sever = models.CharField(max_length=300, default=' ',null=True)

    def __str__(self):
        return str(self.SOP_Items)

class Enviroment(models.Model):
    Enviroment_Items = models.CharField(max_length=900, default=' ',null=True)
    radio = models.CharField(max_length=300, default=' ',null=True)
    Explanation_of_the_deviation = models.CharField(max_length=400, default=' ',null=True)
    Action_Item_description = models.CharField(max_length=400, default=' ',null=True)
    Responsibility = models.CharField(max_length=300, default=' ',null=True)
    Plan_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Actual_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Sever = models.CharField(max_length=300, default=' ',null=True)

    def __str__(self):
        return str(self.Enviroment_Items)

class Electrical_Safety(models.Model):
    Electrical_Safety_Items = models.CharField(max_length=900, default=' ',null=True)
    radio = models.CharField(max_length=300, default=' ',null=True)
    Explanation_of_the_deviation = models.CharField(max_length=400, default=' ',null=True)
    Action_Item_description = models.CharField(max_length=400, default=' ',null=True)
    Responsibility = models.CharField(max_length=300, default=' ',null=True)
    Plan_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Actual_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Sever = models.CharField(max_length=300, default=' ',null=True)

    def __str__(self):
        return str(self.Electrical_Safety_Items)

class Fire_Protection(models.Model):
    Fire_Protection_Items = models.CharField(max_length=900, default=' ',null=True)
    radio = models.CharField(max_length=300, default=' ',null=True)
    Explanation_of_the_deviation = models.CharField(max_length=400, default=' ',null=True)
    Action_Item_description = models.CharField(max_length=400, default=' ',null=True)
    Responsibility = models.CharField(max_length=300, default=' ',null=True)
    Plan_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Actual_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Sever = models.CharField(max_length=300, default=' ',null=True)

    def __str__(self):
        return str(self.Fire_Protection_Items)

class Engineering_Design(models.Model):
    Engineering_Design_Items = models.CharField(max_length=900, default=' ',null=True)
    radio = models.CharField(max_length=300, default=' ',null=True)
    Explanation_of_the_deviation = models.CharField(max_length=400, default=' ',null=True)
    Action_Item_description = models.CharField(max_length=400, default=' ',null=True)
    Responsibility = models.CharField(max_length=300, default=' ',null=True)
    Plan_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Actual_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Sever = models.CharField(max_length=300, default=' ',null=True)

    def __str__(self):
        return str(self.Engineering_Design_Items)

class Industrial_Hygine_personal_Health(models.Model):
    Industrial_Hygine_personal_Health_Items = models.CharField(max_length=900, default=' ',null=True)
    radio = models.CharField(max_length=300, default=' ',null=True)
    Explanation_of_the_deviation = models.CharField(max_length=400, default=' ',null=True)
    Action_Item_description = models.CharField(max_length=400, default=' ',null=True)
    Responsibility = models.CharField(max_length=300, default=' ',null=True)
    Plan_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Actual_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Sever = models.CharField(max_length=300, default=' ',null=True)

    def __str__(self):
        return str(self.Industrial_Hygine_personal_Health_Items)

class Ergonomics(models.Model):
    Ergonomics_Items = models.CharField(max_length=900, default=' ',null=True)
    radio = models.CharField(max_length=300, default=' ',null=True)
    Explanation_of_the_deviation = models.CharField(max_length=400, default=' ',null=True)
    Action_Item_description = models.CharField(max_length=400, default=' ',null=True)
    Responsibility = models.CharField(max_length=300, default=' ',null=True)
    Plan_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Actual_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Sever = models.CharField(max_length=300, default=' ',null=True)

    def __str__(self):
        return str(self.Ergonomics_Items)

class Mechanical_Integrity(models.Model):
    Mechanical_Integrity_Items = models.CharField(max_length=900, default=' ',null=True)
    radio = models.CharField(max_length=300, default=' ',null=True)
    Explanation_of_the_deviation = models.CharField(max_length=400, default=' ',null=True)
    Action_Item_description = models.CharField(max_length=400, default=' ',null=True)
    Responsibility = models.CharField(max_length=300, default=' ',null=True)
    Plan_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Actual_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Sever = models.CharField(max_length=300, default=' ',null=True)

    def __str__(self):
        return str(self.Mechanical_Integrity_Items)

class Contractor_Safety(models.Model):
    Contractor_Safety_Items = models.CharField(max_length=900, default=' ',null=True)
    radio = models.CharField(max_length=300, default=' ',null=True)
    Explanation_of_the_deviation = models.CharField(max_length=400, default=' ',null=True)
    Action_Item_description = models.CharField(max_length=400, default=' ',null=True)
    Responsibility = models.CharField(max_length=300, default=' ',null=True)
    Plan_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Actual_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Sever = models.CharField(max_length=300, default=' ',null=True)

    def __str__(self):
        return str(self.Contractor_Safety_Items)

class General_Process_Safety(models.Model):
    General_Process_Safety_Items = models.CharField(max_length=900, default=' ',null=True)
    radio = models.CharField(max_length=300, default=' ',null=True)
    Explanation_of_the_deviation = models.CharField(max_length=400, default=' ',null=True)
    Action_Item_description = models.CharField(max_length=400, default=' ',null=True)
    Responsibility = models.CharField(max_length=300, default=' ',null=True)
    Plan_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Actual_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Sever = models.CharField(max_length=300, default=' ',null=True)

    def __str__(self):
        return str(self.General_Process_Safety_Items)

class Community_Awareness_Emergency_Response(models.Model):
    Community_Awareness_Emergency_Response_Items = models.CharField(max_length=900, default=' ',null=True)
    radio = models.CharField(max_length=300, default=' ',null=True)
    Explanation_of_the_deviation = models.CharField(max_length=400, default=' ',null=True)
    Action_Item_description = models.CharField(max_length=400, default=' ',null=True)
    Responsibility = models.CharField(max_length=300, default=' ',null=True)
    Plan_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Actual_date_of_completion = models.CharField(max_length=15, default=' ',null=True)
    Sever = models.CharField(max_length=300, default=' ',null=True)

    def __str__(self):
        return str(self.Community_Awareness_Emergency_Response_Items)

