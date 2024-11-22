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

from pyrogram import raw, types
from pyrogram.types.object import Object


class RequestedChats(Object):
    """Contains information about requested chats.

    Parameters:
        button_id (``int``):
            Button identifier.

        chats (List of :obj:`~pyrogram.types.RequestedChat`, *optional*):
            List of chats.

        users (List of :obj:`~pyrogram.types.RequestedUser` *optional*):
            List of users.
    """

    def __init__(
        self,
        button_id: int,
        chats: list[types.RequestedChat] | None = None,
        users: list[types.RequestedUser] | None = None,
    ):
        super().__init__()

        self.button_id = button_id
        self.chats = chats
        self.users = users

    @staticmethod
    async def _parse(
        client,
        request: raw.types.MessageActionRequestedPeer
        | raw.types.MessageActionRequestedPeerSentMe,
    ) -> RequestedChats:
        button_id = request.button_id
        chats = []
        users = []
        for chat in request.peers:
            if isinstance(
                chat,
                raw.types.RequestedPeerChat
                | raw.types.RequestedPeerChannel
                | raw.types.PeerChat
                | raw.types.PeerChannel,
            ):
                chats.append(await types.RequestedChat._parse(client, chat))
            elif isinstance(chat, raw.types.RequestedPeerUser | raw.types.PeerUser):
                users.append(await types.RequestedUser._parse(client, chat))

        return RequestedChats(
            button_id,
            chats if len(chats) > 0 else None,
            users if len(users) > 0 else None,
        )
