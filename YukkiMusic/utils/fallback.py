#
# Copyright (C) 2024-2025 by TheTeamVivek@Github, < https://github.com/TheTeamVivek >.
#
# This file is part of < https://github.com/TheTeamVivek/YukkiMusic > project,
# and is released under the MIT License.
# Please see < https://github.com/TheTeamVivek/YukkiMusic/blob/master/LICENSE >
#
# All rights reserved.
#

from YukkiMusic.platforms import saavn


async def download(title, video):
    try:
        path, details = await saavn.download(title)
        return path, details, video
    except Exception as e:
        raise ValueError(f"Fallback failed: {str(e)}")
