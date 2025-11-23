#!/usr/bin/env python3
"""
GeoCam Website Builder
Generates static HTML from JSON content and templates
"""

import json
import os
import shutil
from pathlib import Path
from string import Template


class SiteBuilder:
    def __init__(self, content_dir="content", template_dir="templates", output_dir="public"):
        self.content_dir = Path(content_dir)
        self.template_dir = Path(template_dir)
        self.output_dir = Path(output_dir)

    def load_json(self, filename):
        """Load JSON content file"""
        with open(self.content_dir / filename, 'r') as f:
            return json.load(f)

    def load_template(self, filename):
        """Load HTML template"""
        with open(self.template_dir / filename, 'r') as f:
            return f.read()

    def render_navigation(self, site_data, current_page=""):
        """Render navigation menu"""
        nav_items = []
        for item in site_data['navigation']:
            active = 'active' if item['href'] == current_page else ''
            nav_items.append(f'<a href="{item["href"]}" class="nav-link {active}">{item["name"]}</a>')
        return '\n'.join(nav_items)

    def render_footer(self, site_data):
        """Render footer"""
        events_html = []
        for event in site_data['events']:
            events_html.append(f'''
                <div class="event-item">
                    <h4>{event['name']}</h4>
                    <p>{event['dates']}</p>
                    <p class="location">{event['location']}</p>
                </div>
            ''')

        events_section = '\n'.join(events_html)

        return f'''
        <footer class="footer">
            <div class="container">
                <div class="footer-grid">
                    <div class="footer-col">
                        <h3>{site_data['siteName']}</h3>
                        <p>{site_data['description']}</p>
                    </div>
                    <div class="footer-col">
                        <h3>Upcoming Events</h3>
                        <div class="events-list">
                            {events_section}
                        </div>
                    </div>
                    <div class="footer-col">
                        <h3>Stay Connected</h3>
                        <form class="newsletter-form" action="#" method="post">
                            <input type="email" placeholder="Your email" required>
                            <button type="submit">Subscribe</button>
                        </form>
                        <p class="contact-email">
                            <a href="mailto:{site_data['contact']['email']}">{site_data['contact']['email']}</a>
                        </p>
                    </div>
                </div>
                <div class="footer-bottom">
                    <p>&copy; {site_data['siteName']} 2025. All rights reserved.</p>
                </div>
            </div>
        </footer>
        '''

    def build_page(self, template_name, content_file, output_file, current_page=""):
        """Build a single page"""
        print(f"Building {output_file}...")

        # Load site-wide data
        site_data = self.load_json('site.json')

        # Load page-specific content
        page_data = self.load_json(content_file)

        # Load template
        template_content = self.load_template(template_name)

        # Render common components
        navigation = self.render_navigation(site_data, current_page)
        footer = self.render_footer(site_data)

        # Create page-specific content based on template
        if template_name == 'home.html':
            content = self.render_home(page_data)
        elif template_name == 'product.html':
            content = self.render_product(page_data)
        elif template_name == 'data.html':
            content = self.render_data(page_data)
        else:
            content = ""

        # Replace template variables
        output = template_content.replace('{{SITE_NAME}}', site_data['siteName'])
        output = output.replace('{{NAVIGATION}}', navigation)
        output = output.replace('{{CONTENT}}', content)
        output = output.replace('{{FOOTER}}', footer)

        # Write output file
        output_path = self.output_dir / output_file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(output)

    def render_home(self, data):
        """Render home page content"""
        hero = data['hero']
        workflow = data['workflow']
        deployment = data['deployment']
        industries = data['industries']

        # Workflow steps
        workflow_html = []
        for step in workflow['steps']:
            workflow_html.append(f'''
                <div class="workflow-step">
                    <div class="step-icon">{step['icon']}</div>
                    <h3>{step['title']}</h3>
                    <p>{step['description']}</p>
                </div>
            ''')

        # Deployment methods
        deployment_html = []
        for method in deployment['methods']:
            deployment_html.append(f'''
                <div class="deployment-card">
                    <h3>{method['title']}</h3>
                    <p>{method['description']}</p>
                </div>
            ''')

        # Industries
        industries_html = []
        for sector in industries['sectors']:
            industries_html.append(f'''
                <div class="industry-card">
                    <div class="industry-icon">{sector['icon']}</div>
                    <h3>{sector['title']}</h3>
                    <p>{sector['description']}</p>
                </div>
            ''')

        return f'''
        <section class="hero">
            <div class="container">
                <div class="hero-content">
                    <h1>{hero['title']}</h1>
                    <p class="hero-subtitle">{hero['subtitle']}</p>
                    <p class="hero-description">{hero['description']}</p>
                    <div class="hero-cta">
                        <a href="{hero['cta']['primary']['href']}" class="btn btn-primary">{hero['cta']['primary']['text']}</a>
                        <a href="{hero['cta']['secondary']['href']}" class="btn btn-secondary">{hero['cta']['secondary']['text']}</a>
                    </div>
                </div>
            </div>
        </section>

        <section class="workflow">
            <div class="container">
                <h2>{workflow['title']}</h2>
                <p class="section-subtitle">{workflow['subtitle']}</p>
                <div class="workflow-grid">
                    {''.join(workflow_html)}
                </div>
            </div>
        </section>

        <section class="deployment">
            <div class="container">
                <h2>{deployment['title']}</h2>
                <p class="section-subtitle">{deployment['subtitle']}</p>
                <div class="deployment-grid">
                    {''.join(deployment_html)}
                </div>
            </div>
        </section>

        <section class="industries">
            <div class="container">
                <h2>{industries['title']}</h2>
                <p class="section-subtitle">{industries['subtitle']}</p>
                <div class="industries-grid">
                    {''.join(industries_html)}
                </div>
            </div>
        </section>
        '''

    def render_product(self, data):
        """Render product page content"""
        hero = data['hero']
        hardware = data['hardware']
        vps = data['vps']
        software = data['software']

        # Hardware features
        features_html = []
        for feature in hardware['features']:
            features_html.append(f'''
                <div class="feature-card">
                    <h3>{feature['title']}</h3>
                    <p>{feature['description']}</p>
                </div>
            ''')

        # VPS capabilities
        capabilities_html = []
        for cap in vps['capabilities']:
            capabilities_html.append(f'<li>{cap}</li>')

        # Software applications
        software_html = []
        for app in software['applications']:
            features_list = ''.join([f'<li>{f}</li>' for f in app['features']])
            software_html.append(f'''
                <div class="software-card">
                    <h3>{app['name']}</h3>
                    <p>{app['description']}</p>
                    <ul class="feature-list">
                        {features_list}
                    </ul>
                </div>
            ''')

        return f'''
        <section class="page-hero">
            <div class="container">
                <h1>{hero['title']}</h1>
                <p class="page-subtitle">{hero['subtitle']}</p>
            </div>
        </section>

        <section class="hardware">
            <div class="container">
                <h2>{hardware['title']}</h2>
                <p class="section-subtitle">{hardware['subtitle']}</p>
                <div class="features-grid">
                    {''.join(features_html)}
                </div>
                <div class="deployment-info">
                    <h3>{hardware['deployment']['title']}</h3>
                    <p>{hardware['deployment']['description']}</p>
                </div>
            </div>
        </section>

        <section class="vps">
            <div class="container">
                <h2>{vps['title']}</h2>
                <p class="section-subtitle">{vps['subtitle']}</p>
                <p class="vps-description">{vps['description']}</p>
                <ul class="capabilities-list">
                    {''.join(capabilities_html)}
                </ul>
            </div>
        </section>

        <section class="software">
            <div class="container">
                <h2>{software['title']}</h2>
                <p class="section-subtitle">{software['subtitle']}</p>
                <div class="software-grid">
                    {''.join(software_html)}
                </div>
            </div>
        </section>
        '''

    def render_data(self, data):
        """Render data page content"""
        hero = data['hero']
        overview = data['overview']
        capabilities = data['capabilities']
        three_d = data['3d']
        services = data['services']
        integration = data['integration']

        # Applications
        applications_html = []
        for app in capabilities['applications']:
            applications_html.append(f'''
                <div class="application-card">
                    <div class="app-icon">{app['icon']}</div>
                    <h3>{app['title']}</h3>
                    <p>{app['description']}</p>
                </div>
            ''')

        # 3D outputs
        outputs_html = []
        for output in three_d['outputs']:
            outputs_html.append(f'''
                <div class="output-card">
                    <h3>{output['title']}</h3>
                    <p>{output['description']}</p>
                </div>
            ''')

        # Services benefits
        benefits_html = ''.join([f'<li>{b}</li>' for b in services['benefits']])

        # Integration features
        features_html = ''.join([f'<li>{f}</li>' for f in integration['features']])

        return f'''
        <section class="page-hero">
            <div class="container">
                <h1>{hero['title']}</h1>
                <p class="page-subtitle">{hero['subtitle']}</p>
            </div>
        </section>

        <section class="overview">
            <div class="container">
                <h2>{overview['title']}</h2>
                <p class="overview-description">{overview['description']}</p>
            </div>
        </section>

        <section class="capabilities">
            <div class="container">
                <h2>{capabilities['title']}</h2>
                <p class="section-subtitle">{capabilities['subtitle']}</p>
                <div class="applications-grid">
                    {''.join(applications_html)}
                </div>
            </div>
        </section>

        <section class="three-d">
            <div class="container">
                <h2>{three_d['title']}</h2>
                <p class="section-subtitle">{three_d['subtitle']}</p>
                <div class="outputs-grid">
                    {''.join(outputs_html)}
                </div>
            </div>
        </section>

        <section class="services">
            <div class="container">
                <h2>{services['title']}</h2>
                <p class="services-description">{services['description']}</p>
                <ul class="benefits-list">
                    {benefits_html}
                </ul>
            </div>
        </section>

        <section class="integration">
            <div class="container">
                <h2>{integration['title']}</h2>
                <p class="integration-description">{integration['description']}</p>
                <ul class="features-list">
                    {features_html}
                </ul>
            </div>
        </section>
        '''

    def copy_assets(self):
        """Copy CSS and other assets to output directory"""
        print("Copying assets...")
        assets_src = Path('src')
        assets_dest = self.output_dir / 'assets'

        if assets_src.exists():
            shutil.copytree(assets_src, assets_dest, dirs_exist_ok=True)

    def build(self):
        """Build the entire site"""
        print("Building GeoCam website...")

        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Build pages
        self.build_page('home.html', 'home.json', 'index.html', 'index.html')
        self.build_page('product.html', 'product.json', 'product.html', 'product.html')
        self.build_page('data.html', 'data.json', 'data.html', 'data.html')

        # Copy assets
        self.copy_assets()

        print("Build complete! Site is in the 'public' directory.")


if __name__ == '__main__':
    builder = SiteBuilder()
    builder.build()
