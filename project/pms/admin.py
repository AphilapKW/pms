from django.contrib import admin

# Register your models here.

from django.apps import apps

# Register your models here.


app = apps.get_app_config('pms')

for model_name, model in app.models.items():
    model_admin = type(model_name + "Admin", (admin.ModelAdmin,), {})
    model_admin.list_display = (
        model.admin_list_display if hasattr(model, 'admin_list_display') else tuple([field.name for field in model._meta.fields])
    )
    model_admin.list_filter = model.admin_list_filter if hasattr(model, 'admin_list_filter') else ()
    model_admin.list_display_links = model.admin_list_display_links if hasattr(model, 'admin_list_display_links') else ()
    model_admin.list_editable = model.admin_list_editable if hasattr(model, 'admin_list_editable') else ()
    model_admin.search_fields = model.admin_search_fields if hasattr(model, 'admin_search_fields') else ()
    model_admin.raw_id_fields = model.admin_raw_id_fields if hasattr(model, 'admin_raw_id_fields') else ()
    model_admin.get_queryset = model.admin_get_queryset if hasattr(model, 'admin_get_queryset') else model_admin.get_queryset

    admin.site.register(model, model_admin)
