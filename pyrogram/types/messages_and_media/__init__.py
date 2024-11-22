#  PyroFork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
#  This file is part of PyroFork.
#
#  PyroFork is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  PyroFork is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with PyroFork.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import annotations

from .animation import Animation
from .audio import Audio
from .available_effect import AvailableEffect
from .chat_theme import ChatTheme
from .chat_wallpaper import ChatWallpaper
from .contact import Contact
from .contact_registered import ContactRegistered
from .dice import Dice
from .document import Document
from .exported_story_link import ExportedStoryLink
from .game import Game
from .giveaway import Giveaway
from .giveaway_launched import GiveawayLaunched
from .giveaway_result import GiveawayResult
from .location import Location
from .media_area import MediaArea
from .media_area_channel_post import MediaAreaChannelPost
from .media_area_coordinates import MediaAreaCoordinates
from .message import Message
from .message_entity import MessageEntity
from .message_reaction_count_updated import MessageReactionCountUpdated
from .message_reaction_updated import MessageReactionUpdated
from .message_reactions import MessageReactions
from .message_reactor import MessageReactor
from .message_story import MessageStory
from .photo import Photo
from .poll import Poll
from .poll_option import PollOption
from .reaction import Reaction
from .read_participant import ReadParticipant
from .screenshot_taken import ScreenshotTaken
from .sticker import Sticker
from .stickerset import StickerSet
from .stories_privacy_rules import StoriesPrivacyRules
from .story import Story
from .story_deleted import StoryDeleted
from .story_forward_header import StoryForwardHeader
from .story_skipped import StorySkipped
from .story_views import StoryViews
from .stripped_thumbnail import StrippedThumbnail
from .thumbnail import Thumbnail
from .translated_text import TranslatedText
from .venue import Venue
from .video import Video
from .video_note import VideoNote
from .voice import Voice
from .wallpaper import Wallpaper
from .wallpaper_settings import WallpaperSettings
from .web_app_data import WebAppData
from .web_page import WebPage
from .web_page_empty import WebPageEmpty
from .web_page_preview import WebPagePreview

__all__ = [
    "Animation",
    "Audio",
    "AvailableEffect",
    "ChatTheme",
    "ChatWallpaper",
    "Contact",
    "ContactRegistered",
    "Dice",
    "Document",
    "ExportedStoryLink",
    "Game",
    "Giveaway",
    "GiveawayLaunched",
    "GiveawayResult",
    "Location",
    "MediaArea",
    "MediaAreaChannelPost",
    "MediaAreaCoordinates",
    "Message",
    "MessageEntity",
    "MessageReactionCountUpdated",
    "MessageReactionUpdated",
    "MessageReactions",
    "MessageReactor",
    "MessageStory",
    "Photo",
    "Poll",
    "PollOption",
    "Reaction",
    "ReadParticipant",
    "ScreenshotTaken",
    "Sticker",
    "StickerSet",
    "StoriesPrivacyRules",
    "Story",
    "StoryDeleted",
    "StoryForwardHeader",
    "StorySkipped",
    "StoryViews",
    "StrippedThumbnail",
    "Thumbnail",
    "TranslatedText",
    "Venue",
    "Video",
    "VideoNote",
    "Voice",
    "Wallpaper",
    "WallpaperSettings",
    "WebAppData",
    "WebPage",
    "WebPageEmpty",
    "WebPagePreview",
]
