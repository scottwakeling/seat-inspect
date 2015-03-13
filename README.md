[![Build Status](https://travis-ci.org/scottwakeling/seat-inspect.svg?branch=master)](https://travis-ci.org/scottwakeling/seat-inspect)

# seat-inspect
seat-inspect is a command line tool for producing status reports of systemd
facilities such as Multi-Seat, Inhibitor Locks, Services, Targets, and other
types of Unit.

The intent of running the code is to have an overview of the system status,
both to see what the new facilities are about, and to figure out if there is
something out of place.

The intent of reading the code is to have an idea of how to use these
facilities: the code has been written to be straightforward and is annotated
with relevant bits from the [logind](http://www.freedesktop.org/wiki/Software/systemd/logind/) and [systemd D-Bus](http://www.freedesktop.org/wiki/Software/systemd/dbus/) API documentation.

See also [here](http://www.freedesktop.org/wiki/Software/systemd/multiseat/)
for general definitions, and the Documentation for Developers section over [here](http://www.freedesktop.org/wiki/Software/systemd/)
for more detailed information.


## EXAMPLE OUTPUT

    sudo seat-inspect
    ...
    - foo.service (loaded failed failed)
        - result: exit-code since: 2015-03-05 22:40:25
            - 2015-03-05 22:40:25 roth systemd[1]: foo.service: control process
            exited, code=exited status=203
            - 2015-03-05 22:40:25 roth systemd[1]: Failed to start a foo that
            will not bar.
                - Subject: Unit foo.service has failed
            - Defined-By: systemd
            - Support: http://lists.freedesktop.org/mailman/listinfo/systemd-devel
            - Unit foo.service has failed.
            - The result is failed.
            - 2015-03-05 22:40:25 roth systemd[1]: Unit foo.service entered
            failed state.
    ...
    - morningalarm.timer (loaded active waiting)
        - Description: "morning alarm"
        - Next elapse: 2015-03-09 07:30:00
    ...
    Current inhibitor locks:
        - handle-power-key:handle-suspend-key:handle-hibernate-key (block) by
        scott (GNOME handling keypresses) uid 1000 pid 1449
        - sleep (delay) by NetworkManager (NetworkManager needs to turn off
        networks) uid 0 pid 654
        - shutdown:sleep (delay) by Telepathy (Disconnecting IM accounts before 
        suspend/shutdown...) uid 1000 pid 1511
        - sleep (delay) by scott (GNOME needs to lock the screen)
        uid 1000 pid 1449
        - sleep (delay) by GNOME Shell (GNOME needs to lock the screen)
        uid 1000 pid 1525
    ...


## NOTES

seat-inspect is not a finished tool, but a starting point. Enrico Zini put
the first verison on github hoping that people would fork it and add their own
extra sanity checks and warnings, that it could grow not only into a standard
thing to run if a system acts weird, but also a standard thing to hack on for
those trying to learn more about Multi-Seat and systemd.

As it is now, it should be able to issue warnings if some bits are missing for
network-manager or shutdown functions to work correctly, or if some Devices or
Services are having problems. It all needs more testing by people with systems
that are experiencing such issues.

Tinkering with the code can be an interesting way to explore the new
functionalities that we recently grew. Ofcourse, the same can be done, and in
more detail, with `loginctl`, `systemctl`, and `journalctl` calls of various
configuration, but seat-inspect provides the only high-level view of everything.

