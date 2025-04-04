from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import extract_route
from config.settings import Settings

def create_application() -> FastAPI:
    settings = Settings()
    application = FastAPI(title=settings.APP_NAME)
    
    # Configure CORS
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include routers
    application.include_router(extract_route.router)
    
    return application

app = create_application()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)