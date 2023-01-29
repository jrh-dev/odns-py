from pydantic import BaseModel

class AllPackages(BaseModel):
    
    id: str
    name: str

class AllResources(BaseModel):
    id: str
    name: str

