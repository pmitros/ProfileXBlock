""" This XBlock maintains a student profile page. """

import os.path

import pkg_resources

#import mako

from xblock.core import XBlock
from xblock.fields import Scope, Dict#, String
from xblock.fragment import Fragment

import profile_json

assets = ["email-16.png", "facebook-3-16.png", "github-16.png", "google-plus-4-16.png", "linkedin-16.png", "pages-3-16.png", "phone-16.png", "profile.png", "skype-16.png", "twitter-16.png"]

def replace_template(source, dictionary):
    processed = source
    for key in dictionary:
        processed = processed.replace(key, dictionary[key])
    return processed

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

    # view = String{
    #     default="student", 
    #     scope=Scope.settings
    #     }

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
        params = {
            'PHOTO_URL' : self.runtime.local_resource_url(self, 'public/assets/profile.png')
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
        frag.initialize_js('ProfileXBlock', {'profile_data' : self.user_profile, 
                                             'profile_config':profile_json.profile_config})
        return frag

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
        print field, value
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
