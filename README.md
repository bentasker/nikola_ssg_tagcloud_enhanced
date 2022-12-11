This plugin generates data in JSON format, for display in a tag cloud. 

This is a tweaked fork of [tagcloud](https://plugins.getnikola.com/v8/tagcloud/)

Tag Data is saved into `output/assets/js/tag_cloud_data_enhanced.json`. 

Sample:

```json
{"blog": [1, "/categories/blog/"]}]}
````

You'll need to add div and script tags to pages where you want to display the tags.

For example, to add to the main tag/category pages:
```
nikola theme -c tags.tmpl
```

Then open `themes/<your theme name>/templates/tags.tmpl` in your favourite text editor.

Wherever you want the cloud to be displayed, insert the following
```html
<div id="tag-cloud-wrap"></div>
<div style="clear: both"></div>
<script type="text/javascript" src="/assets/js/tagcloud.js"></script>
<link rel="stylesheet" href="/assets/css/tagcloud.css" />
<script type="text/javascript">buildTagCloud(5);</script>
```

### Configuration

There are a number of configuration variable which can be added to `conf.py` in order to control the tag cloud
```python
# List of tags to be excluded from the cloud (enter as lowercase)
TAGCLOUD_ENHANCED_EXCLUDES = []

# Minimum number of articles for a tag to be considered for the cloud
TAGCLOUD_ENHANCED_MIN_ARTICLES = 4
```
