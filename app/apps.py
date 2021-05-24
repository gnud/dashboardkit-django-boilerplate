from django.apps import AppConfig
from iommi import Style, Asset
from iommi.style_bootstrap import bootstrap

bootstrap5_base = Style(
    bootstrap,
    root__assets=dict(
        css=Asset.css(),
        popper_js=Asset.js(),
        js=Asset.js(),
    ),
)


class AppConfig1(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        from iommi import register_style

        from iommi import Style

        the_style = Style(
            bootstrap5_base,
            base_template='iommi_base.html',
            query__attrs__class__foo=True,
            content_block='article'
        )

        register_style('abase', the_style)
