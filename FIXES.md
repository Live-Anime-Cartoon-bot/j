# Recording fixes

- `/rec` and `/drec` skip the remote channel playlist lookup for direct URLs.
- Recording setup survives a failed Python stream probe and lets FFmpeg try the
  URL with the supplied headers.
- `/drec` and `/reclink` reject invalid or zero-length durations before a job
  starts.
- `/reclink` passes captured User-Agent, Cookie, Referer, and Origin headers
  into the recorder and falls back to a plain HLS probe when Chromium is not
  available.
- Anonymous Admin is treated as an owner-like actor for `/download` as well
  as recording commands.
- `/start` now includes a working Download help button.

The release archive intentionally omits Telegram session files and uploaded
cookie files from the supplied snapshot. Put those back only through the
deployment's own runtime configuration and secret storage.