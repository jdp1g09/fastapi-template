from pydantic import BaseModel
from typing import Optional

class MyModel(BaseModel):
  id: str
  name: str
  optional_field: Optional[str] = None