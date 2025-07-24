from osbot_fast_api.api.Fast_API import Fast_API
from mangum                      import Mangum

from mgraph_ai_service_billing.core.fast_api.routes.Routes__Info import Routes__Info


class Billing__Fast_API(Fast_API):
    enable_cors    : bool = True
    enable_api_key : bool = False
    default_routes : bool = False

    def handler(self):
        handler = Mangum(self.app())
        return handler

    def setup_routes(self):
        self.add_routes(Routes__Info)