![Canadian Atheist](canatheist.svg)

Canadian Atheist calendar data
==============================

This repository contains the data for the [Canadian Atheist] calendar.

The Canadian Atheist calendar can be found at
<https://www.canadianatheist.com/calendar.ics>.

Data structure
--------------

The data for the calendar is stored as [xCal] `vevent` components, each in its
own XML file in the `data` directory or its subdirectories.

A separate tool scans all the XML files in the `data` directory, and then
combines all the components into a master xCal file. That file is then
transformed to iCal format before being stored on the Canadian Atheist server.

Validation tools are provided in the `util` directory, so that components can
be checked for validity.

Adding new events
-----------------

If you have an event you would like to see added to the Canadian Atheist
calendar, you have several options.

The easiest way would be to simply use the [Canadian Atheist contact form],
and give Canadian Atheist’s editors all the information. They will then add
the event for you.

Another option is to create an issue on the [issues list].

Finally, you could also create a pull request if you want to add the event
manually:

1.  First fork the Canadian Atheist calendar data repository.
2.  In your own fork, create a new branch. Give it a descriptive name.
3.  In that branch, add the new event(s) as XML files in the `data` directory.
4.  Once you are satisfied with your new events, create a pull request.

[Canadian Atheist]: https://www.canadianatheist.com/
[Canadian Atheist contact form]: https://www.canadianatheist.com/contact/
[issues list]: https://github.com/DarkerStar/canatheist-calendar-data/issues
[xCal]: https://en.wikipedia.org/wiki/XCal
