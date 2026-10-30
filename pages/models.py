from wagtail.models import Page
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
# register snippet: transforme le modèle Django classique en snippet wagtail


class CoachPage(Page):
    photo = models.ForeignKey(
        "wagtailimages.Image", #pointer vers la biblio d'images wagtail
        null=True,
        blank=True,
        on_delete=models.SET_NULL,  #si l'img est supprimée, le champ redevient vide
        related_name="+"
    )

    content_panels = Page.content_panels + [
        FieldPanel("photo")
    ]

@register_snippet   #je déclare mon DECORATEUR snippet
class Cours(models.Model): # dit à wagtail que ce model doit apparaitre dans l'admon et ettre administrable avec form
    #défini le contenu de mon model (moule=template)
    nom = models.CharField(max_length=100)
    horaire = models.CharField(max_length=100, blank=True)
    niveaux = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)

    panels = [
        FieldPanel("nom"),
        FieldPanel("horaire"),
        FieldPanel("niveaux"),
        FieldPanel("description")
        #liste les champs visible dans le dorm admin de CD snippet
        #panels et pas content_panels parce qu'un snippet n'est pas une ilage, ca exclu donc le slug, le btn publier etc ...
    ]
    #donne la valeur dans la variable "nom", aux snippets qu'on va créer:
    def __str__(self):
        return self.nom


class CoursPage(Page):
    def get_context(self, request):
        #get context permet de construire les données envoyées à cette âge
        context = super().get_context(request)
        context["cours_list"] = Cours.objects.all()
        return context  #renvois le dictionnaire complet




class ContactPage(Page):
    pass
