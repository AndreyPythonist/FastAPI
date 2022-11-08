from typing import List

from pydantic import BaseModel


class UploadVideo(BaseModel):
    title: str
    description: int
