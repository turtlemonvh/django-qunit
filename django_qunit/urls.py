from django.conf.urls import patterns, url
from views import run_tests

urlpatterns = patterns(
    '',
    url('^(?P<path>.*)$', run_tests,
        name='qunit_test_overview'),
)
