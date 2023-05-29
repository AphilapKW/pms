from django.db import models
from django.contrib.auth.models import User


class WorkOrder(models.Model):
    WORK_ORDER_STATUS_CHOICES = (
        ('Created', 'Created'),
        ('Assigned', 'Assigned'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        ('Cancel', 'Cancel'),
    )

    WORK_ORDER_TYPE_CHOICES = (
        ('Cleaning', 'Cleaning'),
        ('Maid Request', 'Maid Request'),
        ('Technician Request', 'Technician Request'),
        ('Amenity Request', 'Amenity Request'),
    )

    room = models.CharField(max_length=50)
    work_order_number = models.CharField(max_length=50, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_work_orders')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_work_orders')
    started_at = models.DateTimeField(null=True)
    finished_at = models.DateTimeField(null=True)
    work_type = models.CharField(max_length=50, choices=WORK_ORDER_TYPE_CHOICES)
    work_status = models.CharField(max_length=50, choices=WORK_ORDER_STATUS_CHOICES)

    admin_list_display = ('room', 'work_order_number', 'created_by', 'work_type', 'work_status', 'assigned_to', 'started_at', 'finished_at')
    admin_search_fields = ('room', 'work_order_number', 'work_type', 'work_status', 'assigned_to', 'created_by', 'started_at')
    admin_raw_id_fields = ('created_by', 'assigned_to',)

    class Meta:
        db_table = "work_order"


class MaidRequest(models.Model):
    work_order = models.OneToOneField(WorkOrder, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField()

    admin_list_display = ('work_order', 'description')
    admin_search_fields = ('work_order', 'description')
    admin_raw_id_fields = ('work_order', )

    class Meta:
        db_table = "maid_request"


class TechnicianRequest(models.Model):
    work_order = models.OneToOneField(WorkOrder, on_delete=models.CASCADE, primary_key=True)
    DEFECT_CHOICES = (
        ('Electricity', 'Electricity'),
        ('Air Con', 'Air Con'),
        ('Plumbing', 'Plumbing'),
        ('Internet', 'Internet'),
    )
    defect_type = models.CharField(max_length=50, choices=DEFECT_CHOICES)

    admin_list_display = ('work_order', 'defect_type')
    admin_search_fields = ('work_order', 'defect_type')
    admin_raw_id_fields = ('work_order', )

    class Meta:
        db_table = "technician_request"


class AmenityRequest(models.Model):
    work_order = models.OneToOneField(WorkOrder, on_delete=models.CASCADE, primary_key=True)
    amenity_type = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()

    admin_list_display = ('work_order', 'amenity_type', 'quantity')
    admin_search_fields = ('work_order', 'amenity_type', 'quantity')
    admin_raw_id_fields = ('work_order', )

    class Meta:
        db_table = "amenity_request"
