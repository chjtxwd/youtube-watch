import feedparser

# Parse the RSS feed
url = "https://freshrss.haijin666.top/i/?a=rss&user=youtube&token=&hours=168"
feed = feedparser.parse(url)

# Print general feed information
print("Feed Title:", feed.feed.title)
print("Feed Link:", feed.feed.link)
print("Feed Description:", feed.feed.description)
print("Feed Last Build Date:", feed.feed.updated)

# Iterate through each item in the feed
for entry in feed.entries:
    print("\nTitle:", entry.title)
    print("Link:", entry.link)
    print("Creator:", entry.get("author", "N/A"))
    print("Description:", entry.description)
    print("Published Date:", entry.published)
    print("GUID:", entry.id)
    print("=" * 40)
