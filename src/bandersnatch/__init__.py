#!/usr/bin/env python3
from typing import NamedTuple


class _VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int

    @property
    def version_str(self) -> str:
        release_level = f".{self.releaselevel}" if self.releaselevel else ""
        return f"{self.major}.{self.minor}.{self.micro}{release_level}"


__version_info__ = _VersionInfo(
    major=3,
    minor=0,
    micro=0,
    releaselevel="dev0",
    serial=0,  # Not currently in use with Bandersnatch versioning
)
__version__ = __version_info__.version_str
