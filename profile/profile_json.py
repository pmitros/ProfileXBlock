edx_profile_config = {
    "class" : "ProfileMainBlock", 
    "children" : [
	{"class" : "ProfileColumn", 
	 "children" : [
	     { "class" : "ProfileStaticText", 
	       "source" : "profile_overview"},
	     { "class" : "ProfileForm", 
	       "title" : "Contact Information", 
	       "children" : [
		   {"class"    : "ProfileOneLiner", 
		    "question" : "Name", 
		    "field" : "edx_name",
		    "placeholder" : "Your name" },
		   {"class" : "ProfileContactInfo", 
		    "children": [
			{"label":"Telephone", 
			 "field":"edx_phone",
			 "class":"ProfileContactBox", 
			 "placeholder" : "1(617)234-5678",
			 "icon" : "phone"
			},
			{"label":"E-mail:", 
			 "field":"edx_email",
			 "class":"ProfileContactBox", 
			 "placeholder" : "jsmith@edx.org",
			 "icon" : "email"
			},
			{"label":"Web site: ", 
			 "field":"edx_website",
			 "class":"ProfileContactBox", 
			 "placeholder" : "http://www.edx.org/",
			 "icon" : "pages"
			},
			{"label":"Skype username", 
			 "field":"edx_skype",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "skype"
			},
			{"label":"http://facebook.com/", 
			 "field":"edx_facebook",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "facebook",
			 "help" : "For help reserving a Facebook URL, see https://www.facebook.com/help/200712339971750#How-do-I-customize-my-timeline-or-Page-address?-Where-can-I-claim-a-username?"
			},
			{"label":"http://plus.google.com/", 
			 "field":"edx_googleplus",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "google-plus"
			},
			{"label":"http://github.com/", 
			 "field":"edx_github",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "github"
			},
			{"label":"http://linkedin.com/in/", 
			 "field":"edx_linkedin",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "linkedin", 
			 "help": "For help reserving a LinkedIn URL, see http://help.linkedin.com/app/answers/detail/a_id/87"
			},
			{"label":"http://twitter.com/", 
			 "field":"edx_twitter",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "twitter"
			}
		   ]}
	       ]},
	     { "class" : "ProfileForm", 
	       "title" : "Demographics", 
	       "children" : [
		   {"class"    : "ProfileOneLiner", 
		    "question" : "Where do you live?",
		    "field" : "location", 
		    "placeholder" : "East Cambridge" },
		   {"class"    : "ProfileTextArea", 
		    "question" : "What languages are you fluent in?", 
		    "placeholder" : "English", 
		    "field" : "edx_languages",
		    "rows":2},
		   {"class"    : "ProfileDropDown", 
		    "field"    : "edx_age", 
		    "question" : "How old are you?", 
		    "choices" : [{"item": "Prefer not to say"}, {"item":"Under 13"}, {"item":"14-17"}, {"item":"18-24"}, {"item":"25-35"}, {"item":"35-50"}, {"item":"Over 50"}]}
	       ]}
	 ]},
	{"class" : "ProfileColumn", 
	 "children" : [
	     { "class" : "ProfilePhoto", 
	       "source" : "photo"},
	     { "class" : "ProfileForm", 
	       "title" : "Background", 
	       "children" : [
		   {"class"    : "ProfileTextArea", 
		    "question" : "What part of the organization are you in?",
		    "field" : "org-position", 
		    "placeholder" : "Engineering/Teaching and Learning" },
		   {"class"    : "ProfileTextArea", 
		    "question" : "What is your background in education? Have you taught? Are you familiar with any areas of education research? Ed-tech? Psychology? Etc?", 
		    "placeholder" : "I'm a developer; not much education per-se, but I do have a strong background in gamification", 
		    "field" : "cphys.edbackground",
		    "rows":4},
		   {"class"    : "ProfileTextArea", 
		    "question" : "What is your background in technology? Front-end? Back-end? Product? UX? How familiar are you with the edX platform?", 
		    "field" : "cphys.techbackground",
		    "placeholder" : "I am a back-end developer, but I do enjoy graphic design. Still need to learn CSS, though.", 
		    "rows":3},
		   {"class"    : "ProfileTextArea", 
		    "question" : "Tell us a bit about yourself. Write a brief bio.", 
		    "placeholder" : "Biographical Information", 
		    "field" : "cphys.bio",
		    "rows":4},
		   {"class"    : "ProfileTextArea", 
		    "question" : "Finally, what drew you to edX? Why are you here?", 
		    "placeholder" : "I want to modernize education in Walachia", 
		    "field" : "motiviation",
		    "rows":4}
	       ]}
	 ]}
    ]}






