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

import pyrogram
from pyrogram import raw, types
from pyrogram.types.object import Object


class MessageReactions(Object):
    """Contains information about a message reactions.

    Parameters:
        reactions (List of :obj:`~pyrogram.types.Reaction`):
            Reactions list.

        top_reactors (List of :obj:`~pyrogram.types.MessageReactor`):
            Top reactors.
    """

    def __init__(
        self,
        *,
        client: pyrogram.Client = None,
        reactions: list[types.Reaction] | None = None,
        top_reactors: list[types.MessageReactor] | None = None,
    ):
        super().__init__(client)

        self.reactions = reactions
        self.top_reactors = top_reactors

    @staticmethod
    def _parse(
        client: pyrogram.Client,
        message_reactions: raw.base.MessageReactions | None = None,
        users: dict[int, raw.types.User] | None = None,
    ) -> MessageReactions | None:
        if not message_reactions:
            return None

        return MessageReactions(
            client=client,
            reactions=[
                types.Reaction._parse_count(client, reaction)
                for reaction in message_reactions.results
            ],
            top_reactors=[
                types.MessageReactor._parse(client, reactor, users)
                for reactor in message_reactions.top_reactors
            ],
        )
