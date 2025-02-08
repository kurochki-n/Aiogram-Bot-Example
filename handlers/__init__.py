from aiogram import Router

from .user_router import router as user_router
from .admin_router import router as admin_router
from middlewares.check_is_admin import CheckIsAdminMiddleware
from middlewares.check_sub import CheckSubscriptionMiddleware


def setup_routers() -> Router:
    router = Router()
    
    admin_router.message.middleware.register(CheckIsAdminMiddleware())
    user_router.message.middleware.register(CheckSubscriptionMiddleware())
    
    router.include_routers(admin_router, user_router)
    
    return router
