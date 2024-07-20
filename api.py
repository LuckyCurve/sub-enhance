import fastapi

import adaptor.inbounds.manager_controller
import adaptor.inbounds.service_controller
import config.fastapi_config
import config.log

config.log.init()
app = fastapi.FastAPI()
config.fastapi_config.init(app)
app.include_router(adaptor.inbounds.service_controller.router)
app.include_router(adaptor.inbounds.manager_controller.router)


