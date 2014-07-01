profile_config = {
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
	     { "class" : "ProfileStaticText", 
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
	     { "class" : "ProfileStaticText", 
	       "source" : "photo"},
	     { "class" : "ProfileForm", 
	       "children" : [
		   {"class"    : "ProfileOneLiner", 
		    "question" : "", 
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
	       "children" : [
		   {"class"    : "ProfileOneLiner", 
		    "question" : "Location",
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
		    "choices" : [{"item": "Prefer not to say"}, {"item":"Under 13"}, {"item":"14-17"}, {"item":"18-24"}, {"item":"25-35"}, {"item":"35-50"}, {"item":"Over 50"}]},
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
    ]};
