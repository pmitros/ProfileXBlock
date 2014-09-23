import csv
import json
import os, os.path
import subprocess
import sys

# Location of the read replica machine
replica = sys.argv[1]

def decode_json(item):
    '''
    Load JSON as escaped by MySQL
    '''
    try:
        item = item.replace('\\\\' ,'\\')
        return json.loads(item)
    except ValueError:
        print item
        return item

def fix_dict(d):
    '''
    We'd like to put keys in a JavaScript template. We want to kill
    dots. We replace them with underscores. 
    '''
    for key in list(d):
        value = d[key]
        del d[key]
        d[key.replace(".","_")] = value

# Grab the profiles from student_module
profile_str = subprocess.check_output(['ssh', replica, './profile_pages.sh'])
# Parse them into a proper table
profile_items = [x.split('\t') for x in profile_str.split('\n')]
# MySQL Headers are in row 1
keys = profile_items[0]
# Remaining rows are data
profile_items = profile_items[1:]
# Convert each row into a dictionary mapping keys to data
profile_items = [dict(zip(keys, item)) for item in profile_items if len(item) > 1]
# Decode JSON of state, and put it in the top-level dictionary
profile_items = [dict({'student_id': i['student_id']}, **decode_json(i['state'])['user_profile']) for i in profile_items]
# Add URLs for student photos, if they exist. This presumes we downloaded XBlock storage from S3.
for item in profile_items:
    filename = "i4x-_._._edX._edX__Insider._profile._Profile/photo__storage/{id}/profile.png".format(id=item['student_id'])
    if(os.path.exists(filename)):
        item['photo'] = filename
    else:
        item['photo'] = "profile.png"
    # While we're at it, clean up keys to not have dots (so they work for CSS)
    fix_dict(item)

# Sort the users in alphabetical order
profile_items.sort(key=lambda x:x['edx_name'])

# And dump them into a JSON file
f = open("profiles.json", "w")
f.write(json.dumps(profile_items, sort_keys=True, indent=2))
f.close()

# Finally, we print out the list of keys used, so we can make sure we handle them all correctly
print "\n".join(sorted(list(set(sum([k.keys() for k in profile_items], [])))))

