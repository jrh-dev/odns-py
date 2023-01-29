from pydantic import BaseModel

class AllPackages(BaseModel):
    id: str
    name: str