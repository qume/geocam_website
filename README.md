# GeoCam Website

A modern, professional static website for GeoCam - the AI-Native Reality Capture Platform.

## Overview

This website is designed for easy content management without requiring command-line tools. Content is stored in JSON files, and the site automatically rebuilds when changes are pushed to GitHub.

## Architecture

- **Content**: Stored in `content/` directory as JSON files
- **Templates**: HTML templates in `templates/` directory
- **Styles**: CSS in `src/css/` directory
- **Scripts**: JavaScript in `src/js/` directory
- **Build Script**: Python script (`build.py`) generates static HTML
- **Output**: Generated site in `public/` directory

## Editing Content

### To Update Website Content:

1. **Edit JSON files** in the `content/` directory:
   - `site.json` - Site-wide settings (name, navigation, events)
   - `home.json` - Home page content
   - `product.json` - Product page content
   - `data.json` - Data & Deliverables page content

2. **Commit and push** your changes to GitHub:
   ```bash
   git add content/
   git commit -m "Update website content"
   git push
   ```

3. **Automatic rebuild**: GitHub Actions will automatically rebuild and deploy the site

### Example: Updating Events

Edit `content/site.json` and modify the `events` array:

```json
{
  "events": [
    {
      "name": "Your Event Name",
      "dates": "Month DD-DD, YYYY",
      "location": "City, State"
    }
  ]
}
```

## Manual Build (Optional)

If you need to build the site locally:

### Requirements

- Python 3.7 or higher

### Build Steps

```bash
# Run the build script
python build.py

# The generated site will be in the 'public/' directory
```

### Preview Locally

```bash
# Using Python's built-in server
cd public
python -m http.server 8000

# Visit http://localhost:8000 in your browser
```

## GitHub Pages Deployment

### Initial Setup

1. Go to your repository Settings → Pages
2. Under "Source", select "GitHub Actions"
3. The site will automatically deploy when you push changes

### Manual Deployment

You can manually trigger a rebuild:
1. Go to the "Actions" tab in your repository
2. Select "Build and Deploy Website"
3. Click "Run workflow"

## File Structure

```
geocam_website/
├── content/              # Content JSON files (EDIT THESE)
│   ├── site.json        # Site configuration
│   ├── home.json        # Home page content
│   ├── product.json     # Product page content
│   └── data.json        # Data page content
├── templates/           # HTML templates
│   ├── home.html
│   ├── product.html
│   └── data.html
├── src/                 # Source assets
│   ├── css/
│   │   └── main.css     # Main stylesheet
│   └── js/
│       └── main.js      # JavaScript functionality
├── .github/
│   └── workflows/
│       └── build-site.yml  # GitHub Actions workflow
├── build.py            # Build script
├── public/             # Generated site (auto-created)
└── README.md           # This file
```

## Design Features

- **Mobile-First**: Responsive design that works on all devices
- **Professional**: Clean, trustworthy design suitable for utilities and government
- **Accessible**: WCAG compliant with proper semantic HTML
- **Fast**: Static HTML with optimized CSS and minimal JavaScript
- **Modern**: CSS Grid and Flexbox layouts
- **Smooth Animations**: Subtle scroll animations and transitions

## Color Scheme

- **Primary Blue**: #0066cc - Trust and technology
- **Dark Blue**: #004c99 - Professional and stable
- **Secondary Blue**: #00a3e0 - Innovation and energy
- **Text**: #1a1a1a - High contrast for readability
- **Backgrounds**: #ffffff, #f8f9fa - Clean and professional

## Browser Support

- Chrome/Edge (last 2 versions)
- Firefox (last 2 versions)
- Safari (last 2 versions)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Adding Images

### Image Storage

Store images in `src/images/` directory:
```
src/
  images/
    hardware/
      geocam-360.jpg
      device-mounted.jpg
    screenshots/
      manager.png
      editor.png
    logos/
      logo.svg
```

### Using Images in Content

Reference images in your JSON files:
```json
{
  "image": "assets/images/hardware/geocam-360.jpg",
  "alt": "GeoCam 360 Camera Device"
}
```

### Optimizing Images

Before adding images:
1. Resize to appropriate dimensions (max 1920px width for full-width images)
2. Compress using tools like TinyPNG or ImageOptim
3. Use WebP format for better compression (with JPG/PNG fallbacks)

## Customization

### Adding a New Page

1. Create content file in `content/` (e.g., `about.json`)
2. Create template in `templates/` (e.g., `about.html`)
3. Add rendering method in `build.py`
4. Update navigation in `content/site.json`
5. Run build script

### Modifying Styles

Edit `src/css/main.css`. The CSS uses CSS custom properties (variables) for easy theming:

```css
:root {
    --primary-color: #0066cc;
    --text-primary: #1a1a1a;
    /* etc. */
}
```

## Support

For issues or questions:
- Check the GitHub Issues tab
- Review this README
- Contact the development team

## License

© GeoCam 2025. All rights reserved.
