# -*- coding: utf-8 -*-

# Copyright © 2012-2018 Roberto Alsina and others.

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""Render a tag cloud data file."""

import json
import os

from nikola.plugin_categories import Task
from nikola import utils


class RenderTagCloudEnhanced(Task):
    """Render a tag cloud data file."""

    name = "render_tag_cloud_enhanced"

    def gen_tasks(self):
        """Render the tag cloud."""
        self.site.scan_posts()
        yield self.group_task()

        excludes = self.site.config["TAGCLOUD_ENHANCED_EXCLUDES"]
        min_arts = self.site.config['TAGCLOUD_ENHANCED_MIN_ARTICLES']

        # Tag cloud json file
        tag_cloud_data = {}
        for tag, posts in self.site.posts_per_tag.items():
            if tag in self.site.config['HIDDEN_TAGS'] or tag.lower() in excludes:
                continue

            if len(posts) < min_arts:
                continue
            
            tag_cloud_data[tag] = [len(posts), self.site.link(
                'tag', tag, self.site.config['DEFAULT_LANG'])]
        output_name = os.path.join(self.site.config['OUTPUT_FOLDER'],
                                   'assets', 'js', 'tag_cloud_data_enhanced.json')

        def write_tag_data(data):
            """Write tag data into JSON file, for use in tag clouds."""
            utils.makedirs(os.path.dirname(output_name))
            with open(output_name, 'w+') as fd:
                json.dump(data, fd, sort_keys=True)

        task = {
            'basename': str(self.name),
            'name': str(output_name)
        }

        task['uptodate'] = [utils.config_changed(tag_cloud_data, 'nikola.plugins.task.tags:tagdata')]
        task['targets'] = [output_name]
        task['actions'] = [(write_tag_data, [tag_cloud_data])]
        task['clean'] = True
        yield utils.apply_filters(task, self.site.config['FILTERS'])
