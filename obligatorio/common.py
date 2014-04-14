import settings

def template_base(request):
    app_name = settings.INSTALLED_APPS[6]
    return {'template_base':'{0}/Base/base.html'.format(app_name)}
