from django.forms.widgets import Input
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.safestring import mark_safe


JS_BASE_URL = getattr(settings, 'TAGGING_AUTOCOMPLETE_JS_BASE_URL',
                      '%sjquery-autocomplete' % settings.MEDIA_URL)


class TagAutocomplete(Input):
    input_type = 'text'

    def render(self, name, value, attrs=None):
        html = super(TagAutocomplete, self).render(name, value, attrs)
        list_view = reverse('tagging_autocomplete-list')
        js = u'''<script type="text/javascript">
                      jQuery().ready(function() {
                          jQuery("#%s").autocomplete("%s", { multiple: true });
                      });
                  </script>''' % (attrs['id'], list_view)
        return mark_safe("\n".join([html, js]))

    class Media:
        css = {'all': '%s/jquery.autocomplete.css' % js_base_url, }
        js = (
            '%s/lib/jquery.js' % js_base_url,
            '%s/jquery.autocomplete.js' % js_base_url,
        )
