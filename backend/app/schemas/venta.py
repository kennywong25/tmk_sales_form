from pydantic import BaseModel, Extra
from typing import Any, Dict

class WolkvoxEvent(BaseModel, extra=Extra.allow):
    # aquí defines campos conocidos si ya sabes algunos, 
    # o de momento registras todo en un dict:
    raw: Dict[str, Any]

class VentaBQ(BaseModel):
    client_id: str
    agent_id: str
    campaign_id: str
    timestamp: str
    # …otros campos normalizados…
