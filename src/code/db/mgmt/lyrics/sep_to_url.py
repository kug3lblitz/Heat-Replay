#!/usr/bin/env python

from context import *

from settings.filemgmt import fileManager
from settings.paths import sep
from settings.paths import CHARTED_FAIL, URLS_FAILED  # modify


def splitAttr(fileName):

    rawFile = fileManager(fileName, 'r')

    songs = []
    url = '{title}-lyrics-{artist}'

    songs = [
        (
            url.format(
                title=song.split(sep)[1], artist=song.split(sep)[0]
            )
        ).replace(' ', '-').partition('-featuring')[0]
        for song in rawFile.split('\n')
    ]

    return songs

if __name__ == '__main__':

    fileManager(URLS_FAILED, 'w', '\n'.join(splitAttr(CHARTED_FAIL)))
