# seat-inspect

seat-inspect tries to make the status of the login/seat system visible, to help
with understanding and troubleshooting.

The intent of running the code is to have an overview of the system status, both
to see what the new facilities are about, and to figure out if there is
something out of place.

The intent of reading the code is to have an idea of how to use these
facilities: the code has been written to be straightforward and is annotated
with relevant bits from the [logind API documentation](http://www.freedesktop.org/wiki/Software/systemd/logind/).

See also [here](http://www.freedesktop.org/wiki/Software/systemd/multiseat/)
for general definitions.
