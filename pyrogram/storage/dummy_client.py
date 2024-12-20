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

from typing import TYPE_CHECKING, Any, Union

from pymongo.read_preferences import (
    Nearest,
    Primary,
    PrimaryPreferred,
    Secondary,
    SecondaryPreferred,
)

if TYPE_CHECKING:
    from bson.codec_options import CodecOptions
    from pymongo.client_session import TransactionOptions
    from pymongo.read_concern import ReadConcern
    from pymongo.write_concern import WriteConcern

try:
    from typing import Protocol, runtime_checkable
except ImportError:
    from typing_extensions import Protocol, runtime_checkable

ReadPreferences = Union[
    Primary, PrimaryPreferred, Secondary, SecondaryPreferred, Nearest
]


@runtime_checkable
class DummyMongoClient(Protocol):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError

    def get_database(
        self,
        name: str | None = None,
        *,
        codec_options: CodecOptions | None = None,
        read_preference: ReadPreferences | None = None,
        write_concern: WriteConcern | None = None,
        read_concern: ReadConcern | None = None,
    ):
        raise NotImplementedError

    async def start_session(
        self,
        *,
        causal_consistency: bool | None = None,
        default_transaction_options: TransactionOptions | None = None,
        snapshot: bool = False,
    ):
        raise NotImplementedError
