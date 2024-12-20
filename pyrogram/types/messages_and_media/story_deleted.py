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

import pyrogram
from pyrogram import raw, types
from pyrogram.types.object import Object
from pyrogram.types.update import Update


class StoryDeleted(Object, Update):
    """A deleted story.

    Parameters:
        id (``int``):
            Unique story identifier.

        from_user (:obj:`~pyrogram.types.User`, *optional*):
            Sender of the story.

        sender_chat (:obj:`~pyrogram.types.Chat`, *optional*):
            Sender of the story. If the story is from channel.
    """

    def __init__(
        self,
        *,
        client: pyrogram.Client = None,
        id: int,
        from_user: types.User = None,
        sender_chat: types.Chat = None,
    ):
        super().__init__(client)

        self.id = id
        self.from_user = from_user
        self.sender_chat = sender_chat

    async def _parse(
        self: pyrogram.Client,
        stories: raw.base.StoryItem,
        peer: raw.types.PeerChannel | raw.types.PeerUser,
    ) -> StoryDeleted:
        from_user = None
        sender_chat = None
        if isinstance(peer, raw.types.PeerChannel):
            sender_chat = await self.get_chat(peer.channel_id)
        elif isinstance(peer, raw.types.InputPeerSelf):
            from_user = self.me
        else:
            from_user = await self.get_users(peer.user_id)

        return StoryDeleted(
            id=stories.id, from_user=from_user, sender_chat=sender_chat, client=self
        )
