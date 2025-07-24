from unittest                                                    import TestCase
from fastapi                                                     import FastAPI
from osbot_local_stack.local_stack.Local_Stack                   import Local_Stack
from starlette.testclient                                        import TestClient
from mgraph_ai_service_billing.core.fast_api.Billing__Fast_API   import Billing__Fast_API
from mgraph_ai_service_billing.core.fast_api.routes.Routes__Info import ROUTES_PATHS__INFO
from mgraph_ai_service_billing.utils.testing.skip_tests          import skip__if_not__in_github_actions
from testing.billing__objs_for_tests                             import setup__billing_test_api, Billing__Test_APIs


class test_Billing__Fast_API(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.billing_test_apis = setup__billing_test_api()
        cls.fast_api          = cls.billing_test_apis.fast_api
        cls.client            = cls.billing_test_apis.fast_api__client

    def test__init__(self):
        with self.billing_test_apis as _:
            assert type(_) is Billing__Test_APIs
            assert type(_.fast_api        ) is Billing__Fast_API
            assert type(_.fast_api__app   ) is FastAPI
            assert type(_.fast_api__client) is TestClient
            assert type(_.local_stack     ) is Local_Stack
            assert self.fast_api            == _.fast_api
            assert self.client              == _.fast_api__client

    def test__client__root_path(self):
        assert self.client.get('/').status_code == 404
        # the ones below don't work if when default_routes is set to False
        # response__no_redirects  = self.client.get('/', follow_redirects=False)
        # response__with_redirect = self.client.get('/')
        #
        # assert response__no_redirects.status_code    == 307
        # assert response__no_redirects.text           == ''
        #
        # assert response__with_redirect.status_code   == 200
        # assert '<title>FastAPI - Swagger UI</title>' in response__with_redirect.text

    def test__check_if_local_stack_is_setup(self):
        skip__if_not__in_github_actions()
        with self.billing_test_apis.local_stack as _:
            assert _.is_local_stack_configured_and_available() is True


    def test__config_fast_api_routes(self):
        assert self.fast_api.routes_paths() == ROUTES_PATHS__INFO

