from django.conf.urls.defaults import *

urlpatterns = patterns('tinymce',
    (r'^init/tiny_mce_init.js$', 'views.init_mce'),
    (r'^templates/([a-zA-Z0-9-_./]+)$', 'views.get_template'),
    (r'^styles.css$', 'views.get_css'),
)
