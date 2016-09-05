# FBEraser
Delete your Facebook posts

FBEraser is a command line python tool that logs into your Facebook account, goes to your activity log, and deletes your posts one by one.

Improvements are welcome, as is issue logging.

Branch graph-api re-writes FBEraser using the Facebook graph API. It's a work in progress, since the original version doesn't seem to be very effective anymore.

## Usage
To use this tool, you're responsible to get your own Facebook `access_token`.  The easiest way to do so is to go to the graph API explorer at:

`https://developers.facebook.com/tools/explorer/`

When you click 'Get Token', enable permissions for the posts you want to delete.

Then run `FBEraser -token='[your token]'`

## License
Copyright 2016 Azim Sonawalla

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
