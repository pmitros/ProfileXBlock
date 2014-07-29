""" This XBlock maintains a student profile page. """

import os.path

import pkg_resources

import json

from webob.response import Response
from PIL import Image

from xblock.core import XBlock
from xblock.fields import Scope, Dict, String
from xblock.fragment import Fragment
from xblock.reference.plugins import Filesystem

from xblockfuture import futureclass

import profile_json

assets = ["email-16.png", "facebook-3-16.png", "github-16.png", "google-plus-4-16.png", "linkedin-16.png", "pages-3-16.png", "phone-16.png", "profile.png", "skype-16.png", "twitter-16.png"]

def replace_template(source, dictionary):
    processed = source
    for key in dictionary:
        processed = processed.replace(key, dictionary[key])
    return processed

image_types = {
    'jpeg' : {
        'extension': [".jpeg", ".jpg"],
        'mimetypes': ['image/jpeg', 'image/pjpeg'],
        'magic': ["ffd8"]
        },
    'png': {
        'extension': [".png"],
        'mimetypes': ['image/png'],
        'magic': ["89504e470d0a1a0a"]
        },
    'gif': {
        'extension': [".gif"],
        'mimetypes': ['image/gif'],
        'magic': ["474946383961", "474946383761"]
        }
    }

class SuspiciousOperation(Exception):
    pass

class WTFException(Exception):
    pass

def ValidatePhoto(request):
    """
    Take a request, and return a photo embedded in that
    request, validating that file extension, mime-type, and magic
    number all match.

    We'd rather eventually find a way to do away with this
    code. Specifically, we don't want big binary blobs passing through
    memory. We'd like them to go directly to S3. We haven't figured
    out the right APIs for this yet, and this works in the interrim. 

    Takes a webob request. Returns a tuple of the photo extension and
    the photo content.
    """
    # First, check if the file extension is in image_types
    filename = str(request.POST['file'].file).lower()
    filetype = [ft for ft in image_types if any(filename.endswith(ext) for ext in image_types[ft]['extension'])]
    if not filetype:
        return None
    
    if len(filetype)!=1: 
        raise WTFException

    filetype = filetype[0]

    # Next, check magic number
    headers = image_types[filetype]['magic']
    if request.POST['file'].file.read(len(headers[0])/2).encode('hex') not in headers:
        raise SuspiciousOperation("Mismatch between file type and header")
    request.POST['file'].file.seek(0)

    # Finally, check mimetype
    if request.POST['file'].file.content_type not in image_types[filetype]['mimetypes']:
        raise SuspiciousOperation("Mismatch between file type and mimetype")

    # TODO: Go block-by-block
    content = request.POST['file'].file
    return (filetype, content)


@futureclass()
@XBlock.needs('fs')
class ProfileXBlock(XBlock):
    """
    This XBlock maintains a student profile page. 
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    user_profile = Dict(
        default={}, scope=Scope.user_state,
        help="The user's profile information",
    )

    view = String(
        default="student", 
        scope=Scope.settings
    )

    photo_storage = Filesystem(
        scope=Scope.user_state
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def peer_view(self, context=None):
        return "Hello"

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the ProfileXBlock, shown to students
        when viewing courses.
        """
        photo_url = self.runtime.local_resource_url(self, 'public/assets/profile.png')
        if self.photo_storage.exists("profile.png"):
            photo_url = self.photo_storage.get_url("profile.png", 600)
        params = {
            'PHOTO_URL': photo_url
            }
        for asset in assets:
            params[asset] = self.runtime.local_resource_url(self, os.path.join("public/assets",asset))
        html = replace_template(self.resource_string("static/html/profile.html"), params)
        frag = Fragment(html)
        frag.add_javascript_url(self.runtime.local_resource_url(self, 'public/3rdParty/mustache.js'))
        frag.add_css_url(self.runtime.local_resource_url(self, 'public/3rdParty/jquery-ui.css'))
        frag.add_javascript_url(self.runtime.local_resource_url(self, 'public/3rdParty/jquery-ui.min.js'))

# TODO: This would give nicer selects
#        frag.add_css(self.resource_string("static/3rdparty/jquery.dropdown.css"))
#        frag.add_javascript(self.resource_string("static/3rdparty/jquery.dropdown.min.js"))
        frag.add_css(self.resource_string("static/css/profile.css"))
        frag.add_javascript(self.resource_string("static/js/src/profile.js"))
        profile_config = profile_json.profile_config
        if self.view.lower() ==  "peer":
                    profile_config = profile_json.peer_profile_config
        frag.initialize_js('ProfileXBlock', {'profile_data': self.user_profile, 
                                             'profile_config':profile_config})
        return frag

    @XBlock.handler
    def upload_photo(self, request, suffix=''):
        """
        Handle a profile photo upload. 
        * Step 1: Validate that image (magic number, mimetype, and extension all match)
        * Step 2: Resize to a maximum of 211x211
        * Step 3: Save as profile.png with PIL
        """
        (extension, photo) = ValidatePhoto(request)

        im = Image.open(photo)
        im.thumbnail((211,211), Image.ANTIALIAS)
        fp = self.photo_storage.open("profile.png", "wb")
        im.save(fp, "PNG")
        fp.close()

        response = Response()
        response.body = json.dumps({'status': 'success', 
                                   'url': self.photo_storage.get_url("profile.png", 600)})
        response.headers['Content-Type'] = 'text/json'
        return response

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def update_profile(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        field = data['field']
        value = data['value']
        if not isinstance(value, basestring):
            raise TypeError("Fields must be strings. This exception indicates either a bug or a hacking attempt.")
        self.user_profile[field] = value;

        return {'status':'success'}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("ProfileXBlock, edit view",
             """<vertical_demo>
                <profile view="student" name="profile">
                </profile>
                </vertical_demo>
             """),
            ("ProfileXBlock, peer view",
             """<vertical_demo>
                <profile view="peer" name="profile">
                </profile>
                </vertical_demo>
             """),
        ]
