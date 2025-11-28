from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from constants import HeightUnit, WeightUnit, TemperatureUnit, convertUnitsRequest
from constants import convert_height, convert_weight, convert_temperature

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # or your actual frontend domain
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
    allow_credentials=False
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/units")
def get_Units(type: str):
    unit_map = {
        'height': HeightUnit,
        'weight': WeightUnit,
        'temperature': TemperatureUnit
    }
    unit_enum = unit_map.get(type)
    if not unit_enum:
        raise HTTPException(status_code=400, detail="Invalid unit type")
    return [
        {"id": unit.value, "label": unit.name.capitalize() + f" ({unit.value})"}
        for unit in unit_enum
    ]


@app.post("/api/convert")
def convert_units(request: convertUnitsRequest):
    try:
        if request.type == 'height':
            result = convert_height(request.value, request.from_unit, request.to_unit)
        elif request.type == 'weight':
            result = convert_weight(request.value, request.from_unit, request.to_unit)
        elif request.type == 'temperature':
            result = convert_temperature(request.value, request.from_unit, request.to_unit)
        else:
            raise HTTPException(status_code=400, detail="Invalid conversion type")
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))