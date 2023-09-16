# Disable autoconfig
config.load_autoconfig(False)

# Cookies
config.set('content.cookies.accept', 'no-3rdparty', 'chrome-devtools://*')
config.set('content.cookies.accept', 'no-3rdparty', 'devtools://*')

# Random shit lolol
config.set('content.headers.accept_language', '', 'https://matchmaker.krunker.io/*')

# User agent
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0', 'https://accounts.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# Load images automatically in web pages.
config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')

# Dark mode
config.set('colors.webpage.darkmode.enabled', True)

# Disable Autoplay
config.set('content.autoplay', False)

# Adblock method
config.set('content.blocking.method', 'both')

# Privacy stuff
config.set('content.canvas_reading', False)
config.set('content.desktop_capture', False)
config.set('content.geolocation', False)
config.set('content.headers.referer', 'never')
config.set('content.media.audio_capture', False)
config.set('content.media.audio_video_capture', False)
config.set('content.media.video_capture', False)
config.set('content.mouse_lock', False)
config.set('content.notifications.enabled', False)
config.set('content.tls.certificate_errors', 'ask-block-thirdparty')
config.set('content.webgl', False)
config.set('content.webrtc_ip_handling_policy', 'disable-non-proxied-udp')

# Startpage
config.set('url.start_pages', 'qute://start')

# Search engine
config.set('url.searchengines', {"DEFAULT": "https://search.demoniak.ch/search?q={}"})

# Bindings
config.bind('M', 'hint links spawn mpv {hint-url}')
config.bind('Z', 'hint links spawn st -e youtube-dl {hint-url}')