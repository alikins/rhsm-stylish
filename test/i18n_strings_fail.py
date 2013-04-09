import gettext
_ = gettext.gettext
N_ = gettext.ngettext


# fail
_('')
_("")
# there are cases where this is okay, but usually not
_(info)

_("blip %s" % info)
_("Bob" + " foo")
_("blip" + \
  "bloop")
_("whatever %s" % info)
_("this string has a %(key)s but fails" % {'key': info})
_('format strings {info} are okay but xgettext doesnt extrac them'.format(info))

# this should fail
#gettext.gettext("blip %s" % info)
