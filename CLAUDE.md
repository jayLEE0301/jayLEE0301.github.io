# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static personal portfolio website for Seungjae (Jay) Lee, hosted on GitHub Pages at sjlee.cc. The site showcases academic research, publications, and credentials.

## Technology Stack

- **Pure HTML/CSS** - No build system, framework, or package manager
- **Styling**: Custom CSS with Google Fonts (Lato)
- **Analytics**: Google Analytics (G-MBNHLWD0TG) and Google Tag Manager
- **Sub-pages**: Use Bulma CSS framework via CDN

## Development

No build commands exist. Edit HTML/CSS files directly and push to deploy via GitHub Pages.

To test locally, serve the directory with any static file server:
```bash
python3 -m http.server 8000
```

## Architecture

```
index.html          # Main portfolio page (single-page layout)
stylesheet.css      # Global styles for main page
images/             # Profile photos, logos, project demos
data/               # PDF resume
vq-bet/             # VQ-BeT research project sub-site
why-web-ai-agent/   # Web AI Agent research project sub-site
```

### Sub-page Structure

Project sub-pages (vq-bet/, why-web-ai-agent/) follow a consistent pattern:
- `index.html` - Main project page
- `resources/` - Project-specific images and videos
- `static/css/` and `static/js/` - Page-specific styling and scripts
- Uses Bulma CSS framework (loaded from CDN)

## Design Attribution

Based on Dr. Jon Barron's website template (https://jonbarron.info/).