physics_profile_config = {
    "class" : "ProfileMainBlock", 
    "children" : [
	{"class" : "ProfileColumn", 
	 "children" : [
	     { "class" : "ProfileStaticText", 
	       "source" : "profile_overview"},
	     { "class" : "ProfileForm", 
	       "title" : "Contact Information", 
	       "children" : [
		   {"class"    : "ProfileOneLiner", 
		    "question" : "Name", 
		    "field" : "edx_name",
		    "placeholder" : "Your name" },
		   {"class" : "ProfileContactInfo", 
		    "children": [
			{"label":"Telephone", 
			 "field":"edx_phone",
			 "class":"ProfileContactBox", 
			 "placeholder" : "1(617)234-5678",
			 "icon" : "phone"
			},
			{"label":"E-mail:", 
			 "field":"edx_email",
			 "class":"ProfileContactBox", 
			 "placeholder" : "jsmith@edx.org",
			 "icon" : "email"
			},
			{"label":"Web site: ", 
			 "field":"edx_website",
			 "class":"ProfileContactBox", 
			 "placeholder" : "http://www.edx.org/",
			 "icon" : "pages"
			},
			{"label":"Skype username", 
			 "field":"edx_skype",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "skype"
			},
			{"label":"http://facebook.com/", 
			 "field":"edx_facebook",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "facebook",
			 "help" : "For help reserving a Facebook URL, see https://www.facebook.com/help/200712339971750#How-do-I-customize-my-timeline-or-Page-address?-Where-can-I-claim-a-username?"
			},
			{"label":"http://plus.google.com/", 
			 "field":"edx_googleplus",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "google-plus"
			},
			{"label":"http://github.com/", 
			 "field":"edx_github",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "github"
			},
			{"label":"http://linkedin.com/in/", 
			 "field":"edx_linkedin",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "linkedin", 
			 "help": "For help reserving a LinkedIn URL, see http://help.linkedin.com/app/answers/detail/a_id/87"
			},
			{"label":"http://twitter.com/", 
			 "field":"edx_twitter",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "twitter"
			}
		   ]}
	       ]},
	     { "class" : "ProfileForm", 
	       "title" : "Demographics", 
	       "children" : [
		   {"class"    : "ProfileOneLiner", 
		    "question" : "Where do you live?",
		    "field" : "location", 
		    "placeholder" : "Toronto, Canada" },
		   {"class"    : "ProfileTextArea", 
		    "question" : "What languages are you fluent in?", 
		    "placeholder" : "English", 
		    "field" : "edx_languages",
		    "rows":2},
		   {"class"    : "ProfileDropDown", 
		    "field"    : "edx_age", 
		    "question" : "How old are you?", 
		    "choices" : [{"item": "Prefer not to say"}, {"item":"Under 13"}, {"item":"14-17"}, {"item":"18-24"}, {"item":"25-35"}, {"item":"35-50"}, {"item":"Over 50"}]}
	       ]}
	 ]},
	{"class" : "ProfileColumn", 
	 "children" : [
	     { "class" : "ProfilePhoto", 
	       "source" : "photo"},
	     { "class" : "ProfileForm", 
	       "title" : "Background", 
	       "children" : [
		   {"class"    : "ProfileTextArea", 
		    "question" : "What is your background in education? Have you taught? Taught physics? Are you involved in education research? Ed-tech? Etc?", 
		    "placeholder" : "Background in education and physics education", 
		    "field" : "cphys.edbackground",
		    "rows":3},
		   {"class"    : "ProfileTextArea", 
		    "question" : "What is your background in technology? Are you a neophyte? A power user? Do you program? Do you know HTML? Python? Javascript?  How well?", 
		    "field" : "cphys.techbackground",
		    "placeholder" : "Background in technology", 
		    "rows":3},
		   {"class"    : "ProfileTextArea", 
		    "question" : "Tell us a bit about yourself. Write a brief bio.", 
		    "placeholder" : "Biographical Information", 
		    "field" : "cphys.bio",
		    "rows":4}
	       ]}
	 ]}
    ]}

