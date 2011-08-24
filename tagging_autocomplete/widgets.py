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
        # Heavily inspired by LAB.js' small loader
        # https://gist.github.com/603980
        # Check if window.jQuery or window.django.jQuery exists,
        # otherwise load jQuery from Google :-)
        js = u'''(function(global, oDOC) {
            function runCode() {
                if (!jQuery) {
                    setTimeout(arguments.callee, 25);
                    return;
                }
                jQuery().ready(function() {
                    jQuery("#%s").autocomplete("%s", { multiple: true });
                });
            };

            var jQuery = (global.django) ? global.django.jQuery : undefined || global.jQuery;
            if (!jQuery) {
                var head = oDOC.head || oDOC.getElementsByTagName("head");

                setTimeout(function () {
                    if ("item" in head) {
                        if (!head[0]) {
                            setTimeout(arguments.callee, 25);
                            return;
                        }
                        head = head[0];
                    }
                    var scriptElem = oDOC.createElement("script"),
                        scriptdone = false;
                    scriptElem.onload = scriptElem.onreadystatechange = function () {
                        if ((scriptElem.readyState && scriptElem.readyState !== "complete" && scriptElem.readyState !== "loaded") || scriptdone) {
                            return false;
                        }
                        scriptElem.onload = scriptElem.onreadystatechange = null;
                        scriptdone = true;
                        jQuery = global.jQuery;
                    };
                    scriptElem.src = "http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js";
                    head.insertBefore(scriptElem, head.firstChild);
                }, 0);

                if (oDOC.readyState == null && oDOC.addEventListener) {
                    oDOC.readyState = "loading";
                    oDOC.addEventListener("DOMContentLoaded", handler = function () {
                        oDOC.removeEventListener("DOMContentLoaded", handler, false);
                        oDOC.readyState = "complete";
                    }, false);
                }
            };
            runCode();
        })(window, document);''' % (attrs['id'], list_view)
        return mark_safe("\n".join([html, js]))

    class Media:
        css = {'all': '%s/jquery.autocomplete.css' % JS_BASE_URL, }
        js = (
            '%s/jquery.autocomplete.js' % JS_BASE_URL,
        )
