import gettext
_ = gettext.gettext
N_ = gettext.ngettext

#okay
info = "some string"
_('a')   # okay
_("a")   # okay
_("This is find")  # okay

_("This is also fine %s") % info  # okay
_("this multi line"
  "string is fine")   # okay

_("this string has a %(key)s") % {'key': info}  # okay
_("blip % plain percent is fine")  # okay
_("blip %% plain percent and format %s is fine") % info

gettext.gettext("okay to do this as well")

N_("a")
N_("this is fine %s") % info

N_("foo %s" % 2) % info
