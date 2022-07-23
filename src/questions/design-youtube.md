# Design Youtube

## Features

- Upload/Watch a video
- On Web/Mobile/TV
- 5M DAU
- 30 minutes/user/day
- Encryption required
- 1GB maximum video size

- How available should we be? Very.
- Does it matter how consistent we are? Not as much.

- Video uploading
  could take a while (back in 2007, you'd make a video and leave your
  computer on overnight to upload it). Should we handle chunking and
  checkpoints for videos?
- What sort of user features should we consider to make it less
  bandwidth extensive? Use webp/webm (since they compress well). Also
  brotli if supported for metadata, although this is small.

## Back of the Envelope Calculations

- Users watch 5 videos per day.
- 1% of users upload 1 video per day.
- Average video takes 300MB of space.
- Daily storage needed, 15TB.
- CDN cost is about 2c/GB month, so this costs us 15k a day.
- Over the cost of 5 years, 15TB \* 1500 is about 25 PB.
- With this all in S3, this would cost 2c/GB month, or $500k per month.

- If you put half of videos in Glacier, this would cost closer to ~300k
  per month, since they aren't watched often.

## Statistics

- Only half of all videos are ever watched once. Do we need to preprocess
  each video? If we receive 100 views on it, we can process it to 240p,
  360p, 480p, 720p, and 1080p, otherwise, we can keep the original
  quality video + render a 720p version of it.

## Design

- We need a storage solution (S3) to handle data
- A load balancer, with API servers in front of a metadata cache (for
  video data)
- A metadata cache and DB, as well as a DAG processing queue, where
  transcoding servers can work on separate parts of the video queue
  (tagging data with ML, compressing video into different formats,
  splitting audio and video, adding subtitles with ML, etc). The
  completion handler will take jobs from the queue and put it in the
  metadata DB. This will point to the transcoded files in the CDN.
