from mgraph_ai_service_billing.core.fast_api.Billing__Fast_API import Billing__Fast_API

with Billing__Fast_API() as _:
    _.setup()
    handler = _.handler()
    app     = _.app()

def run(event, context=None):
    return handler(event, context)