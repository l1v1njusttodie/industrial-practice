from django.db import models


class AboutCompanyTable(models.Model):
    answer_id = models.AutoField(primary_key=True)
    code = models.TextField()
    name_ru = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return f"{self.answer_id}--{self.name_ru}"

    class Meta:
        db_table = "info_AboutCompanyTable"


class AddressesTable(models.Model):
    address_id = models.AutoField(primary_key=True)
    photo = models.TextField()
    address = models.TextField()
    link_2gis = models.TextField()

    def __str__(self):
        return f"{self.address_id}--{self.address}"

    class Meta:
        db_table = "info_AddressesTable"
