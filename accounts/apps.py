from django.apps import AppConfig
import sys
import os


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        from django.db.models.signals import post_migrate

        def sync_site_domain(sender, **kwargs):
            try:
                from django.contrib.sites.models import Site
                from django.conf import settings
                render_host = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
                is_prod = render_host or not settings.DEBUG
                target_domain = render_host or ('pnk-shop-5zfw.onrender.com' if is_prod else '127.0.0.1:8000')

                site, _ = Site.objects.get_or_create(id=settings.SITE_ID)
                if site.domain != target_domain:
                    site.domain = target_domain
                    site.name = 'PNK SHOP'
                    site.save()
            except Exception:
                pass

        post_migrate.connect(sync_site_domain, sender=self)