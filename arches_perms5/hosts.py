import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(
        re.sub(r"_", r"-", r"arches_perms5"), "arches_perms5.urls", name="arches_perms5"
    ),
)
