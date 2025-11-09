# Social Media & Coding Stats Integration Guide

I've added placeholder cards for Instagram, YouTube, GitHub, and LeetCode on your blog page. Here's how to integrate real data:

## 🎨 Current Setup
- ✅ Beautiful cards with gradient backgrounds
- ✅ Icons and branding colors
- ✅ Links to your profiles
- ⏳ Placeholder data (shows "--" for now)

## 📱 Integration Options

### Option 1: Manual Update (Easiest)
Simply update the numbers manually in `templates/blog.html`:
- Edit the `--` placeholders with your actual stats
- Update weekly/monthly as needed

### Option 2: API Integration (Advanced)

#### 1. Instagram Latest Post
**Using Instagram Basic Display API:**
```python
# Requires: Instagram Business Account + Facebook Developer App
# Get Access Token from: https://developers.facebook.com/apps/

import requests

def get_instagram_latest_post(access_token):
    url = f"https://graph.instagram.com/me/media?fields=id,caption,media_url,permalink&access_token={access_token}"
    response = requests.get(url)
    data = response.json()
    return data['data'][0] if data.get('data') else None
```

**Alternative: Instagram Embed Widget**
- Use Instagram's official embed widget
- No API needed, just paste embed code

#### 2. YouTube Latest Video
**Using YouTube Data API v3:**
```python
# Get API Key from: https://console.cloud.google.com/

from googleapiclient.discovery import build

def get_youtube_latest_video(api_key, channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        order='date',
        maxResults=1
    )
    response = request.execute()
    return response['items'][0] if response.get('items') else None
```

**Alternative: RSS Feed**
- YouTube Channel RSS: `https://www.youtube.com/feeds/videos.xml?channel_id=YOUR_CHANNEL_ID`
- Parse with Python's `feedparser` library

#### 3. GitHub Activity
**Using GitHub REST API (No Auth Needed):**
```python
import requests

def get_github_stats(username):
    # Get user info
    user_url = f"https://api.github.com/users/{username}"
    user_data = requests.get(user_url).json()
    
    # Get contribution count (requires GraphQL or scraping)
    repos = user_data.get('public_repos', 0)
    
    return {
        'repos': repos,
        'followers': user_data.get('followers', 0)
    }
```

**GitHub Contribution Graph:**
- Use: https://github-readme-stats.vercel.app/api?username=mrcuriousind
- Or: https://github-readme-streak-stats.herokuapp.com/?user=mrcuriousind

#### 4. LeetCode Stats
**Using LeetCode API (Unofficial):**
```python
import requests

def get_leetcode_stats(username):
    url = "https://leetcode.com/graphql"
    query = """
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            submitStats {
                acSubmissionNum {
                    difficulty
                    count
                }
            }
            profile {
                ranking
            }
        }
    }
    """
    response = requests.post(url, json={
        'query': query,
        'variables': {'username': username}
    })
    return response.json()
```

**Alternative: LeetCode Stats Card**
- Use: https://leetcard.jacoblin.cool/mrcuriousind
- Embed as image

## 🚀 Quick Implementation (Recommended)

### Step 1: Add to app.py
```python
import requests
from datetime import datetime

@app.route('/blog')
def blog():
    blog_posts = BlogPost.query.all()
    videos = Video.query.all()
    
    # Fetch social stats (with error handling)
    social_stats = {
        'github_repos': get_github_repos('mrcuriousind'),
        'leetcode_solved': get_leetcode_stats('mrcuriousind'),
        # Add more as needed
    }
    
    return render_template('blog.html', 
                         blog_posts=blog_posts, 
                         videos=videos,
                         social_stats=social_stats)

def get_github_repos(username):
    try:
        response = requests.get(f'https://api.github.com/users/{username}')
        return response.json().get('public_repos', '--')
    except:
        return '--'

def get_leetcode_stats(username):
    # Implement LeetCode API call
    return '--'
```

### Step 2: Update templates/blog.html
Replace `--` with `{{ social_stats.github_repos }}`, etc.

## 📊 Widget Alternatives (No Coding Required)

### GitHub Stats Card
```html
<img src="https://github-readme-stats.vercel.app/api?username=mrcuriousind&show_icons=true&theme=radical" />
```

### LeetCode Stats Card
```html
<img src="https://leetcard.jacoblin.cool/mrcuriousind?theme=dark&font=Karma" />
```

### YouTube Subscribe Button
```html
<script src="https://apis.google.com/js/platform.js"></script>
<div class="g-ytsubscribe" data-channelid="YOUR_CHANNEL_ID" data-layout="default" data-count="default"></div>
```

## 🎯 My Recommendation

**For Now (Quick Win):**
1. Manually update the stats in `templates/blog.html`
2. Use GitHub/LeetCode stat cards as images
3. Embed latest YouTube video manually

**Later (Full Integration):**
1. Set up GitHub API (easiest, no auth needed)
2. Add LeetCode GraphQL integration
3. Use Instagram/YouTube embed widgets
4. Cache results to avoid rate limits

## 📝 Notes
- Most APIs have rate limits (GitHub: 60 req/hour without auth)
- Consider caching stats (update every hour/day)
- Use environment variables for API keys
- Add error handling for failed API calls

Let me know which approach you'd like to implement!
