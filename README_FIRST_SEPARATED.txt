Sagar Kerhalkar separated deployment package

This package has two independent projects.

1) 01_PROFILE_WEBSITE_ONLY_DEPLOY_TO_CLOUDFLARE_PAGES
   - Public portfolio website for sagarkerhalkar.com
   - CV page and profile/project pages
   - Local profile/CV update files: profile-editor.html and cv-editor.html
   - No monitor server code inside this folder

2) 02_SYSTEM_HEALTH_MONITOR_ONLY_RUN_ON_LOCAL_SERVER
   - Private system monitor app for monitor.sagarkerhalkar.com
   - Windows/Ubuntu client scripts, API, database and dashboard
   - No profile/CV editor in monitor settings

Connection between them: only links.
Profile project page links to https://monitor.sagarkerhalkar.com.
Monitor dashboard has only a profile website link.
No shared settings, no shared CV update, no profile API in monitor.