peer_profile_config = { 
    "class" : "ProfileMainBlock", 
    "children" : [
	{"class" : "ProfileColumn", 
	 "children" : [
	     { "class" : "ProfilePhoto", 
	       "source" : "photo"},
             {"class"    : "ProfileTextArea", 
              "placeholder" : "Biographical Information", 
              "field" : "cphys.bio",
              },
		   {"class"    : "ProfileOneLiner", 
		    "question" : "Location",
		    "field" : "location", 
		    "placeholder" : "Toronto, Canada" },
		   {"class"    : "ProfileTextArea", 
		    "question" : "Languages:", 
		    "placeholder" : "English", 
		    "field" : "edx_languages",
		    "rows":2},
		   {"class"    : "ProfileTextArea", 
		    "question" : "Education background", 
		    "field" : "cphys.edbackground",
                    },
		   {"class"    : "ProfileTextArea", 
		    "question" : "Technology background", 
		    "field" : "cphys.techbackground",
                    },
		   {"class"    : "ProfileDropDown", 
		    "field"    : "edx_age", 
		    "question" : "How old are you?", 
		    "choices" : [{"item": "Prefer not to say"}, {"item":"Under 13"}, {"item":"14-17"}, {"item":"18-24"}, {"item":"25-35"}, {"item":"35-50"}, {"item":"Over 50"}]},
	     { "class" : "ProfileForm", 
	       "children" : [
		   {"class"    : "ProfileOneLiner", 
		    "question" : "", 
		    "field" : "edx_name",
		    "placeholder" : "Your name" },
		   {"class" : "ProfileContactInfo", 
		    "children": [
			{"label":"Phone", 
			 "field":"edx_phone",
			 "class":"ProfileContactBox", 
			 "placeholder" : "1(617)234-5678",
			 "icon" : "phone"
			},
			{"label":"e-mail", 
			 "field":"edx_email",
			 "class":"ProfileContactBox", 
			 "placeholder" : "jsmith@edx.org",
			 "icon" : "email"
			},
			{"label":"web", 
			 "field":"edx_website",
			 "class":"ProfileContactBox", 
			 "placeholder" : "http://www.edx.org/",
			 "icon" : "pages"
			},
			{"label":"Skype", 
			 "field":"edx_skype",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "skype"
			},
			{"label":"Facebook", 
			 "field":"edx_facebook",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "facebook",
			 "help" : "For help reserving a Facebook URL, see https://www.facebook.com/help/200712339971750#How-do-I-customize-my-timeline-or-Page-address?-Where-can-I-claim-a-username?"
			},
			{"label":"Google+", 
			 "field":"edx_googleplus",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "google-plus"
			},
			{"label":"github", 
			 "field":"edx_github",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "github"
			},
			{"label":"linkedin", 
			 "field":"edx_linkedin",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "linkedin", 
			 "help": "For help reserving a LinkedIn URL, see http://help.linkedin.com/app/answers/detail/a_id/87"
			},
			{"label":"twitter", 
			 "field":"edx_twitter",
			 "class":"ProfileContactBox", 
			 "placeholder" : "",
			 "icon" : "twitter"
			}
                        ]}
                   ]},
             ]}
        ]}

profile_config = edx_profile_config
