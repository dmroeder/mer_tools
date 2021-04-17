# mer_tools documentation

To use mer_tools, we must first create an instance, then we can start using it's
built in functions:

```python
from mer_tools import mer
x = mer("my_mer.mer")

audit = x.audit()
print(audit)
```

# audit
When you call audit, it will grab the following information and return it as a list
of strings

- Project name (mer name)
- MER version
- Platform the project was developed in (ME/SE)
- Protection status

# get_version
Returns the version that the MER was compiled in as a string

# get_protection
MER's have 3 protection modes, choosable when you generate a new MER:
- None
- Never allow conversion
- Password protection

This will tell you what protection mode is applied to the mer

# get_platform
Retreives whether the MER was built for ME or SE

# get_project_name
Retreives the original project name since it doesn't necessairily have
to match the MER.  For example, you may choose a new name when making the
MER, or the MER can be renamed after it was compiled

# get_project_structure
Returns a list of the project structure.  This will be most of what you see in the project
tree (screen names, global objects, etc

# get_screen_names
Returns a list of the screen names

# enable_restore
This will make an edit to the MER that sets the protection mode to none

With newer versions of FactoryTalk View Studio ME, when you make runtimes in v6 or earlier,
they are automatically set to not allow conversion back to and project.  This is annoying because
you can't do anything about it.  Using enable_restore() will allow you to convert it back to a project
using the Application Manager.

This will only work on versions where it was possible to convert back at one point.  For example, this
will not help you with v4 or earlier project because there was never a way to convert them back

# get_object
This is an experimental feature that queries a specific object in the project.  You can see some of the
objects from get_project_structure()
