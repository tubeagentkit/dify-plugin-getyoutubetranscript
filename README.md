# GetYouTubeTranscript

**Author:** tubeagentkit
**Version:** 0.0.1
**Type:** tool
**Source:** https://github.com/tubeagentkit/dify-plugin-getyoutubetranscript

Get YouTube video transcripts (optionally with per-line timestamps), search YouTube, and list a channel's videos, using the [GetYouTubeTranscript](https://getyoutubetranscript.com) API.

## Tools

| Tool | What it does |
| --- | --- |
| Get Transcript | Transcript text of a video by URL or ID, plus title and channel. Turn on **Include Timestamps** to also get one `{start, duration, text}` segment per caption line, in seconds. |
| Search YouTube | Videos or channels for a query. Pass the returned `continuation_token` as **Page Token** for the next page. |
| List Channel Videos | A channel's videos (by @handle, channel URL, or channel ID), newest first. Pass the returned `continuation_token` as **Continuation Token** for the next page. |

## Setup

1. Sign up at https://getyoutubetranscript.com. New accounts include free credits.
2. Create an API key in the dashboard: https://getyoutubetranscript.com/dashboard
3. In Dify, open **Tools**, find **GetYouTubeTranscript**, click **Authorize**, and paste the API key. The key is checked against the free `/credits` endpoint.

## Usage

Add any of the tools to a workflow or an agent. Examples:

- Summarize a video: **Get Transcript** with the video URL, then an LLM node on the transcript text.
- Research a topic: **Search YouTube**, then **Get Transcript** for the top results.
- Process a channel: **List Channel Videos**, then **Get Transcript** for each video.

## Requirements

- A GetYouTubeTranscript API key. Each transcript request uses credits; `/credits` checks are free.
- Outbound HTTPS access to `getyoutubetranscript.com`.

API reference: https://getyoutubetranscript.com/docs

## Privacy

See [PRIVACY.md](PRIVACY.md).
