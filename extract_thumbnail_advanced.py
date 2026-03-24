#!/usr/bin/env python3
"""
Advanced Instagram Thumbnail Extractor
Uses requests to fetch metadata and extract thumbnail
"""

import requests
import json
import re
from urllib.parse import urlparse, parse_qs
import os
from pathlib import Path

def extract_reel_id_from_url(url):
    """Extract reel ID from Instagram URL"""
    # Handle different URL formats for Instagram posts and reels
    patterns = [
        r'/reels/([a-zA-Z0-9_-]+)/',  # Reel format: /reels/ID/
        r'/p/([a-zA-Z0-9_-]+)/',      # Post format: /p/ID/
        r'reel/([a-zA-Z0-9_-]+)'      # Alternative reel format
    ]
    
    # Try each pattern to extract the ID
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None

def get_thumbnail_via_embed(url):
    """Get thumbnail using Instagram's embed API"""
    try:
        # Construct embed URL for the reel/post
        embed_url = f"https://www.instagram.com/p/{extract_reel_id_from_url(url)}/embed/"
        
        # Request embed page with browser user agent to avoid blocking
        response = requests.get(embed_url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
        if response.status_code == 200:
            # Extract thumbnail URL from embed HTML using regex
            thumbnail_match = re.search(r'"thumbnail_url":"([^"]+)"', response.text)
            if thumbnail_match:
                # Clean up escaped slashes in the URL
                thumbnail_url = thumbnail_match.group(1).replace('\\/', '/')
                return thumbnail_url
    
    except Exception as e:
        print(f"Embed method failed: {e}")
    
    return None

def get_thumbnail_via_graphql(url):
    """Get thumbnail using GraphQL endpoint (more reliable)"""
    try:
        reel_id = extract_reel_id_from_url(url)
        if not reel_id:
            return None
        
        # GraphQL query for reel data
        query = """
        query reelQuery($reelId: String!) {
            reelMedia(id: $reelId) {
                thumbnailUrl
                displayUrl
                title
            }
        }
        """
        
        # Note: This requires authentication headers from Instagram session
        # This is more complex and may not work without proper cookies
        
    except Exception as e:
        print(f"GraphQL method failed: {e}")
    
    return None

def download_thumbnail(url, output_path):
    """Download thumbnail image from URL"""
    try:
        # Download image with proper headers to avoid blocking
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Referer': 'https://www.instagram.com/'  # Important for Instagram requests
        })
        
        if response.status_code == 200:
            # Write image data to file
            with open(output_path, 'wb') as f:
                f.write(response.content)
            return True
        else:
            print(f"Failed to download: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"Download error: {e}")
        return False

def main():
    # Handle command line arguments
    if len(sys.argv) < 2:
        print("Usage: python extract_thumbnail_advanced.py <reel_url> [output_filename]")
        sys.exit(1)
    
    reel_url = sys.argv[1]
    output_filename = sys.argv[2] if len(sys.argv) > 2 else "reel_thumbnail.jpg"
    
    print(f"🔍 Extracting thumbnail from: {reel_url}")
    
    # Try embed method first (most reliable)
    thumbnail_url = get_thumbnail_via_embed(reel_url)
    
    if thumbnail_url:
        print(f"📸 Found thumbnail URL: {thumbnail_url}")
        
        # Download the thumbnail image
        if download_thumbnail(thumbnail_url, output_filename):
            print(f"✅ Thumbnail saved as: {output_filename}")
        else:
            print("❌ Failed to download thumbnail")
    else:
        print("❌ Could not find thumbnail URL")
        print("💡 Try the yt-dlp method instead")

if __name__ == "__main__":
    import sys
    main()
