#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
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

from typing import TYPE_CHECKING

import pyrogram
from pyrogram import raw, types, utils
from pyrogram.types.object import Object

if TYPE_CHECKING:
    from datetime import datetime


class ChatJoiner(Object):
    """Contains information about a joiner member of a chat.

    Parameters:
        user (:obj:`~pyrogram.types.User`):
            Information about the user.

        date (:py:obj:`~datetime.datetime`):
            Date when the user joined.

        bio (``str``, *optional*):
            Bio of the user.

        pending (``bool``, *optional*):
            True in case the chat joiner has a pending request.

        approved_by (:obj:`~pyrogram.types.User`, *optional*):
            Administrator who approved this chat joiner.
    """

    def __init__(
        self,
        *,
        client: pyrogram.Client,
        user: types.User,
        date: datetime | None = None,
        bio: str | None = None,
        pending: bool | None = None,
        approved_by: types.User = None,
    ):
        super().__init__(client)

        self.user = user
        self.date = date
        self.bio = bio
        self.pending = pending
        self.approved_by = approved_by

    @staticmethod
    def _parse(
        client: pyrogram.Client,
        joiner: raw.base.ChatInviteImporter,
        users: dict[int, raw.base.User],
    ) -> ChatJoiner:
        return ChatJoiner(
            user=types.User._parse(client, users[joiner.user_id]),
            date=utils.timestamp_to_datetime(joiner.date),
            pending=joiner.requested,
            bio=joiner.about,
            approved_by=(
                types.User._parse(client, users[joiner.approved_by])
                if joiner.approved_by
                else None
            ),
            client=client,
        )
