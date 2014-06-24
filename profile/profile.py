""" This XBlock maintains a student profile page. """

import pkg_resources

import mako

from xblock.core import XBlock
from xblock.fields import Scope, Integer
from xblock.fragment import Fragment


class ProfileXBlock(XBlock):
    """
    This XBlock maintains a student profile page. 
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the ProfileXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/profile.html")
        frag = Fragment(html)
        frag.add_css(self.resource_string("static/css/profile.css"))
        frag.add_javascript(self.resource_string("static/js/src/profile.js"))
        frag.initialize_js('ProfileXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("ProfileXBlock",
             """<vertical_demo>
                <profile>
- - Educational background
  - question: What is your background in education? Have you taught? Taught physics? Are you involved in education research? Ed-tech? Etc? 
    field: textarea
- - Technology background
  - question: What is your background in technology? Are you a neophyte? A power user? Do you program? Do you know HTML? Python? Javascript? How well? 
    field: textarea
- - Age range 
  - question: Please select your age range
    field: ["0-17", "18-20", "21-25", "26-35", "36-50", "51+"]
- - Language 
  - question: What is your native language?
    field: textline
- - Bio
  - question: Please enter your bio
    field: textarea
                </profile>
                </vertical_demo>
             """),
        ]
