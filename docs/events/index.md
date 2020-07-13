# Events

Events are scheduled by passing a dict to `Timeline.schedule()`, which inspects the keys to figure out what type of event you are intending.

- Event dicts with a `note` or `degree` key are assumed to be `note` events
- Event dicts with a `control` or `program_change` key are assumed to be `control` events
- Event dicts with an `action` key is assumed to be an `action` event

## Event types

- [Note events](note.md) trigger discrete MIDI notes, with a duration and amplitude 
- [Control events](control.md) include MIDI control change, program change and pitchwheel messages, and can apply quasi-continuous control curves
- [Action events](control.md) call arbitrary Python functions