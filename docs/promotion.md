# Spike Promotion

Use this process to promote a spike into an approved example video.

1. Confirm the spike has a complete `scene_plan.md`, `research.md` when factual claims are present, and working `scene.py`.
2. Render a preview and check runtime, text overlap, missing assets, pacing, and transitions.
3. Move the folder from `videos/spikes/<slug>/` to `videos/examples/<slug>/`.
4. Review local helpers in the approved video. Extract only reusable, stable, general-purpose code into `components/`.
5. Update the approved video's imports to use `components/`.
6. Update `components/README.md` when a new reusable category or convention is introduced.
7. Keep spike-only experiments out of `components/` and out of new videos.

Promotion approves the video source. It does not automatically approve every local helper as reusable.
