#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
#  This file is part of Pyrofork.
#
#  Pyrofork is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrofork is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrofork.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import annotations

from pyrogram import raw
from pyrogram.types.object import Object


class MediaAreaCoordinates(Object):
    """A coordinates of media area.

    Parameters:
        x (``float``, *optional*):
            X position of media area.

        y (``float``, *optional*):
            Y position of media area.

        width (``float``, *optional*):
            Media area width.

        height (``float``, *optional*):
            Media area height.

        rotation (``float``, *optional*):
            Media area rotation.
    """

    def __init__(
        self,
        x: float | None = None,
        y: float | None = None,
        width: float | None = None,
        height: float | None = None,
        rotation: float | None = None,
    ):
        super().__init__()

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotation = rotation

    def _parse(self: raw.types.MediaAreaCoordinates) -> MediaAreaCoordinates:
        return MediaAreaCoordinates(
            x=self.x, y=self.y, width=self.w, height=self.h, rotation=self.rotation
        )

    def write(self):
        return raw.types.MediaAreaCoordinates(
            x=self.x or 51.596797943115,  # value from official android apps
            y=self.y or 51.580257415771,  # value from official android apps
            w=self.width or 69.867012023926,  # value from official android apps
            h=self.height or 75.783416748047,  # value from official android apps
            rotation=self.rotation or 0.0,  # value from official android apps
        ).write()
