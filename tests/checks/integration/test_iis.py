# 3p
from nose.plugins.attrib import attr

# project
from checks import AgentCheck
from tests.checks.common import AgentCheckTest

INSTANCE = {
    'host': '.',
}

@attr('windows')
@attr(requires='windows')
class IISTest(AgentCheckTest):
    CHECK_NAME = 'iis'

    IIS_METRICS = (
        'iis.uptime',
        # Network
        'iis.net.bytes_sent',
        'iis.net.bytes_rcvd',
        'iis.net.bytes_total',
        'iis.net.num_connections',
        'iis.net.files_sent',
        'iis.net.files_rcvd',
        'iis.net.connection_attempts',
        # HTTP Methods
        'iis.httpd_request_method.get',
        'iis.httpd_request_method.post',
        'iis.httpd_request_method.head',
        'iis.httpd_request_method.put',
        'iis.httpd_request_method.delete',
        'iis.httpd_request_method.options',
        'iis.httpd_request_method.trace',
        # Errors
        'iis.errors.not_found',
        'iis.errors.locked',
        # Users
        'iis.users.anon',
        'iis.users.nonanon',
        # Requests
        'iis.requests.cgi',
        'iis.requests.isapi',
    )

    def test_basic_check(self):
        self.run_check_twice({'instances': [INSTANCE]})

        for metric in self.IIS_METRICS:
            self.assertMetric(metric, tags=[], count=1)

        self.assertServiceCheck('iis.site_up', status=AgentCheck.OK,
                                tags=["site:{0}".format('Total')], count=1)
        self.coverage_report()
