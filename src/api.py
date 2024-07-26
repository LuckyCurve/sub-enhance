import fastapi

import src.adaptor.inbounds.manager_controller
import src.adaptor.inbounds.service_controller
import src.config.fastapi_config
import src.config.log

src.config.log.init()
app = fastapi.FastAPI()
src.config.fastapi_config.init(app)
app.include_router(src.adaptor.inbounds.service_controller.router)
app.include_router(src.adaptor.inbounds.manager_controller.router)
