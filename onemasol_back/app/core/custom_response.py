from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from datetime import datetime

class CustomJSONResponse(JSONResponse):
    def render(self, content: any) -> bytes:
        def format_datetime(obj):
            if isinstance(obj, datetime):
                return obj.strftime('%Y-%m-%d %H:%M:%S')
            return obj

        encoded = jsonable_encoder(
            content,
            custom_encoder={datetime: format_datetime}
        )
        return super().render(encoded)
