from django.apps import AppConfig

class SchoolsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'schools'
    
    # NE PAS IMPORTER LES MODÈLES ICI - SUPPRIMEZ TOUTE IMPORTATION