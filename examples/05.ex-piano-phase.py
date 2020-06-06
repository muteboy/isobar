#!/usr/bin/env python3

#------------------------------------------------------------------------
# isobar: ex-piano-phase
# 
# Implementation of Steve Reich's "Piano Phase" (1967):
# Two identical piano lines, one with a slightly longer duration,
# moving in and out of phase with one another.
#------------------------------------------------------------------------

import isobar as iso

import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")

#------------------------------------------------------------------------
# Melody line
#------------------------------------------------------------------------
seq = iso.PSequence([-7, -5, 0, 2, 3, -5, -7, 2, 0, -5, 3, 2])

#------------------------------------------------------------------------
# Create a timeline at 160BPM
#------------------------------------------------------------------------
timeline = iso.Timeline(160)

#------------------------------------------------------------------------
# Schedule two identical melodies.
# We must copy the note sequence or else the position will be stepped
# by two every note... try removing the .copy() and see what happens!
#------------------------------------------------------------------------
timeline.schedule({
    iso.EVENT_NOTE: seq.copy() + 60,
    iso.EVENT_DURATION: 0.5
})
timeline.schedule({
    iso.EVENT_NOTE: seq.copy() + 72,
    iso.EVENT_DURATION: 0.5 * 1.01
})

#------------------------------------------------------------------------
# Start playing via default MIDI out, and block forever.
# Alternatively, use timeline.background() to retain foreground control.
#------------------------------------------------------------------------
timeline.run()