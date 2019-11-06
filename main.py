# Copyright 2018, Google, LLC.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests

def handle_new_entity_data(data, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This generic function logs relevant data when a file is changed.

    Args:
        data (dict): The Cloud Functions event payload.
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Stackdriver Logging
    """

    url = 'https://wikiload-u236eyd74a-uc.a.run.app/'
    event = context.event_type
    bucket = data['bucket']
    object = data['name']

    if event == 'google.storage.object.finalize' \
      and bucket == 'wiki-staging' \
      and object == 'dumps.wikimedia.org/wikidatawiki/entities/latest-all.json.bz2-x':
        resp = requests.get(url)
        print(resp.text)
