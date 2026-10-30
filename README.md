# Pocket

**Feel and timing analysis for contemporary pianists.**

Most piano apps check whether you hit the right notes. Pocket checks *how* you played them: whether you sit in the pocket, rush or drag, swing, and shape your dynamics. It works from plain audio, so an acoustic piano recorded on a phone is enough. No MIDI keyboard is needed.

It also analyses **reference tracks**. Give it a song you want to learn, and Pocket separates the piano or keys part, measures its feel, and compares it with your own take.

## What it measures

**Your playing**
- **Timing feel:** how early or late each note lands against the beat, in milliseconds, and how consistent that is
- **Tempo stability:** drift and rushing across a take
- **Swing:** the ratio between long and short subdivisions
- **Dynamics:** the loudness of each note, overall range, and the shape of phrases
- **Notes and chords:** audio converted to MIDI for reference

**A reference track**
- Stem separation to isolate the piano or keys part
- Tempo, key and loudness (LUFS)
- An energy curve showing how the arrangement builds
- The same feel profile as above, measured on the reference's piano part

**Comparison**
- Your timing distribution next to the reference's
- Swing and dynamics compared side by side

## Planned usage

```bash
pocket analyze my_take.wav                      # feel report for your recording
pocket reference song.mp3                       # profile a reference track
pocket compare my_take.wav --ref song.mp3       # your feel against the reference
```

## Architecture

```
src/pocket/
  core/
    audio.py       load and normalise audio
    rhythm.py      beats, onsets, micro-timing, tempo drift, swing
    dynamics.py    per-note loudness and phrase shape
    notes.py       audio-to-MIDI transcription
  reference/
    separate.py    stem separation
    profile.py     tempo, key, LUFS, energy curve
  compare.py       you versus the reference
  report.py        plots and summary report
  cli.py           command-line entry point
```

Planned libraries: librosa, numpy, basic-pitch, demucs, pyloudnorm, matplotlib.

## Roadmap

- [ ] **1. Timing feel (MVP):** beat tracking, onset detection, early/late deviations, tempo drift, plot
- [ ] **2. Dynamics and notes:** per-note loudness, phrase shape, audio-to-MIDI
- [ ] **3. Reference analyser:** stem separation, tempo, key, LUFS, energy curve
- [ ] **4. Compare mode:** your feel against the reference's piano part
- [ ] **5. Interface:** a simple web UI and shareable reports
- [ ] **Later:** sustain-pedal detection, chord-voicing analysis

## Status

Early development.

## Licence

MIT
