# voyagerOverdues
This script extracts information about overdue, etc., items from ExLibris' Voyager integrated library system's crcnotes report. The best way to get this information is to use the Reporter module, but one of our libraries does not want notices sent without staff first checking the shelves. This gives them that information and then they can contact the patron manually.

Note: When pulling the crcnotes file from the Voyager server, rename the copy left on the server (example: crcnotes.B-Circ.inp.old). If this isn't done, Voyager will keep appending information to it rather than creating a new file.
