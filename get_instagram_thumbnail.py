#!/usr/bin/env python3
"""
Instagram Reel Thumbnail Extractor
Usage: python get_instagram_thumbnail.py <reel_url> [output_filename]
"""

import sys
import subprocess
import os
from pathlib import Path

def install_yt_dlp():
    """Install yt-dlp if not available"""
    try:
        import yt_dlp
        return True
    except ImportError:
        # Install yt-dlp using pip when not found
        print("Installing yt-dlp...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
        return True

def extract_thumbnail(reel_url, output_filename=None):
    """Extract thumbnail from Instagram reel"""
    
    # Install yt-dlp if needed
    install_yt_dlp()
    import yt_dlp
    
    # Configure yt-dlp options for thumbnail extraction
    ydl_opts = {
        'writethumbnail': True,  # Enable thumbnail writing
        'skip_download': True,  # Don't download the video, just metadata
        'outtmpl': '%(title)s.%(ext)s',  # Output filename template
        'format': 'best',  # Best quality format
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video information without downloading
            info = ydl.extract_info(reel_url, download=False)
            
            # Generate output filename if not provided
            if output_filename is None:
                # Clean up the title for safe filename usage
                safe_title = "".join(c for c in info['title'] if c.isalnum() or c in (' ', '-', '_')).rstrip()
                output_filename = f"{safe_title}_thumbnail.jpg"
            
            # Set output template without extension
            ydl_opts['outtmpl'] = output_filename.replace('.jpg', '')
            
            # Download thumbnail only using updated options
            with yt_dlp.YoutubeDL(ydl_opts) as ydl_thumb:
                ydl_thumb.extract_info(reel_url)
            
            print(f"✅ Thumbnail saved as: {output_filename}")
            return output_filename
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    # List of pending reel URLs to process
    pending_reels = [
        # Add your Instagram reel URLs here
        # Example: "https://www.instagram.com/reels/DV8CLU9jINn/",
        # Example: "https://www.instagram.com/reels/ABC123XYZ/",
    ]
    
    # List of already processed reel URLs to skip
    done_reels = [
        # Add URLs that have already been processed here
        # Example: "https://www.instagram.com/reels/ALREADYPROCESSED123/",
    ]
    
    if not pending_reels:
        print("❌ No reels in pending_reels list. Please add URLs to the list.")
        sys.exit(1)
    
    # Filter out reels that are already done
    reels_to_process = []
    for reel_url in pending_reels:
        if reel_url in done_reels:
            print(f"⏭️  Skipping already processed: {reel_url}")
        else:
            reels_to_process.append(reel_url)
    
    if not reels_to_process:
        print("✅ All reels have already been processed!")
        sys.exit(0)
    
    print(f"📋 Processing {len(reels_to_process)} new reel(s) out of {len(pending_reels)} total...")
    
    # Process each new reel in the list
    for i, reel_url in enumerate(reels_to_process, 1):
        print(f"\n🔄 [{i}/{len(reels_to_process)}] Processing: {reel_url}")
        
        # Validate Instagram URL format
        if not reel_url.startswith('https://www.instagram.com/'):
            print(f"❌ Skipping invalid URL: {reel_url}")
            continue
        
        # Generate filename based on index or use reel-specific naming
        output_filename = f"reel_{i}_thumbnail.jpg"
        
        # Extract and save thumbnail
        result = extract_thumbnail(reel_url, output_filename)
        
        if result:
            print(f"✅ Successfully processed reel {i}")
            # Add to done_reels list after successful processing
            done_reels.append(reel_url)
        else:
            print(f"❌ Failed to process reel {i}")
    
    print(f"\n🏁 Finished processing {len(reels_to_process)} new reel(s)")
    print(f"📊 Total processed reels: {len(done_reels)}")
    
    # Optional: Print updated done_reels list for reference
    print("\n📝 Updated done_reels list (copy this to the script):")
    print("done_reels = [")
    for reel in done_reels:
        print(f'    "{reel}",')
    print("]")

if __name__ == "__main__":
    main()
